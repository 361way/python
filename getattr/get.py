#!/usr/bin/env python
# coding=utf-8
## author: yangbk（itybku@139.com）
## site: www.361way.com

class getfun:
    def funa(self):
        print  'processNavigate'

    def funb(self):
        print 'processCreateTab'


action = raw_input('请输入地址：')
newfun = getfun()
fun = getattr(newfun,action)
fun()
