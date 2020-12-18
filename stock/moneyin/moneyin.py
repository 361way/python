#!/usr/bin/env python
# coding=utf-8
#
import urllib2,re,os,time
from prettytable import *

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def formatid(codeid):
    if str(codeid)[0] != '6':
        return str(codeid) + '2'
    else:
        return str(codeid) + '1'  
    
def getValue(codeid):
    codeid = formatid(codeid)

    html = urllib2.urlopen(r'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=' + str(codeid) + '&sty=DCFFMBFMS&st=&sr=&p=&ps=&cb=&js=(x)&token=0b9469e9fdfd123fcec4532ae1c20f4f&_=1481174762100')
    stockv = (html.read()).strip('"')
    return stockv.split(",")[1:]


codes = ['000060','600050']

while True:
    row = PrettyTable()
    row.field_names = ["codeid","name","当前价","百分比","净流入","涨跌值","date"]
    for codeid in codes:
        
        row.add_row(getValue(codeid))
        
    result = row.get_string(hrules=ALL)
    print result
    time.sleep(2)
    clear()




  
