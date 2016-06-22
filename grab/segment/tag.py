#!/usr/bin/python
#coding=utf-8
import time
import urllib3
import re
import MySQLdb

def Title_Escape(s):
    s = s.replace('&quot;','"')
    s = s.replace('&amp;','&')
    s = s.replace('&lt;','<')
    s = s.replace('&gt;','>')
    s = s.replace('&nbsp;',' ')
    s = s.replace(' - SegmentFault','')
    return s

def  Gtag_ID(db,tags):
    #tag_list = []
    for tag in tags:
      cursor = db.cursor()
      id_qsql = "SELECT term_id FROM wp_terms where name=%s "
      count = cursor.execute(id_qsql,tag)
      if count == 0:
          try:
             sql = "INSERT into wp_terms (name,slug,term_group) values (%s,%s,0)"
             data = (tag,tag)
             cursor.execute(sql,data)
             db.commit()
             tag_id = cursor.lastrowid
             print 'Add the new tag %s ,tag_id is ' %(tag),tag_id
             tag_list.append(int(tag_id))

             taxonomy_sql = "INSERT into wp_term_taxonomy (term_id,taxonomy,description) values (%s,'post_tag','') " % (tag_id)
             cursor.execute(taxonomy_sql)
             db.commit()
             db.close()
          except:
             db.rollback()
             db.close()
      else:
          id = cursor.fetchall()
          for tag_id in range(count):
            print "%s have been in wp_terms ,tag_id is  " %(tag),int(id[tag_id][0])
            tag_list.append(int(id[tag_id][0]))
    return list(set(tag_list))


db = MySQLdb.connect("localhost","root","111111","test" )
url = "http://segmentfault.com/blog/wangbinke/1190000000351425"
now = time.time()
pool = urllib3.PoolManager()
r = pool.request('GET', url, assert_same_host=False)
tags = re.findall(r'data-original-title=[\'"](.*?)[\'"]',r.data)
print tags
#tags = ['php','java','91it']
tag_list = [100]
Gtag_ID(db,tags)
