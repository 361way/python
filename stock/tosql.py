#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Create Time:2017-03-10 10:16:55
# Author:itybku < www.361way.com >
# 遍历一段时期的数据并写入数据库

from sqlalchemy import create_engine
import tushare as ts
import requests,re
from multiprocessing.dummy import Pool as ThreadPool


def tosql(id):
#df = ts.get_k_data('600000',ktype='D',index=True,start='2016-03-01', end='2017-03-08')
    df = ts.get_k_data(id,ktype='D',start='2016-03-01', end='2017-03-08')
    engine = create_engine('mysql://root:password@127.0.0.1/stock?charset=utf8')

# tick_data 为插入时的表名
    df.to_sql('tick_data',engine,if_exists='append')

def Allstockid():
    stockids = []
    for pagenum in range(1,57):
            r = requests.get(r'http://data.10jqka.com.cn/funds/ggzjl/board/3/field/code/order/asc/page/' + str(pagenum) + '/ajax/1/',timeout = 200)
            codes = re.findall('target="_blank">(.+)?</a></td>', r.text, re.I)
            #print codes
            stockids.extend(codes)
    return stockids


def writedata():
    codes = Allstockid()
    pool = ThreadPool(30) 
    pool.map(tosql, codes)

    pool.close()
    pool.join()
    print 'write to mysql is ok!'

writedata()
