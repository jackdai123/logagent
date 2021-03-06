#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
import traceback

class RPCHandler:
	def __init__(self, args):
		rpc_handler_dir = os.path.dirname(os.path.abspath(__file__))
		files = os.listdir(rpc_handler_dir)
		if rpc_handler_dir not in sys.path:
			sys.path.append(rpc_handler_dir)
		self.func_map = {}
		loaded_modules = set()

		for f in files:
			if f.find('_rpc_handler.py') == -1:
				continue

			module_name, ext = os.path.splitext(f)
			if module_name in loaded_modules:
				continue

			try:
				module = __import__(module_name)
				loaded_modules.add(module_name)
				rpc_handler = module.handler(args)
				for func in dir(module.handler):
					if func.startswith('_'):
						continue
					self.func_map[func] = rpc_handler
			except Exception as e:
				print 'import %s module %s' % (module_name, traceback.format_exc())

		self.rpc_worker_pool = args['rpc_worker_pool']

	def critical(self, req):
		res = self.rpc_worker_pool.apply_async(self.func_map['critical'].critical, (req,))
		return res.get()

	def error(self, req):
		res = self.rpc_worker_pool.apply_async(self.func_map['error'].error, (req,))
		return res.get()

	def warning(self, req):
		res = self.rpc_worker_pool.apply_async(self.func_map['warning'].warning, (req,))
		return res.get()

	def info(self, req):
		res = self.rpc_worker_pool.apply_async(self.func_map['info'].info, (req,))
		return res.get()

	def debug(self, req):
		res = self.rpc_worker_pool.apply_async(self.func_map['debug'].debug, (req,))
		return res.get()

	def opreport(self, req):
		res = self.rpc_worker_pool.apply_async(self.func_map['opreport'].opreport, (req,))
		return res.get()

	def opquery(self, req):
		res = self.rpc_worker_pool.apply_async(self.func_map['opquery'].opquery, (req,))
		return res.get()

	def webreport(self, req):
		res = self.rpc_worker_pool.apply_async(self.func_map['webreport'].webreport, (req,))
		return res.get()

	def busireport(self, req):
		res = self.rpc_worker_pool.apply_async(self.func_map['busireport'].busireport, (req,))
		return res.get()

