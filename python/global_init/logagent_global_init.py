#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import logging
import logging.config
import importlib

def init(args):
	#init debug log
	logging.config.fileConfig(args['conffile'])
	args['debuglog'] = logging.getLogger()

	#init op log
	utils = None
	absolute_path = os.path.dirname(os.path.abspath(os.path.join(__file__, '..')))
	for python_path in os.getenv('PYTHONPATH').split(':'):
		if absolute_path.startswith(python_path):
			rootpath = os.path.relpath(absolute_path, python_path).replace(os.path.sep, '.')
			utils = importlib.import_module('.utils.logagent_utils', rootpath)
			break
	else:
		raise IOError('%s is not in PYTHONPATH' % (__file__))

	args['oplog'] = utils.OpLog(
		args['conf'].get('oplog', 'engine'),
		args['conf'].get('oplog', 'user'),
		args['conf'].get('oplog', 'pass'),
		args['conf'].get('oplog', 'ip'),
		args['conf'].get('oplog', 'port'),
		args['conf'].get('oplog', 'db')
	)

	pass
