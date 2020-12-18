#!/usr/bin/python
#-*- coding: utf-8 -*-
# code from www.361way.com <itybku@139.com>

import pexpect

'''
pexpect.spawn执行出的日志结果是二进制日志，所以下open
函数执行写入时，也要是二进制格式，该脚本执行完成后，
cat ttt文件就会发现是ls -l /root执行的结果
'''
f = open('ttt','wb')
child = pexpect.spawn('ls -l /root',logfile=f)
child.expect(pexpect.EOF)
f.close()


'''
也可以将执行的日志输出到标准输出，不过需要启用
spawnu方法，u代表unicode
'''
import sys
child = pexpect.spawnu('ls -l /root',logfile=sys.stdout)
child.expect(pexpect.EOF)


'''
同时也可以通过cwd参数指定执行该脚本时默认跳到的路径
'''
child = pexpect.spawnu('ls',logfile=sys.stdout,cwd='/home')
child.expect(pexpect.EOF)
