#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
import getopt
import ConfigParser
import traceback
import daemonize
import ctypes
import gevent
import multiprocessing
from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool
import logagent_proto

libc = ctypes.CDLL('libc.so.6')

import msgpackrpc
import logagent_rpc_handler

rpc_worker_pool = None

import logging
import logging.config
logger = None

class RPCHandler(object):
	def critical(self, msg):
		msg_data = logagent_proto.logmsg()
		msg_data.from_msgpack(msg)
		res = rpc_worker_pool.apply_async(logagent_rpc_handler.critical, (logger, msg_data,))

	def error(self, msg):
		msg_data = logagent_proto.logmsg()
		msg_data.from_msgpack(msg)
		res = rpc_worker_pool.apply_async(logagent_rpc_handler.error, (logger, msg_data,))

	def warning(self, msg):
		msg_data = logagent_proto.logmsg()
		msg_data.from_msgpack(msg)
		res = rpc_worker_pool.apply_async(logagent_rpc_handler.warning, (logger, msg_data,))

	def info(self, msg):
		msg_data = logagent_proto.logmsg()
		msg_data.from_msgpack(msg)
		res = rpc_worker_pool.apply_async(logagent_rpc_handler.info, (logger, msg_data,))

	def debug(self, msg):
		msg_data = logagent_proto.logmsg()
		msg_data.from_msgpack(msg)
		res = rpc_worker_pool.apply_async(logagent_rpc_handler.debug, (logger, msg_data,))

class Service:
	def __init__(self, argv):
		self.daemon = False
		self.conffile = ''
		self.conf = ConfigParser.ConfigParser()
		self.parse_opts(argv)
		self.parse_conf(argv)

	def parse_opts(self, argv):
		try:
			opts, args = getopt.getopt(argv[1:], "df:h")
		except getopt.GetoptError:
			self.print_usage(argv)
			sys.exit()
		for op, value in opts:
			if op == '-d':
				self.daemon = True
			elif op == '-f':
				self.conffile = value
			else:
				self.print_usage(argv)
				sys.exit()

	def parse_conf(self, argv):
		if self.conffile != '' and os.path.exists(self.conffile):
			try:
				self.conf.read(self.conffile)
			except Exception,e:
				print traceback.format_exc()
				sys.exit()
		else:
			self.print_usage(argv)
			sys.exit()

	def print_usage(self, argv):
		print 'Usage:'
		print '\t%s -f /path/to/svr.conf -d' % (argv[0])
		print 'Options:'
		print '\t-f\tserver configure file'
		print '\t-d\trun as daemon'
		print '\t-h\tshow help'

	def start(self):
		if self.daemon:
			daemon = daemonize.Daemonize(
				app = self.conf.get('app', 'name'),
				pid = self.conf.get('app', 'pid'),
				action = self.start_server,
				auto_close_fds = False)
			daemon.start()
		else:
			self.start_server()

	def rpc_worker_process_init(self):
		libc.prctl(1, 15)

	def start_rpc_server(self, rpc_worker_type, rpc_worker_sum):
		if rpc_worker_type == 'process':
			libc.prctl(1, 15)

		global rpc_worker_pool, logger
		logging.config.fileConfig(self.conffile)
		logger = logging.getLogger()

		if rpc_worker_type == 'process':
			rpc_worker_pool = ProcessPool(
					processes = rpc_worker_sum,
					initializer = self.rpc_worker_process_init)
		elif rpc_worker_type == 'thread':
			rpc_worker_pool = ThreadPool(
					processes = rpc_worker_sum)
		else:
			raise TypeError('type of self worker_type isnot correct!')

		addr = msgpackrpc.Address(
				host = self.conf.get('rpc_server', 'ip'),
				port = self.conf.getint('rpc_server', 'port'))
		server = msgpackrpc.Server(RPCHandler())
		server.listen(addr)
		server.start()

		rpc_worker_pool.close()
		rpc_worker_pool.join()

	def create_rpc_server_manager(self):
		try:
			rpc_worker_type = self.conf.get('rpc_server', 'worker_type')
			rpc_worker_sum = self.conf.getint('rpc_server', 'worker_sum')
		except Exception,e:
			print traceback.format_exc()
			sys.exit()

		rpc_server_manager = None
		if rpc_worker_type == 'process':
			rpc_server_manager = multiprocessing.process.Process(
					target = self.start_rpc_server,
					args = (rpc_worker_type, rpc_worker_sum))
		elif rpc_worker_type == 'thread':
			rpc_server_manager = multiprocessing.dummy.DummyProcess(
					target = self.start_rpc_server,
					args = (rpc_worker_type, rpc_worker_sum))
		else:
			raise TypeError('type of rpc worker_type isnot correct!')
		return rpc_server_manager

	def start_server(self):
		rpc_server_manager_dead = True
		self_server_manager_dead = True

		while 1:
			if rpc_server_manager_dead:
				rpc_server_manager = self.create_rpc_server_manager()
				rpc_server_manager.start()
				rpc_server_manager_dead = False

			if not rpc_server_manager_dead:
				rpc_server_manager.join(1)
				if not rpc_server_manager.is_alive():
					rpc_server_manager_dead = True

if __name__ == '__main__':
	Service(sys.argv).start()

