#!/usr/bin/env python
#-*- coding: utf-8 -*-

import logagent_proto
import logagent_cli

def test_critical():
	cli = logagent_cli.Client('logagent_cli.conf')
	msg = logagent_proto.logmsg()
	msg.value = 'test_critical'
	cli.critical(msg,)

def test_error():
	cli = logagent_cli.Client('logagent_cli.conf')
	msg = logagent_proto.logmsg()
	msg.value = 'test_error'
	cli.error(msg,)

def test_warning():
	cli = logagent_cli.Client('logagent_cli.conf')
	msg = logagent_proto.logmsg()
	msg.value = 'test_warning'
	cli.warning(msg,)

def test_info():
	cli = logagent_cli.Client('logagent_cli.conf')
	msg = logagent_proto.logmsg()
	msg.value = 'test_info'
	cli.info(msg,)

def test_debug():
	cli = logagent_cli.Client('logagent_cli.conf')
	msg = logagent_proto.logmsg()
	msg.value = 'test_debug'
	cli.debug(msg,)

def main():
	test_critical()
	test_error()
	test_warning()
	test_info()
	test_debug()

if __name__ == '__main__':
	main()

