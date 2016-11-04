#!/usr/bin/env python
# -*- coding: utf-8 -*-
# site: www.361way.com
# mail: itybku@139.com

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import glob
import xlrd
import xlsxwriter
import re

workbook = xlsxwriter.Workbook('date_report.xlsx')
worksheet = workbook.add_worksheet('Sheet1')
bold = workbook.add_format({'bold': 1})
headings = [u'时间', u'问题描述', u'责任人']
worksheet.write_row('A1', headings, bold)


def get_xlsx_data(file):
    #data = xlrd.open_workbook(u"D:\\2016\\杭州软件服务部管理服务工作日报(2016-07-13).xlsx")
    data = xlrd.open_workbook(file)
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    timedata = table.row_values(0)[0]
    
    timedata = re.split('（',timedata.encode("utf-8",'ignore'))
    timedata = timedata[1].replace('）','')


    #print timedata
    for i in range(7,nrows):
        #print table.row_values(i)[0]
        if  table.row_values(i)[0] == 1.0:
            maxv = i
    #print maxv        
    if maxv:
        for i in range(6,(maxv-2)):
            if  table.row_values(i)[2]:
                #print timedata + '|' + table.row_values(i)[2].encode("utf-8",'ignore')
                data_arry.append([timedata,table.row_values(i)[2].encode("utf-8",'ignore'),'361way'])
    else:
        for i in range(6,nrows):
            if  table.row_values(i)[2]:
                #print timedata + '|' + table.row_values(i)[2].encode("utf-8",'ignore')
                data_arry.append([timedata,table.row_values(i)[2].encode("utf-8",'ignore'),'361way'])

data_arry = []
for file in glob.glob("d:\\2016\\*.xlsx"):
    get_xlsx_data(file)
    
row = 1
col = 0
for linev in  data_arry:
    #print linev
    worksheet.write_row(row,col,linev)
    row += 1

workbook.close()
