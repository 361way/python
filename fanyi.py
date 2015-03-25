#!/usr/bin/python
#coding=utf-8
import pycurl
import StringIO
import json
import sys



def FanYi(words):
	c = pycurl.Curl()
	buf = StringIO.StringIO()
        Url = "http://openapi.baidu.com/public/2.0/bmt/translate?client_id=PGcC40pcK5PVqN87d9VwfcXj&q=" + words + "&from=auto&to=auto"
	#c.setopt(pycurl.URL, "http://openapi.baidu.com/public/2.0/bmt/translate?client_id=PGcC40pcK5PVqN87d9VwfcXj&q=today&from=auto&to=auto")
	c.setopt(pycurl.URL, Url)
	c.setopt(pycurl.WRITEFUNCTION, buf.write)
	c.perform()
	data = buf.getvalue()
	#jdata = json.loads(data,encoding='utf-8')
	jdata = json.loads(data,encoding='utf-8')
	print json.dumps(jdata,ensure_ascii=False,indent=2)


if len(sys.argv) < 2:
    print 'No anything input ,please input your word'
    sys.exit()

else :
    words = '%0A'.join(sys.argv[1:])
    FanYi(words)
    sys.exit()

