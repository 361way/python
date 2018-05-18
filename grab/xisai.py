#!/usr/bin/python
# encoding: utf-8
# desc: 采集希赛网历年考题，通过抓手机APP访问包里的cookice字段信息，返回json数据，处理后保存为网页
# code from www.361way.com <itybku@139.com>

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import pycurl
import StringIO
import zlib
import json

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

def PostData(curl, url, data):
        head = ['Accept:*/*',
                'Accept-Encoding:gzip,deflate',
                'Accept-Language: zh-Hans-CN;q=1',
                'User-Agent: CsaiApp/2.0 (iPhone; iOS 11.3.1; Scale/3.00)']
        buf = StringIO.StringIO()
        curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        curl.setopt(pycurl.POSTFIELDS,  data)
        curl.setopt(pycurl.URL, url)
        curl.setopt(pycurl.HTTPHEADER,  head)
        curl.perform()
        the_page = buf.getvalue()
        #print the_page
        buf.close()
        return the_page

def writeinfo(cookie , filename):
    
    c = initCurl()
    html = PostData(c, 'http://app.educity.cn/tiku/tiku_paper_test.ashx',cookie)
    
    html = zlib.decompress(html, 16+zlib.MAX_WBITS)
    #print html
    
    hjson = json.loads(html)
    #print  hjson['data']['stlist'][53]
    slist = hjson['data']['stlist']
    
    for num in range(0,len(slist)):
        data = slist[num]
        wdata = '<b>' + data['btitle'] + data['sort'] + '</b><br/>' + data['item_text'] + '<br/>' + data['ask_text'] + '-'*10 + '<br/>' + '<b><font color="red">答案：' + data['answer'] + '</font></b><br/>' + data['analyze'] + '<br/><br/>' 
        #filename = "201405_wenda.html"
        with open(filename,'a') as f: 
            f.write(wdata)

cookie = 'CheckVersions=2.0&GlobalAppType=1&gradeID=9&'
filename = '201511-afternoon.html'
writeinfo(cookie,filename)
