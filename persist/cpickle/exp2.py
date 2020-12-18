#!/usr/bin/env python
# coding=utf-8
# code from www.361way.com
try:
    import cPickle as pickle
except:
    import pickle

obj = {'a' : 'b', 'c' : 'd'}
obj2 = [0, 1, 1, 0, 1]
f = open('obj.pkl', 'wb')
pickle.dump(obj, f, protocol=2)
pickle.dump(obj2, f, protocol=2)
f.close()

f = open('obj.pkl', 'rb')
x1 = pickle.load(f)
x2 = pickle.load(f)
print x1,x2
f.close()
