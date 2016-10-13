#!/usr/bin/env python
#-*- coding: utf-8 -*-

import logging
import logging.config

def init(args, conffile):
	logging.config.fileConfig(conffile)
	args['logger'] = logging.getLogger()
	pass
