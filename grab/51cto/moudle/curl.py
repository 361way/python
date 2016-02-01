#!/usr/bin/python
#coding=utf-8
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
import time
import urllib3
import re
import string
import pycurl
import StringIO
import urllib2
import MySQLdb
import datetime
import random
import os
from  tools import *

def formatHtml(input):
    regular = re.compile('<\\bp\\b[^>]*>',re.IGNORECASE)
    input = regular.sub('<p>',input)

#    regular = re.compile('</?SPAN[^>]*>',re.IGNORECASE)
#    input = regular.sub('',input)

    regular = re.compile('</?o:p>',re.IGNORECASE)
    input = regular.sub('',input)

    regular = re.compile('</?FONT[^>]*>',re.IGNORECASE)
    input = regular.sub('',input)

    regular = re.compile('</?\\bB\\b[^>]*>',re.IGNORECASE)
    input = regular.sub('',input)

#    regular = re.compile('<\?[^>]*>',re.IGNORECASE)
#    input = regular.sub('',input)

    regular = re.compile('</?st1:[^>]*>',re.IGNORECASE)
    input = regular.sub('',input)

    regular = re.compile('</?\\bchsdate\\b[^>]*>',re.IGNORECASE)
    input = regular.sub('',input)

    regular = re.compile('<\\bbr\\b[^>]*>',re.IGNORECASE)
    input = regular.sub('<br>',input)

    regular = re.compile('</?DIV[^>]*>',re.IGNORECASE)
    input = regular.sub('<br>',input)

    regular = re.compile('(<br>)+',re.IGNORECASE)
    input = regular.sub('<br>',input)

    regular = re.compile('</?\\bchmetcnv\\b[^>]*>',re.IGNORECASE)
    input = regular.sub('',input)

    regular = re.compile('<script[^>]*?>.*?</script>',re.IGNORECASE+re.DOTALL)
    input = regular.sub('',input)
    return input

def initCurl():
        c = pycurl.Curl()
        c.setopt(pycurl.COOKIEFILE, "cookie_file_name")#把cookie保存在该文件中
        c.setopt(pycurl.COOKIEJAR, "cookie_file_name")
        c.setopt(pycurl.FOLLOWLOCATION, 1) #允许跟踪来源
        c.setopt(pycurl.MAXREDIRS, 5)
        c.setopt(pycurl.CONNECTTIMEOUT, 8)
        c.setopt(pycurl.REFERER, "http://blog.51cto.com")
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


def ConvUrl(url_suff,url):
        m = re.match('http://',url.lower())
        if m is not None:
             return url
        else:
             return url_suff + url

def herf_Img(text):
	str=''
	text=text.replace('</a>','</a>|||')
	for href_img in text.split('|||'):
	    r = re.compile(r'<a.*?img1.51cto.com.*?><img(.+?)src="(.*?)</a>')
	    #x = r.sub(r'<img\1src=\2', text)
	    x = r.sub(r'<img src="\2', text)
            x = x.replace('|||','')
	    str += x
	return str


def GetImg(curl, url):
######################### set the img suffix ##################################
        img_suff = url.split(".")[-1].lower()
        if img_suff not in ['jpeg','png','jpg','gif','bmp']:
            img_suff = 'png'

        imgdata = GetDate(curl, url)
########################### create img  filename ###############################
        filename = time.strftime("%Y%m%d_%H%M%S") + str(random.randint(10, 99))
########################### create the path for save the img ###################
        dir = '/data/img/' + time.strftime("%Y/%m")
        if not os.path.exists(dir):
           os.makedirs(dir)
        f = open("%s/%s" % (dir,filename + '.' + img_suff), 'wb')
        f.write(imgdata)
        f.close()
	new_img_url = 'http://img.91it.org/' + time.strftime("%Y/%m/") + filename + '.' + img_suff
        #print time.strftime("%Y/%m/") + filename + '.' + img_suff
        return new_img_url



def wp_checktitle(dbconn,title):
    '''wordpress检测是否有重复标题'''

    cursor=dbconn.cursor()

    sql = "select post_title from wp_posts where post_title='%s'" % (title)
    cursor.execute(sql)

    if cursor.rowcount == 0:
        checkflag = 1
    else:
        checkflag = 0

    return checkflag



def  sync_wordpress(dbconn,title,content):
    '''同步wordpress程序'''
    
    checkflag = wp_checktitle(dbconn,title)
    cursor=dbconn.cursor()
    
    curtime = str(datetime.datetime.now())[:19]
    
    post_author = 1
    post_date = curtime
    post_date_gmt = curtime
    #post_content = '"""%s"""' % (content)
    post_content = content
    post_title = title
    post_name = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    post_modified = curtime
    post_modified_gmt = curtime
    post_content_filtered = ''
    currenttime = int(time.time())
    value = (post_author,post_date,post_date_gmt,post_content,post_title,post_name,post_modified,post_modified_gmt,post_content_filtered)


    if checkflag:
       try:
           postsql = ''
           postsql = '''INSERT INTO `wp_posts` ( 
                  `post_author` , 
                  `post_date` ,  
                  `post_date_gmt` , 
                  `post_content` , 
                  `post_title` ,
                  `post_name` , 
                  `post_modified`, 
                  `post_modified_gmt`, 
                  `post_content_filtered` 
                  ) 
                  VALUES ( 
                   %s,%s,%s,%s,%s,%s,%s,%s,%s)'''
           

           cursor.execute(postsql,value)
           dbconn.commit()
           
           rowid = cursor.lastrowid
               
           metasql = ''
           metasql = "insert into `wp_postmeta`(`post_id`)VALUES(%s)" % (rowid)
           cursor.execute(metasql)
           dbconn.commit()
           
           # category = python , tag = djanjo
           category_tag_data = [
#                       (rowid,38),
                       (rowid,3)]
           insertsql = '''INSERT INTO `wp_term_relationships` (
           `object_id` ,
           `term_taxonomy_id` 
           )
           VALUES (
           %s, %s) '''
           #%(object_id)s, %(term_taxonomy_id)s) ''' % {'object_id':rowid,'term_taxonomy_id':1}

           cursor.executemany(insertsql,category_tag_data)
           dbconn.commit()

           return 1

       except Exception, e:
            print '数据库错误:', e
            return 0

       finally:
            cursor.close()

            dbconn.close()
    else:
        print 'wordpress title exist'
        return 1



