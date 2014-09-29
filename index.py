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
import tornado.ioloop
import tornado.web

from urls import *
import re

import requests
import tornado.websocket

# import api.QQWry
from api.QQWry import *

#初始化ip库
tt = IPSearch('api/QQWry.Dat')


from settings import engine, DB_Session
from jm_waf.models import Hack



def get_tags(content):
    r = re.compile(ur"@([\u4E00-\u9FA5\w-]+)")
    return r.findall(content)

class BaseHandle(tornado.web.RequestHandler):
    def initialize(self):
        self.session = DB_Session

    def on_finish(self):
        self.session.close()

    def get_current_user(self):
        return self.get_secure_cookie("user")

class WeiboHandler(BaseHandle):
    """发送微博模块"""
    @tornado.web.authenticated
    def get(self):
        """请求发送页面"""
        self.render("weibo_add.html")

    @tornado.web.authenticated
    def post(self):
        """接收发送数据并入库"""
        result = self.get_argument("content",None)

        # db.weibo.insert({"content": result, "user": self.get_current_user()})
        self.write(result)


# class MainHeandler(tornado.web.RequestHandler):
class MainHeandler(BaseHandle):
    # @tornado.web.authenticated
    def get(self):
        """
        首页渲染数据
        """
        # name = tornado.escape.xhtml_escape(self.current_user)   #读取session，验证是否登录

        # test = self.session.query(Hack).all()
        # print test.id

        iterm = []
        # self.render("weibo_list.html", content=iterm)
        self.render("waf.html", content=iterm)
        # for i in test:
        #     # print i.ip
        #     s = "https://www.maxmind.com/geoip/v2.1/city/%s?demo=1" %(i.ip)
        #     rst = requests.get(s)
        #     print rst.json()

    def post(self):
        self.write("hello post\n")

    def put(self):
        self.write("hello put\n")

    def delete(self):
        self.write("hello delete\n")

class LoginHandler(BaseHandle):
    def get(self):
        self.render("login.html")


    def post(self):
        user_name = self.get_argument("account")
        print user_name
        # print db.user.find_one({"account": user_name})["account"]
        # if db.user.find({"account": user_name}):
        #     self.set_secure_cookie("user", self.get_argument("account"))
        #     self.redirect("/")
        # else:
        #     self.write("无此帐号，请注册")
        self.write("无此帐号，请注册")

class RegisterHandler(BaseHandle):
    """注册方法"""
    def get(self):
        self.render("register.html")

    def post(self):
        """验证提交是否为空，验证帐号是否存在"""
        user_name = self.get_argument("account")
        password = self.get_argument("password")
        if not user_name or not password:
            return self.write("帐号或密码未填写")

        # print db.user.count({"account": user_name})
        # if db.user.find({"account": user_name}).count() > 0:
        #     return self.write("亲，已经注册了")
        # db.user.insert({"account": user_name, "password": password})
        self.set_secure_cookie("user", self.get_argument("account"))


class Waf_upload(BaseHandle):
    """
    入侵上报日志
    """

    def get(self):
        self.write({"status": 403, "message": "Permission denied"})

    def post(self):
        try:
            data = {
                "url": self.get_argument("att_url"),
                "acl": self.get_argument("attacker_acl"),
                "attacker_ip": self.get_argument("attacker_ip"),
                "attacker_time":  self.get_argument("attacker_time"),
                "server_domain": self.get_argument("server_domain"),
            }
            city_data = tt.find("222.91.163.114")
            print unicode(city_data[0], 'gb2312').encode('utf-8')
            print unicode(city_data[1], 'gb2312').encode('utf-8')
            self.write(data)
        except:
            self.write({"status": 400, "message": "Missing argument"})

class ChatSocketHandler(tornado.websocket.WebSocketHandler):

    connects = set()

    def open(self):
        print "socket opened"
        ChatSocketHandler.connects.add(self)

    def on_message(self, message):
        ChatSocketHandler.send_all(message)

    def on_close(self):
        print "socketed closed"

    @classmethod
    def send_all(cls, chat):
        for connect in cls.connects:
            try:
                connect.write_message(chat)
            except:
                pass


class Atk_Handler(BaseHandle):
    # @tornado.web.authenticated
    def get(self):
        """
        首页渲染数据
        """
        self.render("d3.html")

if __name__ == "__main__":
    #监听端口
    application.listen(8888)
    tornado.ioloop.PollIOLoop.instance().start()
    tornado.ioloop.IOLoop.instance().start()