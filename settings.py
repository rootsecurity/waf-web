#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName:
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 2013-02-20 14:52:11
#      History:
#=============================================================================


import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


DB_CONNECT_STRING = 'mysql+mysqldb://root:@localhost/jm_waf?charset=utf8'
engine = create_engine(DB_CONNECT_STRING, echo=True)
DB_Session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
session = DB_Session()

#配置路由规则url
settings = {
    'debug':True,   #此为调试模式，正式环境必须关闭
    'static_path': os.path.join(os.path.dirname(__file__), "static"),
    'template_path': os.path.join(os.path.dirname(__file__), "templates"),
    "cookie_secret": "8i$2jaau-_w%yqwazz7xikka*^ekkvmn$4+25v8&amp;ngz+$&amp;qy#3",
    "login_url": "/login",
    # "xsrf_cookies": True,
}
