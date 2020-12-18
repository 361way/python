#!/usr/bin/env python
# coding=utf-8
# code from www.361way.com
from gevent import monkey
monkey.patch_all()
 
import urllib2
from gevent.pool import Pool

def geturls():
    urls = []
    for v in range(0,1000,10):
        url = 'http://www.baidu.com/s?wd=site%3A361way.com&pn=' + str(v)
        urls.append(url)
    return urls
def download(url):
    return urllib2.urlopen(url).read()
 
if __name__ == '__main__':
    urls = geturls()
    pool = Pool(20)
    print pool.map(download, urls)
