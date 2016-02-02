#!/usr/bin/env python
# coding=utf-8
## author: yangbk（itybku@139.com）
## site: www.361way.com

def funa():
    print  'processNavigate'

def funb():
    print 'processCreateTab'

action = raw_input('请输入地址：')
actionMap = {"processNavigate":funa ,"processCreateTab":funb}
actionMap[action]()
