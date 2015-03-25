#!/usr/bin/python
#coding=utf-8
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
import time
import urllib3
import re
import string
import StringIO
import urllib2
import datetime
import random
import os
#from  tools import *
from  curl import *
#from iconv import iconv

title_urls = []
now = time.time()
'''
for id in range(1,2):
   url = 'http://redking.blog.51cto.com/all/27212/5/page/%s' % id
   pool = urllib3.PoolManager()
   r = pool.request('GET', url, assert_same_host=False)
   title_url = re.findall("<span class=\"artList_tit\">.*?\/a>", r.data, re.S)
   title_urls.extend(title_url)
'''
#title_urls = list(set(title_urls))
title_urls = ['<a href="/27212/120373">RHCE课程-RH131Linux管理笔记四-Linux的计划任务</a>']



for i in title_urls:
    pre_url = re.findall(r'href=[\'"]?([^">]+)', i)
    title = re.findall(r'\d+">?([^"<]+)', i)
    if str(pre_url[0]).startswith('/'):
        url  = 'http://redking.blog.51cto.com' + pre_url[0]
    else:
        url = 'http://redking.blog.51cto.com/' + pre_url[0]
    print 'now start sprid the page'
    print str(url),title[0].decode('gb2312','ignore').encode('utf-8', 'ignore')
    blog_url = str(url)
    c = initCurl()
    html = GetDate(c, blog_url)
    html = html.decode('gb2312','ignore').encode('utf-8', 'ignore')
    #before = html.split('<div class="showContent">',1)[1]
    before = html.split('<!--正文 begin-->',1)[1]
    content = before.split('<!--正文 end-->',1)[0]
############################get the imgs ,replace the img url################################
    img=re.compile(r"""<img\s.*?\s?src\s*=\s*['|"]?([^\s'"]+).*?>""",re.I)
    img_urls = img.findall(content)
    img_urls = list(set(img_urls))
    content = formatHtml(content)
    content = herf_Img(content)
    print content
