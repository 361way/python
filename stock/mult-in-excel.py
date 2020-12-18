#!/usr/bin/env python
# coding=utf-8
#
#import urllib2,re,os,time
import requests,re,os,time,xlsxwriter
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

def toexcel(data):
    workbook = xlsxwriter.Workbook('stock.xlsx')
    worksheet = workbook.add_worksheet('monin_dfcf')
    bold = workbook.add_format({'bold': 1})
    headings = [u'股票代码', u'名称', u'当前价', u'涨跌幅', u'净流入', u'涨跌值', u'日期']
    worksheet.write_row('A1', headings, bold)
    row = 1
    col = 0
    for linev in  data:    
        worksheet.write_row(row,col,linev)    
        row += 1
    workbook.close()



#codes = ['000060','600050']

def main():
    codes = Allstockid()
    print codes

    pool = ThreadPool(30) 
    results = pool.map(getValue, codes)
    toexcel(results)
    

    pool.close()
    pool.join()

    

if __name__ =='__main__':
    start = time.time()
    main()
    costtime = time.time() - start
    print 'mult costime:',costtime




  
