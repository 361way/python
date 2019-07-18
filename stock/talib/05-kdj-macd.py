#!/usr/bin/env python
# coding=utf8
# ===============================================================================
#   Copyright (C) 2019 www.361way.com site All rights reserved.
#   
#   Filename      ：05-kdj-macd.py
#   Author        ：yangbk <itybku@139.com>
#   Create Time   ：2019-07-18 17:30
#   Description   ：
# ===============================================================================
import talib as ta
import tushare as ts
import pandas as pd

def Get_Stock_List():
    df = ts.get_stock_basics()
    return df

def K_Data(code):
  dw = ts.get_k_data(code)
  # 排除新股
  if len(dw) > 51:
    dw = dw[-50:]
    return dw

def Get_KDJ(dw):
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
      
def Get_MACD(dw):
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
  print('check ' + code + '  kdj and macd now:') 
  dw = ts.get_k_data(code)
  # 排除新股
  if len(dw) > 60:
     dw = dw[-56:]
     kcode = Get_KDJ(dw)
     mcode = Get_MACD(dw)
     if (kcode != None) and (mcode != None):
        codes.append(code)
print(codes)
print(len(codes))

df = ts.get_realtime_quotes(codes)
#print(df)
#print(df[['code','name','price','bid','ask','volume','amount','time']])
print(df[['code','name','price','low','high','time']])
