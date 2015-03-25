#!/usr/bin/python
# encoding: utf-8
import pycurl
import StringIO
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


def PostData(curl, url, data):
        head = ['Accept:*/*',
                'Content-Type:application/xml',
                'render:json',
                'clientType:json',
                'Accept-Charset:GBK,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding:gzip,deflate,sdch',
                'Accept-Language:zh-CN,zh;q=0.8',
                'User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0']
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

#def GetImg(curl, url, path ,filename):
def GetImg(curl, url):
######################### set the img suffix ##################################
	img_suff = url.split(".")[-1].lower()
	if img_suff not in ['jpeg','png','jpg','gif','bmp']:
	    img_suff = 'png'

        imgdata = GetDate(curl, url)
########################### create img  filename ###############################
	filename = time.strftime("%Y%m%d_%H%M%S") + str(random.randint(10, 99))
########################### create the path for save the img ###################
        dir = time.strftime("%Y/%m")
	if not os.path.exists(dir):
   	   os.makedirs(dir)
        f = open("%s/%s" % (dir,filename + '.' + img_suff), 'wb')
	f.write(imgdata)
	f.close()

c = initCurl()
html = GetDate(c, 'www.cnblogs.com/chenkun24/archive/2012/10/06/2713348.html')
before = html.split('<div id="topics">',1)[1]
content = before.split('<div id="post_next_prev">',1)[0]
#print "'''%s'''" %(content)
#print '"""%s"""' %(content)
img=re.compile(r"""<img\s.*?\s?src\s*=\s*['|"]?([^\s'"]+).*?>""",re.I)  
img_url = img.findall(content)  
print "\n".join(img_url)


############################### download img use urllib2 ###########################
#img = urllib2.urlopen(m[0],timeout=3)
#localFile = open('desktop.jpg', 'wb')
#localFile.write(img.read())
#localFile.close()
################################ downlaod img use def Getdate ######################
#img = GetDate(c,m[0])
#f = open("./%s" % ("img",), 'wb')
#f.write(img)
#f.close()

#GetImg(c,img_url[0])
GetImg(c,'http://pic002.cnblogs.com/images/2012/450597/2012100622313798.JPG')
