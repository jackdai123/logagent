#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import importlib

class RPCTest:
	def __init__(self):
		rpc_test_name = os.path.splitext(os.path.basename(__file__))[0]
		service_name = rpc_test_name[:-9]
		self.rpc_proto = None
		self.cli = self._get_rpc_cli().Client(service=service_name, caller=rpc_test_name)

	def _get_rpc_cli(self):
		absolute_path = os.path.dirname(os.path.abspath(os.path.join(__file__, '..')))
		for python_path in os.getenv('PYTHONPATH').split(':'):
			if absolute_path.startswith(python_path):
				rootpath = os.path.relpath(absolute_path, python_path).replace(os.path.sep, '.')
				self.rpc_proto = importlib.import_module('.rpc_proto.logagent_rpc_proto', rootpath)
				return importlib.import_module('.rpc_cli', rootpath)
		else:
			raise IOError('%s is not in PYTHONPATH' % (__file__))

	def run(self):
		self.test_critical()
		self.test_error()
		self.test_warning()
		self.test_info()
		self.test_debug()
		self.test_opreport()
		self.test_webreport()
		self.test_busireport()

	def test_critical(self):
		ret = self.cli.critical('%s %s', 'test', 'critical')
		print 'critical ret %s' % (ret)

	def test_error(self):
		ret = self.cli.error('%s %s', 'test', 'error')
		print 'error ret %s' % (ret)

	def test_warning(self):
		ret = self.cli.warning('%s %s', 'test', 'warning')
		print 'warning ret %s' % (ret)

	def test_info(self):
		ret = self.cli.info('%s %s', 'test', 'info')
		print 'info ret %s' % (ret)

	def test_debug(self):
		ret = self.cli.debug('%s %s', 'test', 'debug')
		print 'debug ret %s' % (ret)

	def test_opreport(self):
		req = self.rpc_proto.opmsg()
		req.time = 1476344719
		req.user = 'david'
		req.action = 'Logout'
		ret = self.cli.opreport(req)
		print 'opreport ret %s' % (ret)

	def test_webreport(self):
		req = self.rpc_proto.webmsg()
		ret = self.cli.webreport(req)
		print 'webreport ret %s' % (ret)

	def test_busireport(self):
		req = self.rpc_proto.busimsg()
		ret = self.cli.busireport(req)
		print 'busireport ret %s' % (ret)

if __name__ == '__main__':
	RPCTest().run()

