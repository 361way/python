#!/usr/bin/env python
# coding=utf-8
#
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2,re
import xlrd
import xlsxwriter

workbook = xlsxwriter.Workbook('date_report.xlsx')
worksheet = workbook.add_worksheet('Sheet1')
bold = workbook.add_format({'bold': 1})
headings = [u'时间', u'问题描述', u'责任人']
worksheet.write_row('A1', headings, bold)
worksheet.freeze_panes(1, 0)

row = 1
col = 0

html = urllib2.urlopen(r'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx/JS.aspx?type=ct&st=(Code)&sr=1&p=1&ps=3500&js=(x)&token=894050c76af8597a853f5b408b759f5d&cmd=C._A&sty=DCFFITA&rt=49311621')
for line in  re.split('","',html.read()):
    line = line.strip('"')
    linev = line.split(',')[:11]

    worksheet.write_row(row,col,linev)
    row += 1
workbook.close()


