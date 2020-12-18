#!/usr/bin/env python
# coding=gbk

from BeautifulSoup import BeautifulSoup
# import urllib
# import xlwt
import urllib2
import xlsxwriter

# wb = xlwt.Workbook()
# ws = wb.add_sheet('a test sheet')


# workbook = xlsxwriter.Workbook('BlastResults.xlsx')
# worksheet = workbook.add_worksheet('Sheet1')
# 
# row = 1
# col = 0


#f = urllib2.urlopen("http://data.10jqka.com.cn/funds/ggzjl/field/zjjlr/order/desc/ajax/1/")
f = urllib2.urlopen("http://data.10jqka.com.cn/funds/ggzjl/field/zjjlr/order/desc/ajax/1/")
# http://data.10jqka.com.cn/funds/ggzjl/field/zjjlr/order/desc/page/2/ajax/1/
html = f.read()



# 
soup = BeautifulSoup(html)
# print soup.prettify()
# print soup
  
#table = soup.find("table",id="alignmentTable")
table = soup.find("table")



for i in table.findAll('th'):
    print i.find_all(text)

# for tag in table.findAll(['tr','th','td']):
#     print tag.findAll('th')


# rows = table.findAll("tr")
# print rows
# for row in rows:
#      print row
#      cols = row.find_all('td')

# x = 0
# for tr in rows:
#     cols = tr.findAll("td")
#     if not cols: 
#         # when we hit an empty row, we should not print anything to the workbook
#         continue
#     y = 0
#     for td in cols:
#         texte_bu = td.text
#         texte_bu = texte_bu.encode('utf-8')
#         texte_bu = texte_bu.strip()
#         worksheet.write_row(x, y, td.text)
#         print(x, y, td.text)
#         y = y + 1
#     # update the row pointer AFTER a row has been printed
#     # this avoids the blank row at the top of your table
#     x = x + 1
 
#workbook.close()