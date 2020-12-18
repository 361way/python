#!/usr/bin/env python
# coding=utf-8
# code from www.361way.com
try:
    import cPickle as pickle
except:
    import pickle
import pprint

data = [ { 'a':'A', 'b':2, 'c':3.0 } ]
print 'DATA:',
pprint.pprint(data)

data_string = pickle.dumps(data)
print 'PICKLE:', data_string
