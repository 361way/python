#!/usr/bin/env python
# coding=utf-8
# itybku@139.com <www.361way.com>
# desc: 计算波动率
import sys,requests,re
reload(sys)  
sys.setdefaultencoding('utf8')   

import tushare as ts
from multiprocessing.dummy import Pool as ThreadPool

def per(code):
        #print code,type(code)
	try:
		x = ts.get_hist_data(code,start='2017-01-01',end='2017-12-05')  
		# for i in x.p_change:
		# if abs(i)>3:    
		# 	print i 

		y = len([i for i in x.p_change if abs(i)>3])
		if len(x)>1 and y >1:
		   print "%s %.2f%%" %(code ,(float(y)/float(len(x))*100))
	except:
	       print "code error"

def Allstockid():
    stockids = []
    #html = urllib2.urlopen(r'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx/JS.aspx?type=ct&st=(Code)&sr=1&p=1&ps=4000&js=(x)&token=894050c76af8597a853f5b408b759f5d&cmd=C._A&sty=DCFFITA&rt=49373571',timeout = 200)
    html = requests.get(r'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx/JS.aspx?type=ct&st=(Code)&sr=1&p=1&ps=4000&js=(x)&token=894050c76af8597a853f5b408b759f5d&cmd=C._A&sty=DCFFITA&rt=49373571',timeout = 200)
    for line in  re.split('","',html.text):
        linev = line.split(',')[1]
        linev = str(linev)
        stockids.append(linev)
    return stockids

'''
def main():
    codes = Allstockid()
    #print codes

    pool = ThreadPool(30) 
    pool.map(per, codes)
    pool.close()
    pool.join()

if __name__ =='__main__':
    main()
'''
for code in Allstockid():
    per(code)

