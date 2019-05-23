#!/usr/bin/env python
# coding=utf8
# ===============================================================================
#   Copyright (C) 2019 www.361way.com site All rights reserved.
#   Filename      ：multipart.py
#   Author        ：yangbk <itybku@139.com>
#   Description   ：
# ===============================================================================
import requests,json
 
url_mul = 'http://httpbin.org/post'
files = {'file':open('/tmp/test.txt','rb')}
r = requests.post(url_mul,files=files)
print(r)
print(r.text)
print(r.content)
