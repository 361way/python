#!/usr/bin/python
#coding=utf-8
#import sys,os
import time
import urllib3
import re

#url = "http://www.361way.com/python-mysqldb/3842.html"
#url = "http://segmentfault.com/blog/wangbinke/1190000000351425"
url = "http://segmentfault.com/t/php/blogs?page=25"
now = time.time()
pool = urllib3.PoolManager()
r = pool.request('GET', url, assert_same_host=False)
#title = re.findall("<li><a\w+href=\w+title",r.data)
#regex url 
#urls = urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', r.data)
#or use this one
#urls = re.findall(r'href=[\'"]?([^\'" >]+)', r.data)
#urls = re.findall(r'href=[\'"]?([^">]+)', r.data)
title_urls = re.findall(r'<li><a href=[\'"].*?target="_blank"',r.data)
for i in title_urls:
    url = re.findall(r'href=[\'"]?([^">]+)', i)
#    title = re.findall(r'title=[\'"].*?\"',i)
#    title = re.findall(r'title=".*?"',i)
    title = re.findall(r'title=[\'"]?([^">]+)"',i)

    print str(url[0]),title[0]
    
#print title_urls[0]
#print urls[169]
elapsed = time.time() - now
#print r.data , elapsed
print elapsed
