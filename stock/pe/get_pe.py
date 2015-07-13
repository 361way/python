#!/usr/bin/python
#coding=utf-8
# 1、pe在 0~20 之间的企业
# 2、流通股本小于50亿的企业


import urllib2
import time 
import json



def get_pe(stockid):
    try:
	url = 'http://d.10jqka.com.cn/v2/realhead/hs_%s/last.js' % stockid
        send_headers = {
	    'Host':'d.10jqka.com.cn',
	    'Referer':'http://stock.10jqka.com.cn/',
	    'Accept':'application/json, text/javascript, */*; q=0.01',
	    'Connection':'keep-alive',
	    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36',
            'X-Forwarded-For':'124.160.148.178',
	    'X-Requested-With':'XMLHttpRequest'
	}
        req = urllib2.Request(url,headers=send_headers)
        f = urllib2.urlopen(req)

	data = f.read().split('items":',1)[1]
	data = data.split('})',1)[0]


	J_data = json.loads(data)
	#J_data = json.dumps(data,indent=4,encoding='utf-8')
	stockpe = J_data['2034120']
	stockname = J_data['name']
        sumvalue = J_data['3475914']
        currentprice = J_data['10']
	#print stockid,stockname,stockpe
	return stockname,stockpe,sumvalue,currentprice
    except urllib2.HTTPError, e:  
        #return stockid ,'get happed httperror'
        return e.code

if __name__ == '__main__':
    print 'stockid  stockname  currentprice  stockpe  Billvalue'
    stockids = [line.strip() for line in open("stock_exp.txt", 'r')]
    for stockid in stockids:
      try:
        stockname,stockpe,sumvalue,currentprice = get_pe(stockid)
        if sumvalue:
           Billvalue = round(float(sumvalue)/1000/1000/100)
        else:
           Billvalue = 0
        
        if stockpe:
           if float(stockpe) > 0 and float(stockpe) < 22 and Billvalue < 200 :
              print stockid,stockname,currentprice,stockpe,Billvalue
        #else:
        #   print stockid
      except TypeError ,e:
        print stockid ,'get is error'
