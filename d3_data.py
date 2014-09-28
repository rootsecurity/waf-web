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
ws = create_connection("ws://127.0.0.1:8888/websocket")
# print "Sending 'Hello, World'..."
json_file = open("/Users/voilet/snort_dev/static/data/eventstream", "r")
json_data = json_file.readlines()
# for i in json_data:
#     s = json.loads(i)
#     s["latitude2"] = 35.86
#     s["longitude2"] = 104.1
#     print s
while True:
    for i in json_data:
        time.sleep(0.1)
        s = "%s" %(i)
        ws.send(s)
        result = ws.recv()
ws.close()