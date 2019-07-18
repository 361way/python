#!/usr/bin/env python
# coding=utf8
# ===============================================================================
#   Copyright (C) 2019 www.361way.com site All rights reserved.
#   
#   Filename      ：kdj.py
#   Author        ：yangbk <itybku@139.com>
#   Create Time   ：2019-07-17 19:25
#   Description   ：
# ===============================================================================
import talib as ta
import tushare as ts
import pandas as pd



dw = ts.get_k_data("603236")
print(len(dw))
dw = dw[300:]
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
row = df.iloc[-10:].values
print(row)


   
"""slowkMA5 = ta.MA(slowk, timeperiod=5, matype=0)
slowkMA10 = ta.MA(slowk, timeperiod=10, matype=0)
slowkMA20 = ta.MA(slowk, timeperiod=20, matype=0)
slowdMA5 = ta.MA(slowd, timeperiod=5, matype=0)
slowdMA10 = ta.MA(slowd, timeperiod=10, matype=0)
slow
"""
