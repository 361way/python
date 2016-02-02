#!/usr/bin/env python
# coding=utf-8

action = raw_input('请输入地址：')
newfun = __import__('funab')
fun = getattr(newfun,action)
fun()
