#!/usr/bin/env python
# coding=utf-8
# shelve all stock codes
import requests,re,shelve

def dfcfall():
    stockids = []
    #html = urllib2.urlopen(r'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx/JS.aspx?type=ct&st=(Code)&sr=1&p=1&ps=4000&js=(x)&token=894050c76af8597a853f5b408b759f5d&cmd=C._A&sty=DCFFITA&rt=49373571',timeout = 200)
    html = requests.get(r'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx/JS.aspx?type=ct&st=(Code)&sr=1&p=1&ps=4000&js=(x)&token=894050c76af8597a853f5b408b759f5d&cmd=C._A&sty=DCFFITA&rt=49373571',timeout = 200)
    for line in  re.split('","',html.text):
        linev = line.split(',')[1]
        stockids.append(linev)
    return stockids


def thsall():
    stockids = []
    for pagenum in range(1,57):
            r = requests.get(r'http://data.10jqka.com.cn/funds/ggzjl/board/3/field/code/order/asc/page/' + str(pagenum) + '/ajax/1/',timeout = 200)
            codes = re.findall('target="_blank">(.+)?</a></td>', r.text, re.I)
            #print codes
            stockids.extend(codes)
    return stockids

def shewrite(key,value):
    d = shelve.open('shelve.db', flag='c', protocol=2, writeback=False)
    assert isinstance(d, shelve.Shelf)
    d[key] = value
    d.sync()
    d.close()

def sheread(key):
    d = shelve.open('shelve.db')
    assert isinstance(d, shelve.Shelf)
    return d[key]
    d.close()

if __name__ =='__main__':
    
    shewrite('dfcfall',dfcfall())
    shewrite('thsall',thsall())
    
    print sheread('dfcfall')
    print 'thsall' , sheread('thsall')
