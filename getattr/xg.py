#!/usr/bin/python
# coding=utf-8
## author: yangbk(itybku@139.com)
## site: www.361way.com
## desc: test inspect module || hasattr、setattr 、delattr and getattr

class test:
    def __init__(self):
        self.name = 'www.361way.com'
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print "Hello,I'm %s" %self.name  
foo = test()

# test for inspect
im = foo.greet
import inspect
if inspect.isroutine(im):
        im()

# test for hasattr getattr  setattr delattr
print hasattr(foo,'abc')
print hasattr(foo,'getName')

setattr(foo,'age',18)
print getattr(foo,'age')

print getattr(foo,'name')

setattr(foo,'name','newname')
print getattr(foo,'name')

delattr(foo,'name')
print getattr(foo,'name','not find')


