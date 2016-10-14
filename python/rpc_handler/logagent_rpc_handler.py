#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import time
import importlib

class handler:
	def __init__(self, args):
		self.args = args
		self.rpc_proto = None
		self._get_rpc_proto()

	def _get_rpc_proto(self):
		absolute_path = os.path.dirname(os.path.abspath(os.path.join(__file__, '..')))
		for python_path in os.getenv('PYTHONPATH').split(':'):
			if absolute_path.startswith(python_path):
				rootpath = os.path.relpath(absolute_path, python_path).replace(os.path.sep, '.')
				self.rpc_proto = importlib.import_module('.rpc_proto.logagent_rpc_proto', rootpath)
				break
		else:
			raise IOError('%s is not in PYTHONPATH' % (__file__))

	#@req : debugmsg
	def critical(self, m):
		req = self.rpc_proto.debugmsg()
		req.from_msgpack(m)

		########add logic code here########
		self.args['debuglog'].critical(req.value)

		########end logic code########

		pass

	#@req : debugmsg
	def error(self, m):
		req = self.rpc_proto.debugmsg()
		req.from_msgpack(m)

		########add logic code here########
		self.args['debuglog'].error(req.value)

		########end logic code########

		pass

	#@req : debugmsg
	def warning(self, m):
		req = self.rpc_proto.debugmsg()
		req.from_msgpack(m)

		########add logic code here########
		self.args['debuglog'].warning(req.value)

		########end logic code########

		pass

	#@req : debugmsg
	def info(self, m):
		req = self.rpc_proto.debugmsg()
		req.from_msgpack(m)

		########add logic code here########
		self.args['debuglog'].info(req.value)

		########end logic code########

		pass

	#@req : debugmsg
	def debug(self, m):
		req = self.rpc_proto.debugmsg()
		req.from_msgpack(m)

		########add logic code here########
		self.args['debuglog'].debug(req.value)

		########end logic code########

		pass

	#@req : opmsg
	def opreport(self, m):
		req = self.rpc_proto.opmsg()
		req.from_msgpack(m)

		########add logic code here########
		self.args['oplog'].insert(req)

		########end logic code########

	#@req : opqueryreq
	#@res : opqueryres
	def opquery(self, m):
		req = self.rpc_proto.opqueryreq()
		req.from_msgpack(m)

		########add logic code here########
		oplog_list = self.args['oplog'].query(req)

		########end logic code########

		res = self.rpc_proto.opqueryres()
		for oplog in oplog_list:
			msg = self.rpc_proto.opmsg()
			msg.time = int(time.mktime(oplog.time.timetuple()))
			msg.user = oplog.user
			msg.action = oplog.action
			msg.args = oplog.args
			msg.others = oplog.others
			res.oplogs.append(msg)
		return res

	#@req : webmsg
	def webreport(self, m):
		req = self.rpc_proto.webmsg()
		req.from_msgpack(m)

		########add logic code here########

		########end logic code########

		pass

	#@req : busimsg
	def busireport(self, m):
		req = self.rpc_proto.busimsg()
		req.from_msgpack(m)

		########add logic code here########

		########end logic code########

		pass

