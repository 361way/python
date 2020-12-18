#!/usr/bin/env python
# coding=utf-8
# tmv = Total market value
# famc = free-float market capitalisation
# mav =market value
import requests,re,json,xlsxwriter

def Allstockid():
    stockids = []
    for pagenum in range(1,57):
            r = requests.get(r'http://data.10jqka.com.cn/funds/ggzjl/board/3/field/code/order/asc/page/' + str(pagenum) + '/ajax/1/',timeout = 200)
            codes = re.findall('target="_blank">(.+)?</a></td>', r.text, re.I)
            #print codes
            stockids.extend(codes)
    return stockids

def  mav(codeid):
#     r = requests.get(r'http://d.10jqka.com.cn/v2/realhead/hs_002346/last.js',timeout = 200)
    r = requests.get(r'http://d.10jqka.com.cn/v2/realhead/hs_' + str(codeid) + '/last.js',timeout = 200)
    codes = re.findall(('\{.*?\}\}' ),r.text, re.I)
    # print codes[0]
    # s =  json.dumps(codes[0],indent=4,encoding='utf-8')
    if codes:
        hjson = json.loads(codes[0])
        
        name = hjson['items']['name']
        famc = hjson['items']['3475914']
        tmv = hjson['items']['3541450']
        timev = hjson['items']['time']
        
        return [codeid,name,famc,tmv,timev]

#print mav('000404')
# edata = []
# codes = Allstockid()
# for code in codes:
#     print code
#     ov = mav(code)
#     if ov:
#         edata.extend(ov)
# print edata

codes = Allstockid()
workbook = xlsxwriter.Workbook('stock.xlsx')
worksheet = workbook.add_worksheet('tmv')
bold = workbook.add_format({'bold': 1})
headings = [u'股票代码', u'名称', u'流通值', u'总市值', u'日期']
worksheet.write_row('A1', headings, bold)
worksheet.freeze_panes(1, 0)
row = 1
col = 0
for code in codes:
    print code
    ov = mav(code)
    if ov: 
        worksheet.write_row(row,col,ov)    
    row += 1
workbook.close()
print 'ok now !!!'
