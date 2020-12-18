#!/usr/bin/env python
# coding=utf-8

# re.split 截断获取想要的日期范围内的数据 
# re.sub 将有问题的流释行清除掉
# re.findall 查找出所有的td行的值

import requests,re,xlsxwriter
from multiprocessing.dummy import Pool as ThreadPool

def Allstockid():
    stockids = []
    for pagenum in range(1,57):
            r = requests.get(r'http://data.10jqka.com.cn/funds/ggzjl/board/3/field/code/order/asc/page/' + str(pagenum) + '/ajax/1/',timeout = 200)
            codes = re.findall('target="_blank">(.+)?</a></td>', r.text, re.I)
            #print codes
            stockids.extend(codes)
    return stockids

def hismoney(codeid):
    
    r = requests.get(r'http://stockpage.10jqka.com.cn/' + codeid + '/funds/#funds_lszjsj')
    datev = re.findall('class="border_l_none">(.+)?</td>', r.text, re.I)
    
    text = re.sub('<!--(.+)?-->', '', r.text)
    
    if len(datev) >5:
        #print date[4]
        data = re.split('tr_border|>' + datev[4] +'</td',text)
        # data = re.split('tr_border|>20161213</td',text)
    
    p = re.compile('>(\S+)</td>' )
    q = p.findall(data[1])
    
    # if len(q) >11:
    #     print q[:11]
    #     print q[11:22]
    #     print q[22:33]
#     x=0
#     y=11
#     while (len(q)+1) >y:
#         dmoney = q[x:y]
#         dmoney.append(codeid)
#         mondata.append(dmoney)
#         x=x+11
#         y=y+11
    
    x=0
    y=11
    while (len(q)+1) >y and len(q)>43:
        if float((q[:11])[3])<1000 or float((q[11:22])[3])<800 or float((q[22:33])[3])<500 :
#        if float((q[:11])[3])<4800 or float((q[11:22])[3])<4800 :
            break
        dmoney = q[x:y]
        dmoney.append(codeid)
        mondata.append(dmoney)
       
        x=x+11
        y=y+11
        
def toexcel(data):
    workbook = xlsxwriter.Workbook('stock.xlsx')
    worksheet = workbook.add_worksheet('hismoney')
    bold = workbook.add_format({'bold': 1})
    headings = [u'日期', u'收盘价', u'涨跌幅', u'资金净流入', u'5日主力净流入', u'大单净额', u'大单净占比',u'中单净额', u'中单净占比',u'小单净额', u'小单净占比',u'股票代码']
    worksheet.write_row('A1', headings, bold)
    row = 1
    col = 0
    for linev in  data:    
        worksheet.write_row(row,col,linev)    
        row += 1
    workbook.close()

def main():
    global mondata
    mondata = []    
        
    codes = Allstockid()
#     print len(codes),codes
    
    for code in codes:
        print code
        hismoney(code)
#     pool = ThreadPool(30) 
#     pool.map(hismoney, codes)
    print mondata
    toexcel(mondata)
    
#     pool.close()
#     pool.join()
    print 'doing ok'
    

if __name__ =='__main__':

    main()

