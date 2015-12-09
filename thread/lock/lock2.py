#!/usr/bin/env python
# coding=utf-8

import threading                            # 导入threading模块
import time                             # 导入time模块
class mythread(threading.Thread):                   # 通过继承创建类
    def __init__(self,threadname):                  # 初始化方法
        threading.Thread.__init__(self,name = threadname) 
    def run(self):                          # 重载run方法
        global x                        # 使用global表明x为全局变量
        lock.acquire()                      # 调用lock的acquire方法
        for i in range(3):
            x = x + 1
        time.sleep(2)           # 调用sleep函数，让线程休眠5秒
        print x
        lock.release()                # 调用lock的release方法
lock = threading.Lock()               # 类实例化
tl = []                          # 定义列表
for i in range(10):
    t = mythread(str(i))            # 类实例化
    tl.append(t)              # 将类对象添加到列表中
                           
x=0                        # 将x赋值为0
for i in tl:
    i.start()                     # 依次运行线程
