#!/usr/bin/env python
# coding=utf-8
#
#import urllib2,re,os,time
import requests,re,os,time
from multiprocessing.dummy import Pool as ThreadPool

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def formatid(codeid):
    if str(codeid)[0] != '6':
        return str(codeid) + '2'
    else:
        return str(codeid) + '1'  
    
def getValue(codeid):
    codeid = formatid(codeid)

    #html = urllib2.urlopen(r'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=' + str(codeid) + '&sty=DCFFMBFMS&st=&sr=&p=&ps=&cb=&js=(x)&token=0b9469e9fdfd123fcec4532ae1c20f4f&_=1481174762100',timeout = 200)
    html = requests.get(r'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=' + str(codeid) + '&sty=DCFFMBFMS&st=&sr=&p=&ps=&cb=&js=(x)&token=0b9469e9fdfd123fcec4532ae1c20f4f&_=1481174762100',timeout = 200)
    stockv = (html.text).strip('"')
    return stockv.split(",")[1:]


def Allstockid():
    stockids = []
    #html = urllib2.urlopen(r'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx/JS.aspx?type=ct&st=(Code)&sr=1&p=1&ps=4000&js=(x)&token=894050c76af8597a853f5b408b759f5d&cmd=C._A&sty=DCFFITA&rt=49373571',timeout = 200)
    html = requests.get(r'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx/JS.aspx?type=ct&st=(Code)&sr=1&p=1&ps=4000&js=(x)&token=894050c76af8597a853f5b408b759f5d&cmd=C._A&sty=DCFFITA&rt=49373571',timeout = 200)
    for line in  re.split('","',html.text):
        linev = line.split(',')[1]
        stockids.append(linev)
    return stockids



#codes = ['000060','600050']

def main():
    codes = Allstockid()
    print codes

    pool = ThreadPool(4) 
    results = pool.map(getValue, codes)
    print results
    
#     results = [pool.apply_async(getValue, codeid) for codeid in codes]
#     print 'Ordered results using pool.apply_async():'
#     for r in results:
#         print '\t', r.get()

    pool.close()
    pool.join()

    

if __name__ =='__main__':
    start = time.time()
    main()
    costtime = time.time() - start
    print 'mult costime:',costtime




  
