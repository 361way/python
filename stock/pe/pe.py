#!/usr/bin/python
#coding=utf-8
import urllib2
import time 
import json

codeid = '600030'

f = urllib2.urlopen('http://d.10jqka.com.cn/v2/realhead/hs_%s/last.js'%codeid)

data = f.read().split('items":',1)[1]
data = data.split('})',1)[0]


J_data = json.loads(data)
#J_data = json.dumps(data,indent=4,encoding='utf-8')
stockpe = J_data['2034120']
stockname = J_data['name']


print codeid,stockname,stockpe

