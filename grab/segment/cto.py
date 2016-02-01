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
import MySQLdb
import datetime
import random
import os
from  tools import *
from  curl import *

title_urls = []
now = time.time()

for id in range(1,5):
   url = 'http://redking.blog.51cto.com/all/27212/5/page/%s' % id
   pool = urllib3.PoolManager()
   r = pool.request('GET', url, assert_same_host=False)
   title_url = re.findall("<span class=\"artList_tit\">.*?\/a>", r.data, re.S)
   title_urls.extend(title_url)

for i in title_urls:
    pre_url = re.findall(r'href=[\'"]?([^">]+)', i)
    title = re.findall(r'\d+">?([^"<]+)', i)
    if str(pre_url[0]).startswith('/'):
        url  = 'http://redking.blog.51cto.com' + pre_url[0]
    else:
        url = 'http://redking.blog.51cto.com/' + pre_url[0]
    print 'now start sprid the page'
    print str(url),title[0]
    u_conn = MySQLdb.connect("localhost","root","123456","test",charset="utf8",init_command="set names utf8")
    cursor = u_conn.cursor()
    s_sql = "select id from url where url=%s"
    id = cursor.execute(s_sql,str(url))
    if int(id) == 0:  
        u_sql = "insert into url (url, title) values  (%s,%s)"
        m_sql = "insert into img (title,imgvalue) values (%s,%s)"
        data = (str(url),title[0])
        cursor.execute(u_sql,data) 
        #u_conn.close()
        blog_url = str(url)
        c = initCurl()
        html = GetDate(c, blog_url)
        before = html.split('<div class="showContent">',1)[1]
        content = before.split('<!--正文 end-->',1)[0]
        ############################get the imgs ,replace the img url################################
        img=re.compile(r"""<img\s.*?\s?src\s*=\s*['|"]?([^\s'"]+).*?>""",re.I)
        img_urls = img.findall(content)
        img_urls = list(set(img_urls))

        for url in img_urls:
        ############################ there can use startswith() #####################################
                conv_lnk = ConvUrl('http://www.51cto.com/',url)
                conv_lnk = conv_lnk.replace("//","/")
                new_url = conv_lnk.replace("http:/","http://")
                new_img_url = GetImg(c,new_url)
                m_data = (title[0],new_img_url)
                cursor.execute(m_sql,m_data) 
                content = content.replace(new_url,new_img_url)
                content = content.replace(url,new_img_url)
                content = formatHtml(content)
        u_conn.close()

        content = herf_Img(content)
        r = re.compile(r'<pre><code.*?>(.+?)</code></pre>',re.S|re.I|re.M)
        content =  r.sub(r'<pre class="prettyprint linenums">\1</pre>', content)
        #content = content.replace("<pre class=\"prettyprint\">","<pre class=\"prettyprint linenums\">")
        title = title[0]

        curhost = 'localhost'##远程数据库服务器地址
        webuser = 'root'#数据库用户名
        webpwd ='123456'#数据库密码
        webdb = 'useso'#数据库名称

        dbconn = MySQLdb.connect(host=curhost, user=webuser, passwd=webpwd, db=webdb, port=3306, charset='utf8', init_command="set names utf8")
        flag = sync_wordpress(dbconn,title,content)
        if flag:
            print 'wordpress sync success'
        else:
            print 'wordpress sync error'
        else:
            print  url , 'have been spide'
    
#    time.sleep(5)
elapsed = time.time() - now
#print r.data , elapsed
print elapsed

