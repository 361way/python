#!/usr/bin/env python
#coding=utf-8

import threading
import pycurl
from cStringIO import StringIO

class UrlOpen(threading.Thread):
    """异步下载网页"""

    def __init__(self):
        super(UrlOpen,self).__init__()
        self.opener = pycurl.CurlMulti()
        self.handle_list=[]

    def add(self,url,recall,writer=StringIO()):
        """
        参数:网址,回调函数,存放临时数据的对象
        """
        c = pycurl.Curl()

        #可以传给回调函数
        c.url=url
        c.content = writer
        c.recall = recall
        c.setopt(c.URL,url)
        c.setopt(c.WRITEFUNCTION,c.content.write)

        self.handle_list.append(c)
        self.opener.add_handle(c)

    def _remove(self,c):
        c.close()
        self.opener.remove_handle(c)
        self.handle_list.remove(c)


    def run(self):
        num_handle=len(self.handle_list)
        while 1:
            ret = self.opener.select(10.0)
            if ret == -1:  continue
            while 1:
                num_handle_pre=num_handle
                ret, num_handle =self.opener.perform()
                #活动的连接数改变时
                if num_handle!=num_handle_pre:
                    result=self.opener.info_read()
                    print result
                    for i in result[1]:
                        #成功
                        i.http_code = i.getinfo(i.HTTP_CODE)
                        self._remove(i)
                        i.recall(i)
                    for i in result[2]:
                        #失败,应该记录一下
                        self._remove(i)

                if ret != pycurl.E_CALL_MULTI_PERFORM:
                    break

_opener=None
def urlopen(*arg,**key):
    global _opener
    if _opener is None:
        _opener=UrlOpen()
        _opener.add(*arg,**key)
        _opener.start()
    else:
        _opener.add(*arg,**key)

def show(x):
    print x.content.getvalue()
if __name__=="__main__":
    urlopen("http://blog.linuxeye.com/400.html",show)
    _opener.join()
