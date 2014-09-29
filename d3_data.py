# !/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName: d3_data.py
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 2014-09-28
#      History: 
#=============================================================================

import websocket
import time
import json
from websocket import create_connection
from settings import engine, DB_Session
from jm_waf.models import Hack

import pygeoip
gi = pygeoip.GeoIP('GeoLiteCity.dat', pygeoip.MEMORY_CACHE)

test = DB_Session.query(Hack).all()
ws = create_connection("ws://127.0.0.1:8888/websocket")
for i in test:
    # print i.ip
    atk_data = {'city': 'Changsha', 'dport': '80', 'countrycode': 'CN', 'country': 'CN', 'latitude2': 35.86,
                'longitude2': 104.1, 'longitude': '10.08', 'svc': 'http', 'country2': 'US', 'city2': 'Miami',
                'countrycode2': 'US', 'latitude': '34.63', 'org': 'http hacker', 'zerg': '', 'type': 'web atk',
                'md5': ''}
    rst = gi.record_by_addr(i.ip)
    time.sleep(0.1)
    try:
        # atk_data["city"] = rst.get("city", None)
        # atk_data["countrycode"] = rst["country_code"]
        # atk_data["country"] = rst["country_code3"]
        # atk_data["country2"] = "CN"
        # atk_data["countrycode2"] = "CN"
        # atk_data["city2"] = "Beijing"
        # atk_data["md5"] = i.ip
        # atk_data["latitude"] = rst["latitude"]
        # atk_data["longitude"] = rst["longitude"]
        # print atk_data
        s = {'city': str(rst["city"]), 'countrycode': 'MO', 'latitude': rst["latitude"], 'country': 'MAC', 'latitude2': 35.86, 'longitude2': 104.1, 'longitude': rst["longitude"], 'svc': 'http', 'country2': 'CN', 'city2': 'Beijing', 'org': 'Hurricane Electric', 'dport': '80', 'countrycode2': 'CN', 'zerg': '', 'type': 'ipviking.honey', 'md5': str(i.ip)}
        print s
        s = "%s" %(s)
        ws.send(s)
        result = ws.recv()
    except Exception, e:
        pass
ws.close()




# json_file = open("./static/data/eventstream", "r")
# atk_data = {'city': 'Changsha', 'dport': '80', 'countrycode': 'CN', 'country': 'CN', 'latitude2': 35.86, 'longitude2': 104.1, 'longitude': '10.08', 'svc': 'http', 'country2': 'US', 'city2': 'Miami', 'countrycode2': 'US', 'latitude': '34.63', 'org': 'http hacker', 'zerg': '', 'type': 'ipviking.honey', 'md5': '210.78.137.6'}
# json_data = json_file.readlines()
# # for i in json_data:
# #     s = json.loads(i)
# #     s["latitude2"] = 35.86
# #     s["longitude2"] = 104.1
# #     print s
# while True:
#     for i in json_data:
#         time.sleep(0.1)
#         s = "%s" %(i)
#         print s
#         print type(s)
#         ws.send(s)
#         result = ws.recv()
# ws.close()