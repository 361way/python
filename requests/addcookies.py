#!/usr/bin/env python
# coding=utf8
# ===============================================================================
#   Copyright (C) 2019 www.361way.com site All rights reserved.
#   
#   Filename      ：addcookies.py
#   Author        ：yangbk <itybku@139.com>
#   Description   ：
# ===============================================================================
# 方式1
import requests
url = 'http://200.200.0.7/Java/jviewer.jnlp?EXTRNIP=200.200.0.7&JNLPSTR=JViewer'
cookies = '''SessionCookie=shfLO755DJlWGV4AkCjSb4jnkBHPXe3J005; Language=ZH; Username=admin;'''
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Geck
    o) Chrome/53.0.2785.143 Safari/537.36',
    'Connection': 'keep-alive',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cookie': cookies
           }
r = requests.get(url,headers=header)
print(r.text)

#===================================#
#             方式2                 #
#===================================#
import requests
url = 'http://200.200.0.7/Java/jviewer.jnlp?EXTRNIP=200.200.0.7&JNLPSTR=JViewer'
cookie = '''SessionCookie=shfLO755DJlWGV4AkCjSb4jnkBHPXe3J005; Language=ZH; Username=admin;'''
r = requests.get(url,cookies=cookie)
print(r.text)

