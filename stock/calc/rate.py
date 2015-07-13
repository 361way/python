#!/usr/bin/python
#coding=utf-8
from prettytable import *

def  rate(value):
	narrow = ["%.2f" % (i*0.01*value) for i in range(99,89,-1)]
	narrow.insert(0,'-')

	add = ["%.2f" % (i*0.01*value) for i in range(101,111)]
	add.insert(0,'+')

	field = [i for i in range(1,11)]
	field.insert(0,'+/-')

	x = PrettyTable()
	x.field_names = field
	x.add_row(narrow)
	x.add_row(add)
	result = x.get_string(hrules=ALL)
	print(result)

print 'wwdn 维维豆奶'
rate(12.61)
'''
print 'hhkg  辉煌科技'
rate(32.27)
print 'sdby  山东玻药'
rate(22.49)

print 'jbfz  津滨发展'
rate(9.92)
print 'hbyy '
rate(12.39)
'''
#print 'tpjt 塔牌集团'
#rate(23.18)
print 'xspc 小商品城'
rate(15.32)
print 'yjpj 燕京啤酒'
rate(12.34)
