#!/usr/bin/env python
# coding=utf-8
#import urllib2,re,os,time
import requests,re,os,time,xlsxwriter,json
from multiprocessing.dummy import Pool as ThreadPool
workbook = xlsxwriter.Workbook('stock.xlsx')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def formatid(codeid):
    if str(codeid)[0] != '6':
        return str(codeid) + '2'
    else:
        return str(codeid) + '1'  
    
def getValue(codeid):
    codeid = formatid(codeid)
    html = requests.get(r'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=' + str(codeid) + '&sty=DCFFMBFMS&st=&sr=&p=&ps=&cb=&js=(x)&token=0b9469e9fdfd123fcec4532ae1c20f4f&_=1481174762100',timeout = 200)
    stockv = (html.text).strip('"')
    return stockv.split(",")[1:]

def dfcfAllid():
    stockids = []
    html = requests.get(r'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx/JS.aspx?type=ct&st=(Code)&sr=1&p=1&ps=4000&js=(x)&token=894050c76af8597a853f5b408b759f5d&cmd=C._A&sty=DCFFITA&rt=49373571',timeout = 200)
    for line in  re.split('","',html.text):
        linev = line.split(',')[1]
        stockids.append(linev)
    return stockids

def toexcel(data):
    worksheet = workbook.add_worksheet('monin_dfcf')
    bold = workbook.add_format({'bold': 1})
    headings = [u'股票代码', u'名称', u'当前价', u'涨跌幅', u'净流入', u'涨跌值', u'日期']
    worksheet.write_row('A1', headings, bold)
    row = 1
    col = 0
    for linev in  data:    
        worksheet.write_row(row,col,linev)    
        row += 1
    #workbook.close()

def writemonin():
    codes = dfcfAllid()
    pool = ThreadPool(30) 
    results = pool.map(getValue, codes)
    toexcel(results)

    pool.close()
    pool.join()
    print 'writemonin doing ok'
def thscodes():
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
        data = re.split('tr_border|>' + datev[4] +'</td',text)
    p = re.compile('>(\S+)</td>' )
    q = p.findall(data[1])
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
        
def hismon(data):
    worksheet2 = workbook.add_worksheet('hismoney')
    bold = workbook.add_format({'bold': 1})
    headings = [u'日期', u'收盘价', u'涨跌幅', u'资金净流入', u'5日主力净流入', u'大单净额', u'大单净占比',u'中单净额', u'中单净占比',u'小单净额', u'小单净占比',u'股票代码']
    worksheet2.write_row('A1', headings, bold)
    row = 1
    col = 0
    for linev in  data:    
        worksheet2.write_row(row,col,linev)    
        row += 1
    #workbook.close()

def thshis():
    global mondata
    mondata = []    
    codes = thscodes()
    for code in codes:
        print code
        hismoney(code)
    print mondata
    hismon(mondata)
    print 'doing ok'
    
def  mav(codeid):
    r = requests.get(r'http://d.10jqka.com.cn/v2/realhead/hs_' + str(codeid) + '/last.js',timeout = 200)
    codes = re.findall(('\{.*?\}\}' ),r.text, re.I)

    if codes:
        hjson = json.loads(codes[0])
        
        name = hjson['items']['name']
        famc = hjson['items']['3475914']
        tmv = hjson['items']['3541450']
        timev = hjson['items']['time']
        
        return [codeid,name,famc,tmv,timev]
    
def thslast():    
    codes = thscodes()
    worksheet3 = workbook.add_worksheet('tmv')
    bold = workbook.add_format({'bold': 1})
    headings = [u'股票代码', u'名称', u'流通值', u'总市值', u'日期']
    worksheet3.write_row('A1', headings, bold)
    worksheet3.freeze_panes(1, 0)
    row = 1
    col = 0
    for code in codes:
        print code
        ov = mav(code)
        if ov: 
            worksheet3.write_row(row,col,ov)    
        row += 1
    #workbook.close()
    print 'ok now !!!'   

writemonin()
thshis()
thslast()
workbook.close()
    