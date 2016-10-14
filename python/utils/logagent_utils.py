#!/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, VARCHAR, Text, TIMESTAMP, func, Column, MetaData, Table

Base = declarative_base()
OPLOG_TABLENAME = 'oplog'

class OpLogData(Base):
	__tablename__ = OPLOG_TABLENAME

	id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
	time = Column(TIMESTAMP, default=func.current_timestamp(), nullable=False, index=True)
	user = Column(VARCHAR(32), nullable=False, index=True)
	action = Column(Text, nullable=False)
	args = Column(Text, nullable=True)
	others = Column(Text, nullable=True)

	def __init__(self, time, user, action, args = None, others = None):
		self.time = datetime.datetime.fromtimestamp(time)
		self.user = user
		self.action = action
		self.args = args
		self.others = others

class OpLog(object):
	def __init__(self, engine, user, password, ip, port, db):
		self.engine = create_engine(
			engine + '://' + user + ':' + password + '@' + ip + ':' + port + '/' + db
		)
		self.create_table()

	def create_table(self):
		Table(
			OPLOG_TABLENAME,
			MetaData(bind = self.engine),
			Column('id', Integer, autoincrement=True, nullable=False, primary_key=True),
			Column('time', TIMESTAMP, default=func.current_timestamp(), nullable=False, index=True),
			Column('user', VARCHAR(32), nullable=False, index=True),
			Column('action', Text, nullable=False),
			Column('args', Text, nullable=True),
			Column('others', Text, nullable=True),
			mysql_engine = 'InnoDB',
			mysql_charset = 'utf8',
		).create(checkfirst = True)

	def _get_session(self):
		return sessionmaker(self.engine)()

	def insert(self, req):
		session = self._get_session()
		session.add(OpLogData(req.time, req.user, req.action, req.args, req.others))
		session.commit()
		session.close()

	def multi_insert(self, req_list):
		session = self._get_session()
		oplogdata_list = []
		for req in req_list:
			oplogdata_list.append(OpLogData(req.time, req.user, req.action, req.args, req.others))
		session.add_all(oplogdata_list)
		session.commit()
		session.close()

	def delete(self, begintime, endtime):
		session = self._get_session()
		session.query(OpLogData).filter(
				OpLogData.time >= datetime.datetime.fromtimestamp(begintime), 
				OpLogData.time <= datetime.datetime.fromtimestamp(endtime)).delete(synchronize_session=False)
		try:
			session.commit()
		except Exception as e:
			session.rollback()
		session.close()

	def query(self, req):
		session = self._get_session()
		total_data = session.query(OpLogData).filter(
				OpLogData.user == req.user, 
				OpLogData.time >= datetime.datetime.fromtimestamp(req.begintime), 
				OpLogData.time <= datetime.datetime.fromtimestamp(req.endtime)).order_by(OpLogData.time.desc()).all()
		session.close()
		return total_data

