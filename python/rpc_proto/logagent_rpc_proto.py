#!/usr/bin/env python
#-*- coding: utf-8 -*-

class debugmsg(object):
	def __init__(self):
		self.value = ''

	def to_msgpack(self):
		return [
			self.value,
		]

	def from_msgpack(self, msg):
		self.value = msg[0]

class opmsg(object):
	def __init__(self):
		self.time = 0
		self.user = ''
		self.action = ''
		self.args = ''
		self.others = ''

	def to_msgpack(self):
		return [
			self.time,
			self.user,
			self.action,
			self.args,
			self.others,
		]

	def from_msgpack(self, msg):
		self.time = msg[0]
		self.user = msg[1]
		self.action = msg[2]
		self.args = msg[3]
		self.others = msg[4]

class webmsg(object):
	def __init__(self):
		self.time = 0
		self.clientip = ''
		self.url = ''
		self.status = 0
		self.runtime = 0

	def to_msgpack(self):
		return [
			self.time,
			self.clientip,
			self.url,
			self.status,
			self.runtime,
		]

	def from_msgpack(self, msg):
		self.time = msg[0]
		self.clientip = msg[1]
		self.url = msg[2]
		self.status = msg[3]
		self.runtime = msg[4]

class busimsg(object):
	def __init__(self):
		self.time = 0
		self.svrname = ''
		self.api = ''
		self.args = ''
		self.status = ''
		self.runtime = 0

	def to_msgpack(self):
		return [
			self.time,
			self.svrname,
			self.api,
			self.args,
			self.status,
			self.runtime,
		]

	def from_msgpack(self, msg):
		self.time = msg[0]
		self.svrname = msg[1]
		self.api = msg[2]
		self.args = msg[3]
		self.status = msg[4]
		self.runtime = msg[5]

