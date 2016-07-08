#!/usr/bin/env python
#-*- coding: utf-8 -*-

import logagent_proto

#@param msg : logmsg
#@return : no
def critical(logger, msg,):
	logger.critical(msg.value)

#@param msg : logmsg
#@return : no
def error(logger, msg,):
	logger.error(msg.value)

#@param msg : logmsg
#@return : no
def warning(logger, msg,):
	logger.warning(msg.value)

#@param msg : logmsg
#@return : no
def info(logger, msg,):
	logger.info(msg.value)

#@param msg : logmsg
#@return : no
def debug(logger, msg,):
	logger.debug(msg.value)

