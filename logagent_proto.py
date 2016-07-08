#!/usr/bin/env python
#-*- coding: utf-8 -*-

import msgpack

class logmsg(object):
	def __init__(self):
		self.value = ''

	def to_msgpack(self):
		return msgpack.dumps({
			'value' : self.value,
			})

	def from_msgpack(self, msg):
		m = msgpack.loads(msg)
		self.value = m['value']

