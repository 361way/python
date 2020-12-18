#!/usr/bin/env python
# coding=utf-8
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')   

import requests,re,urllib2,xlsxwriter
from multiprocessing.dummy import Pool as ThreadPool

def Allstockid():
    stockids = []
    #html = urllib2.urlopen(r'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx/JS.aspx?type=ct&st=(Code)&sr=1&p=1&ps=4000&js=(x)&token=894050c76af8597a853f5b408b759f5d&cmd=C._A&sty=DCFFITA&rt=49373571',timeout = 200)
    html = requests.get(r'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx/JS.aspx?type=ct&st=(Code)&sr=1&p=1&ps=4000&js=(x)&token=894050c76af8597a853f5b408b759f5d&cmd=C._A&sty=DCFFITA&rt=49373571',timeout = 200)
    for line in  re.split('","',html.text):
        linev = line.split(',')[1]
        stockids.append(linev)
    return stockids



def stockscore(stockid):
    html = requests.get(r'http://vaserviece.10jqka.com.cn/advancediagnosestock/html/' + str(stockid) + '/index.html')
    
    # regex = '<ins class="scoreall" style="display: none">(.+?)</ins>'
    # pattern = re.compile(regex,re.I)
    # score = re.findall(pattern, html.text)
    
    # regex2 = '<div class="zonghe_h">\s+<h2>(.+?)</h2>\s+<p>打败了99%的股票</p>\s+<h3 class="redtxt">(.+?)</h3>\s+</div>'
    # pattern2 = re.compile(regex2,re.M)
    # data = re.search(pattern2, html.text)
    
    score = re.findall('<ins class="scoreall" style="display: none">(.+?)</ins>',html.text,re.I)
    name = re.findall('<h2>(.+?)\(',html.text,re.I)
    mark = re.findall('<p>打败了(.+?)%的股票</p>',html.text,re.I)
    suggest = re.findall("<h3 class='redtxt'>(.+?)</h3>",html.text,re.I)
    
    if len(name) != 0 and len(score) != 0 and len(mark) != 0 and len(suggest) != 0:
        return stockid,name[0].decode('utf8'),score[0],mark[0],suggest[0]
#     if len(suggest) == 0:
#         return stockid,name[0],score[0],mark[0] 
#     else:
#         return stockid,name[0],score[0],mark[0],suggest[0]
#      
def toexcel(data):
    workbook = xlsxwriter.Workbook('stockscore.xlsx')
    worksheet = workbook.add_worksheet('Sheet1')
    bold = workbook.add_format({'bold': 1})
    headings = [u'股票代码', u'名称', u'综合诊断分', u'打败了%的股票', u'建议']
    worksheet.write_row('A1', headings, bold)
    row = 1
    col = 0
    for linev in  data:
        if linev is not None:    
            worksheet.write_row(row,col,linev)    
            row += 1
    workbook.close()
#stockscore('000961')

def main():
    codes = Allstockid()
    print codes

    pool = ThreadPool(30) 
    results = pool.map(stockscore, codes)
    print results
    toexcel(results)
    pool.close()
    pool.join()
    print 'get all data'

    
if __name__ =='__main__':
    main()
    #print stockscore('000961')
