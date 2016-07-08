#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import ConfigParser
import msgpackrpc
import traceback

class Client(object):
	def __init__(self, conffile, module=None):
		try:
			conf = ConfigParser.ConfigParser()
			conf.read(conffile)
			addr = msgpackrpc.Address(conf.get('server', 'ip'), conf.getint('server', 'port'))
			self.client = msgpackrpc.Client(addr)
			self.module = module
		except Exception,e:
			print traceback.format_exc()
			sys.exit()

	def setmodule(self, module):
		self.module = module

	#@param msg : logmsg
	#@return : no
	def critical(self, msg):
		msg.value = '[%s] %s' % (self.module, msg.value) 
		self.client.notify('critical', msg)

	#@param msg : logmsg
	#@return : no
	def error(self, msg):
		msg.value = '[%s] %s' % (self.module, msg.value) 
		self.client.notify('error', msg)

	#@param msg : logmsg
	#@return : no
	def warning(self, msg):
		msg.value = '[%s] %s' % (self.module, msg.value) 
		self.client.notify('warning', msg)

	#@param msg : logmsg
	#@return : no
	def info(self, msg):
		msg.value = '[%s] %s' % (self.module, msg.value) 
		self.client.notify('info', msg)

	#@param msg : logmsg
	#@return : no
	def debug(self, msg):
		msg.value = '[%s] %s' % (self.module, msg.value) 
		self.client.notify('debug', msg)

