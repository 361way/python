#!/usr/bin/env python
# coding=utf8
# ===============================================================================
#   Copyright (C) 2019 www.361way.com site All rights reserved.
#   
#   Filename      ：04-macdall.py
#   Author        ：yangbk <itybku@139.com>
#   Create Time   ：2019-07-18 17:28
#   Description   ：
# ===============================================================================
import talib as ta
import tushare as ts
import pandas as pd

def Get_Stock_List():
    df = ts.get_stock_basics()
    return df

def Get_MACD(code):
  dw = ts.get_k_data(code)
  if len(dw) > 60:
    dw = dw[-56:]
    close = dw.close.values
    dw['macd'], dw['macdsignal'], dw['macdhist'] = ta.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
    
    df = pd.DataFrame(data=dw)   
    row3,row2,row1 = df.iloc[-3:].values
    md1,mds1,mdh1 = row1[-3:]
    md2,mds2,mdh2 = row2[-3:]
    md3,mds3,mdh3 = row3[-3:]
    if (md3< md2 <md1) and ( -0.4 < md1) and (mdh2 < mdh1):
        return code

codes = []
df = Get_Stock_List()
for code in df.index:
  print('check ' + code + '  macd now:') 
  mcode = Get_MACD(code)
  if mcode != None:
     codes.append(mcode)
  
print(codes)
print(len(codes))
