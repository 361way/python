#!/usr/bin/python
# encoding: utf-8
# site: www.361way.com   
# mail: itybku@139.com
# desc: get the rpm package from yum site 

import pycurl
import StringIO
import urllib
import urllib2
import re
import time
import random
import os


def initCurl():
        c = pycurl.Curl()
        c.setopt(pycurl.COOKIEFILE, "cookie_file_name")#把cookie保存在该文件中
        c.setopt(pycurl.COOKIEJAR, "cookie_file_name")
        c.setopt(pycurl.FOLLOWLOCATION, 1) #允许跟踪来源
        c.setopt(pycurl.MAXREDIRS, 5)
        #设置代理 如果有需要请去掉注释，并设置合适的参数
        #c.setopt(pycurl.PROXY, ‘http://11.11.11.11:8080′)
        #c.setopt(pycurl.PROXYUSERPWD, ‘aaa:aaa’)
        return c



def GetDate(curl, url):
        head = ['Accept:*/*',
                'User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0']
        buf = StringIO.StringIO()
        curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        curl.setopt(pycurl.URL, url)
        curl.setopt(pycurl.HTTPHEADER,  head)
        curl.perform()
        the_page =buf.getvalue()
        buf.close()
        return the_page


def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print '%.2f%%' % per

c = initCurl()
html = GetDate(c, 'http://repo.saltstack.com/yum/rhel6/')
#print type(html)
#print html

rpmpack = re.compile(r'href="(.*?).rpm',re.I)
rpmpack_url = rpmpack.findall(html)
#print rpmpack_url

for rpm in rpmpack_url:
    rpm_url = 'http://repo.saltstack.com/yum/rhel6/' + rpm + '.rpm'
    print rpm_url
    #urllib.urlretrieve(rpm_url, rpm + '.rpm',Schedule) 回调Schedule函数，显示进度
    try:  
        urllib.urlretrieve(rpm_url, rpm + '.rpm')
    except Exception,e:
        continue
