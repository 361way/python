#!/usr/bin/env python
# coding=utf-8
## author: yangbk（itybku@139.com）
## site: www.361way.com

def funa():
    print 'running funa ......'

def funb():
    print 'running funb ......'

action = raw_input('请输入地址：')
if action == "funa":
    funa()
elif action == "funb":
    funb()
