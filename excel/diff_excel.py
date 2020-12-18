#!/usr/bin/env python
# coding=utf8
# ===============================================================================
#   Copyright (C) 2020 www.361way.com site All rights reserved.
#   
#   Filename      ：diff_excel.py
#   Author        ：yangbk <itybku@139.com>
#   Create Time   ：2020-02-16 21:57
#   Description   ：
# ===============================================================================
import sys
import pandas as pd
from pathlib import Path


def diff_excel(file1,file2,keyname):
  #define parameters
  #path to files
  #path_old=Path(r'01.xlsx')
  #path_new=Path(r'02.xlsx')

  path_old=Path(file1)
  path_new=Path(file2)
  #list of key column(s)
  #key=['电话']
  key=[str(keyname)]
  #sheets to read in
  sheet='Sheet1'

  # Read in the two excel files and fill NA
  old = pd.read_excel(path_old).fillna(0)
  new = pd.read_excel(path_new).fillna(0)
  #set index
  old=old.set_index(key)
  new=new.set_index(key)

  #identify dropped rows and added (new) rows
  dropped_rows = set(old.index) - set(new.index)
  added_rows = set(new.index) - set(old.index)

  #combine data
  df_all_changes = pd.concat([old, new], axis='columns', keys=['old','new'], join='inner')

  #prepare functio for comparing old values and new values
  def report_diff(x):
      return x[0] if x[0] == x[1] else '{} ---> {}'.format(*x)

  #swap column indexes
  df_all_changes = df_all_changes.swaplevel(axis='columns')[new.columns[0:]]

  #apply the report_diff function
  df_changed = df_all_changes.groupby(level=0, axis=1).apply(lambda frame: frame.apply(report_diff, axis=1))

  #create a list of text columns (int columns do not have '{} ---> {}')
  df_changed_text_columns = df_changed.select_dtypes(include='object')

  #create 3 datasets:
  #diff - contains the differences
  #dropped - contains the dropped rows
  #added - contains the added rows
  diff = df_changed_text_columns[df_changed_text_columns.apply(lambda x: x.str.contains("--->") == True, axis=1)]
  dropped = old.loc[dropped_rows]
  added = new.loc[added_rows]


  #create a name for the output excel file
  fname =  '{}-vs-{}.xlsx'.format(path_old.stem, path_new.stem)

  #write dataframe to excel
  writer=pd.ExcelWriter(fname, engine='xlsxwriter')
  #diff.to_excel(writer, sheet_name='diff', index=True)
  df_changed_text_columns.to_excel(writer, sheet_name='diff', index=True)
  dropped.to_excel(writer, sheet_name='dropped', index=True)
  added.to_excel(writer, sheet_name='added', index=True)

  #get xlswriter objects
  workbook = writer.book
  worksheet = writer.sheets['diff']
  worksheet.hide_gridlines(2)
  worksheet.set_default_row(15)

  #get number of rows of the df diff
  row_count_str=str(len(diff.index)+1)

  #define and apply formats
  highligt_fmt = workbook.add_format({'font_color': '#FF0000', 'bg_color':'#B1B3B3'})
  worksheet.conditional_format('A1:ZZ'+row_count_str, {'type':'text', 'criteria':'containing', 'value':'--->',
                              'format':highligt_fmt})

  #save the output
  writer.save()
  print ('\nDone.\n')


def usage():
  print("Need three argvs to input:filename1  filename2  keyname")
  print("For example:")
  print("\t" + sys.argv[0] + "\t a.xlsx  b.xlsx  phonenum")


def main():
  if len(sys.argv) != 4:    
      usage()
      sys.exit()

  diff_excel(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == '__main__':
  main()
