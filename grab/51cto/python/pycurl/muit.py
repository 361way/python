#coding=utf-8

import threading
from cStringIO import StringIO
import pycurl
"""
Asyn open url
Author:zsp007@gmail.com
2008-1-25 17:14
"""
from Queue import Queue,Empty

class UrlOpen(threading.Thread):
   """异步下载网页"""

   def __init__(self):
       super(UrlOpen, self).__init__()
       self.opener = pycurl.CurlMulti()
       self.handle_list = []
       self.waiting = Queue(2048)

   def add(self, url, recall, catch=None, writer=StringIO):
       """
       参数:网址,回调函数,存放临时数据的对象
       """
       if catch is None:
           def catch(curl, error_no, desp):
               print "Url:%s\nError:%s - %s"%(curl.url, error_no, desp)

       c = pycurl.Curl()

       #可以传给回调函数
       c.url = url
       c.content = writer()
       c.recall = recall
       c.catch = catch
       c.setopt(c.URL,
           url.encode('utf-8') if type(url) is unicode else url
       )
       c.setopt(c.WRITEFUNCTION, c.content.write)
       c.setopt(pycurl.CONNECTTIMEOUT, 30)
       c.setopt(pycurl.MAXREDIRS, 3)
       c.setopt(pycurl.TIMEOUT, 300)
       c.setopt(pycurl.FOLLOWLOCATION, 1)

       self.waiting.put(c)

   def _add(self,c):
       self.handle_list.append(c)
       self.opener.add_handle(c)

   def _pull(self):
       while True:
           try:
               self._add(self.waiting.get_nowait())
           except Empty:
               break

   def _remove(self, c):
       c.close()
       self.opener.remove_handle(c)
       self.handle_list.remove(c)
       del c

   def run(self):
       import select
       import time
       num_handle = 0
       while 1:
           #print 1
           if self.handle_list:
               #print "select start"
               ret = self.opener.select(1.0)
               #print "select end"
               if ret >= 0:
                   while 1:
                       #print "perform start"
                       num_handle_pre = num_handle
                       ret, num_handle = self.opener.perform()
                       #print "preform end"
                       #活动的连接数改变时
                       if num_handle != num_handle_pre:
                           result = self.opener.info_read()
                           for i in result[1]:
                               #成功
                               i.http_code = i.getinfo(i.HTTP_CODE)
                               i.recall(i)
                               self._remove(i)
                           for i in result[2]:
                               #失败,应该记录一下,或回调失败函数
                               #i为(<pycurl.Curl object at0x00C04C80>, 6, 'Could not resolve host: www.msn.com (Domain name notfound)')
                               i[0].catch(*i)
                               self._remove(i[0])
                       if ret != pycurl.E_CALL_MULTI_PERFORM:
                           #print "break"
                           break
                       self._pull()
               self._pull()
           else:
               self._add(self.waiting.get())

_opener = None
def urlopen(*arg, **key):
   global _opener
   if _opener is None:
       _opener = UrlOpen()
       _opener.start()
   _opener.add(*arg, **key)
import time
if __name__ == "__main__":
   link = ['http://www.baidu.com/', 'http://www.sina.com.cn',
'http://www.qq.com', 'http://www.sohu.com', 'http://www.163.com/',
'http://www.ifeng.com/', 'http://www.cctv.com/default.shtml',
'http://www.xinhuanet.com/', 'http://www.people.com.cn/',
'http://cn.msn.com/', 'http://www.google.cn/', 'http://cn.yahoo.com/',
'http://www.amazon.cn/?source=2009hao123famousdaohang',
'http://www.chinamobile.com/', 'http://www.pconline.com.cn/',
'http://www.chinahr.com/', 'http://www.gov.cn/',
'http://www.zhcw.com/', 'http://www.autohome.com.cn/',
'http://www.zhaopin.com/Market/hao123.jsp',
'http://fund.eastmoney.com/', 'http://www.eastmoney.com/',
'http://www.xiaonei.com/', 'http://www.soufun.com/',
'http://www.jiayuan.com/st/?id=3237&amp;url=http://www.jiayuan.com']
   link +=['http://www.qidian.com/', 'http://www.readnovel.com/',
'http://www.hongxiu.com/', 'http://www.bookge.com/',
'http://www.jjwxc.net/', 'http://hjsm.tom.com/',
'http://www.4yt.net/', 'http://www.cuiweiju.com/',
'http://book.sina.com.cn/', 'http://www.xxsy.net/',
'http://www.wansong.net/', 'http://www.myfreshnet.com/',
'http://www.fmx.cn/', 'http://www.xs8.cn/',
'http://www.qnwz.cn/', 'http://wenxue.xilu.com/']
   link +=['http://www.ganji.com/', 'http://www.58.com/',
'http://www.baixing.com/', 'http://www.263.com/',
'http://www.kuxun.cn/', 'http://www.mangocity.com/',
'http://www.e-giordano.com/', 'http://www.361sport.com/',
'http://www.levi.com.cn/', 'http://www.lee.com.cn/',
'http://www.sharp.cn/', 'http://www.galanz.com.cn/',
'http://www.yongle.com.cn/', 'http://www.xinfei.com/']

   begin = time.time()
   number = 0
   dumped = set()
   def show(c):
       global number
       number +=1

       content = c.content.getvalue()
       print number,". cost time", time.time() - begin,"htmllen", len(content)
       print c.url
       begin_pos = None
       count = 1
       while True:
           pos = content.rfind('<a href="http://',None,begin_pos)
           #print content[pos:pos+200]
           if pos!=-1:
               begin_pos = pos
               url = content[pos+9:content.find('"',pos+13)]
               if url in dumped:
                   return
               dumped.add(url)
               print "\tadd",url
               urlopen(url,show)
               count +=1
               if count>10:
                   break
           else:
               break
   link = set(link)
   print "total link", len(link)
   for i in link:
       urlopen(i, show)
       dumped.add(i)
   _opener.join()
   print "cost time", time.time() - begin
