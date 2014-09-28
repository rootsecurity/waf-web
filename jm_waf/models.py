# !/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName: models.py
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 2014-08-28
#      History: 
#=============================================================================
from sqlalchemy import Column
from sqlalchemy.types import CHAR, Integer, String, TEXT, DATETIME, DateTime
from sqlalchemy.ext.declarative import declarative_base
from settings import engine


BaseModel = declarative_base()

def init_db():
    BaseModel.metadata.create_all(engine)

def drop_db():
    BaseModel.metadata.drop_all(engine)


class Hack(BaseModel):
    __tablename__ = 'jm_hacker'

    id = Column(Integer, primary_key=True)
    ip = Column(CHAR(60))
    hack_city = Column(CHAR(40))
    hack_addr = Column(CHAR(40))
    url = Column(TEXT())
    host = Column(CHAR(80))
    acl = Column(TEXT(80))
    src_time = Column(DATETIME(20))
    method = Column(CHAR(10))
    headers = Column(TEXT(200))
    user_agent = Column(TEXT(80))
    cookie = Column(TEXT(80))
    post_data = Column(TEXT())

if __name__ == "__main__":
    init_db()