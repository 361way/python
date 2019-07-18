#!/usr/bin/env python
# coding=utf8
# ===============================================================================
#   Copyright (C) 2019 www.361way.com site All rights reserved.
#   
#   Filename      ：03-macd.py
#   Author        ：yangbk <itybku@139.com>
#   Create Time   ：2019-07-17 19:47
#   Description   ：
# ===============================================================================
# macd = 12 天 EMA - 26 天 EMA
# signal = 9 天 MACD的EMA
# hist = MACD - MACD signal

import talib as ta
import tushare as ts
import pandas as pd



dw = ts.get_k_data("600600")
dw = dw[-50:]
print(dw)
close = dw.close.values
print(close)
print(len(close))
dw['macd'], dw['macdsignal'], dw['macdhist'] = ta.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)

df = pd.DataFrame(data=dw)   
row = df.iloc[-10:].values
print(row)
