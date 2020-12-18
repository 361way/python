#!/usr/bin/python
#-*- coding: utf-8 -*-
# code from www.361way.com <itybku@139.com>

import pexpect
child = pexpect.spawn('ls -l /root')
child.expect(pexpect.EOF)
print child.before.decode()


'''
上面的代码可以正常执行，下面的代码执行的时候，print会打印出EOF捕获的异常，
因为spawn函数不支持管道、通配符、标志输入、输出、错误重定向
'''

child = pexpect.spawn('cat /root/test.file|grep 123')
child.expect(pexpect.EOF)
print child.before.decode()


'''
如下代码可以正常执行，我们可以通过args参数支持管道，通配符
等的执行，这些相当于是bash执行的参数
'''
child = pexpect.spawn('/bin/bash',['-c','cat /root/test.file|grep 123'])
child.expect(pexpect.EOF)
print child.before.decode()

