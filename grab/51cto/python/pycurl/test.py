#!/usr/bin/python
# encoding: utf-8
import pycurl
import StringIO
import MySQLdb
import datetime
import time
from  tools import *


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
    post_content = content
    post_title = title
    post_name = post_title
    post_modified = curtime
    post_modified_gmt = curtime
    post_content_filtered = ''
    currenttime = int(time.time())
    

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
                   '%(post_author)s','%(post_date)s','%(post_date_gmt)s','%(post_content)s','%(post_title)s','%(post_name)s','%(post_modified)s','%(post_modified_gmt)s','%(post_content_filtered)s')''' % {'post_author':post_author,'post_date':post_date,'post_date_gmt':post_date_gmt,'post_content':post_content,'post_title':post_title,'post_name':post_name,'post_modified':post_modified,'post_modified_gmt':post_modified_gmt,'post_content_filtered':post_content_filtered}
           

           cursor.execute(postsql)
           dbconn.commit()
           
           rowid = cursor.lastrowid
               
           metasql = ''
           metasql = "insert into `wp_postmeta`(`post_id`)VALUES(%s)" % (rowid)
           cursor.execute(metasql)
           dbconn.commit()

           insertsql = '''INSERT INTO `wp_term_relationships` (
           `object_id` ,
           `term_taxonomy_id` 
           )
           VALUES (
           %(object_id)s, %(term_taxonomy_id)s) ''' % {'object_id':rowid,'term_taxonomy_id':1}
           
           cursor.execute(insertsql)
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



c = initCurl()
html = GetDate(c, 'http://blog.linuxeye.com/400.html')
before = html.split('<!-- Widgets: Before Post Content -->',1)[1]
content = before.split('<!-- Widgets: After Post Content -->',1)[0]
#print content




title = 'splace-titl-wptitle-qq'
zcontent = content

curhost = 'localhost'##远程数据库服务器地址
webuser = 'root'#数据库用户名
webpwd ='tsy10060'#数据库密码
webdb = 'blog'#数据库名称

dbconn = MySQLdb.connect(host=curhost, user=webuser, passwd=webpwd, db=webdb, port=3306, charset='utf8')
     
flag = sync_wordpress(dbconn,title,zcontent)

if flag:
    print 'wordpress sync success'
else:
    print 'wordpress sync error'

