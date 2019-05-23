#!/usr/bin/env python
# coding=utf8
# ===============================================================================
#   Copyright (C) 2019 www.361way.com site All rights reserved.
#   Filename      ：urlencoded.py
#   Author        ：yangbk <itybku@139.com>
#   Description   ：
# ===============================================================================

import requests,json
 
url = 'http://httpbin.org/post'
data = {'key1':'value1','key2':'value2'}
r =requests.post(url,data)
print(r)
print('==========================')
print(r.text)
print('==========================')
print(r.content)
