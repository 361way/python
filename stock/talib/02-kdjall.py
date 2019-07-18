#!/usr/bin/env python
# coding=utf8
# ===============================================================================
#   Copyright (C) 2019 www.361way.com site All rights reserved.
#   
#   Filename      ：02-kdjall.py
#   Author        ：yangbk <itybku@139.com>
#   Create Time   ：2019-07-17 19:26
#   Description   ：
# ===============================================================================
import talib as ta
import tushare as ts
import pandas as pd

def Get_Stock_List():
    df = ts.get_stock_basics()
    return df

def Get_KDJ(code):
  dw = ts.get_k_data(code)
  # 排除新股
  if len(dw) > 60:
    dw = dw[-56:]
    dw.index = range(len(dw))
    dw['slowk'], dw['slowd'] = ta.STOCH(dw['high'].values,
                            dw['low'].values,
                            dw['close'].values,
                            fastk_period=9,
                            slowk_period=3,
                            slowk_matype=0,
                            slowd_period=3,
                            slowd_matype=0)

    df = pd.DataFrame(data=dw)   
    #row = df.iloc[-10:].values
    v1 = df.iloc[-1].values
    v2 = df.iloc[-2].values
    k1,d1 = v1[-2:]
    k2,d2 = v2[-2:]
    if (k2 < 22) and (d2 < 22) and (k1 > d1) and (k1 > k2) and (d1 > d2) and (k1 < 35):
      return(code)

codes = []
df = Get_Stock_List()
for code in df.index:
  print('check ' + code + '  kdj now:') 
  kcode = Get_KDJ(code)
  if kcode != None:
     codes.append(kcode)
print(codes)
