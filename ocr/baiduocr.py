#! /usr/bin/env python                                                                                      
# -*- coding: utf-8 -*-
# desc: 使用百度AI图片识别模板，进行文字识别，每日限制500次

import json
from aip import AipOcr
APP_ID = '11241005'
API_KEY = 'key number'
SECRET_KEY = 'secret key'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('example.jpg')
outdata = client.basicGeneral(image)
for line in  outdata['words_result']:
    print line['words']

#jsdata =  json.dumps(outdata,indent=4,encoding='utf-8')
#print jsdata['words_result']
