#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName: urls.py
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 2014 14-2-23 上午12:40
#      History: 
#=============================================================================

import tornado.web
from index import MainHeandler, LoginHandler, WeiboHandler, RegisterHandler, Waf_upload, ChatSocketHandler, Atk_Handler
from settings import settings

application = tornado.web.Application([
    (r"/", MainHeandler),
    (r"/atk", Atk_Handler),
    (r"/login", LoginHandler),
    (r"/weibo/add", WeiboHandler),
    (r"/register", RegisterHandler),
    (r"/api/waf", Waf_upload),
    (r"/websocket", ChatSocketHandler),
], **settings)