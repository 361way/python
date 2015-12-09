#!/usr/bin/env python
# coding=utf-8

import threading                            # 导入threading模块
import time                             # 导入time模块
class mythread(threading.Thread):        # 通过继承创建类
    def __init__(self,threadname):      # 初始化方法
        # 调用父类的初始化方法
        threading.Thread.__init__(self,name = threadname) 
    def run(self):                          # 重载run方法
        global x                  # 使用global表明x为全局变量
        for i in range(3):
            x = x + 1
        time.sleep(5)          # 调用sleep函数，让线程休眠5秒
        print x
                                                             
tl = []                              # 定义列表
for i in range(10):
    t = mythread(str(i))               # 类实例化
    tl.append(t)                      # 将类对象添加到列表中
                                                         
x=0                                 # 将x赋值为0
for i in tl:
    i.start()  
