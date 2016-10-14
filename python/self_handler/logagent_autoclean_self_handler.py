#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import time

class process:
	def __init__(self, worker_id, args):
		self.worker_id		= worker_id
		self.args			= args
		self.do()

	def do(self):
		interval = self.args['conf'].getint('autoclean', 'interval')

		while 1:
			self.args['oplog'].delete(0, int(time.time()) - interval)
			time.sleep(300)

