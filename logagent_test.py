#!/usr/bin/env python
#-*- coding: utf-8 -*-

import logagent_proto
import logagent_cli

def test_critical():
	cli = logagent_cli.Client('logagent_cli.conf', modulename='logagent_test')
	cli.critical('%s %d', 'test_critical', 123)

def test_error():
	cli = logagent_cli.Client('logagent_cli.conf', modulename='logagent_test')
	cli.error('%s %d', 'test_error', 234)

def test_warning():
	cli = logagent_cli.Client('logagent_cli.conf', modulename='logagent_test')
	cli.warning('%s %d', 'test_warning', 345)

def test_info():
	cli = logagent_cli.Client('logagent_cli.conf', modulename='logagent_test')
	cli.info('%s %d', 'test_info', 456)

def test_debug():
	cli = logagent_cli.Client('logagent_cli.conf', modulename='logagent_test')
	cli.debug('%s %d', 'test_debug', 567)

def main():
	test_critical()
	test_error()
	test_warning()
	test_info()
	test_debug()

if __name__ == '__main__':
	main()

