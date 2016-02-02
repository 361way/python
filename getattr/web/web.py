#!/usr/bin/env python
# coding=utf-8
## author: yangbk（itybku@139.com）
## site: www.361way.com

'''
from backend import account
data = raw_input('请输入地址：')
if data == 'account/login':
    account.login()
elif data == 'account/logout':
    account.logout()
'''
data = raw_input('请输入地址：')
array = data.split('/')

userspance = __import__('backend.'+array[0])
model = getattr(userspance , array[0])
func = getattr(model,array[1])
func()
