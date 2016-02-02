#!/usr/bin/env python
# coding=utf-8

from backend import account
data = raw_input('请输入地址：')
if data == 'account/login':
    account.login()
elif data == 'account/logout':
    account.logout()
