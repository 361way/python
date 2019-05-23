#!/usr/bin/env python
# coding=utf8
# ===============================================================================
#   Copyright (C) 2019 www.361way.com site All rights reserved.
#   
#   Filename      ：headers.py
#   Author        ：yangbk <itybku@139.com>
#   Create Time   ：2019-05-23 11:43
#   Description   ：
# ===============================================================================
import requests
r = requests.head('http://httpbin.org/get')
print(r.headers)
