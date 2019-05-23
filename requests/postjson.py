#!/usr/bin/env python
# coding=utf8
# ===============================================================================
#   Copyright (C) 2019 www.361way.com site All rights reserved.
#   Filename      ：json.py
#   Author        ：yangbk <itybku@139.com>
#   Description   ：
# ===============================================================================
import requests,json
 
url_json = 'http://httpbin.org/post'

#dumps：将python对象解码为json数据    
data_json = json.dumps({'key1':'value1','key2':'value2'}) 
r_json = requests.post(url_json,data_json)
print(r_json)
print(r_json.text)
print(r_json.content)
