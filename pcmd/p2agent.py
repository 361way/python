#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import cgi
import urllib
import os
import commands
import threading
import json
import thread,time,random
import base64
import ConfigParser
import logging
import logging.handlers
LOG_FILE = 'agent.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5)
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)
logger = logging.getLogger('python')
logger.addHandler(handler)
logger.setLevel(logging.INFO)
BBH='1.0.0.0'
x = []
alist=[]
blist=[]
keynumb=1
def encrypt(key, s):
            b = bytearray(str(s).encode("gbk"))
            n = len(b)
            c = bytearray(n*2)
            j = 0
            for i in range(0, n):
                b1 = b[i]
                b2 = b1 ^ key
                c1 = b2 % 16
                c2 = b2 // 16
                c1 = c1 + 65
                c2 = c2 + 65
                c[j] = c1
                c[j+1] = c2
                j = j+2
            return c.decode("gbk")
def decrypt(key, s):
    c = bytearray(str(s).encode("gbk"))
    n = len(c)
    if n % 2 != 0 :
        return ""
    n = n // 2
    b = bytearray(n)
    j = 0
    for i in range(0, n):
        c1 = c[j]
        c2 = c[j+1]
        j = j+2
        c1 = c1 - 65
        c2 = c2 - 65
        b2 = c2*16 + c1
        b1 = b2^ key
        b[i]= b1
    try:
        return b.decode("gbk")
    except:
        return "failed"
#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):

    def re_send_response(self, code, message=None):
        #===================recode send_responses=====================

        if message is None:
            if code in self.responses:
                message = self.responses[code][0]
            else:
                message = ''
        if self.request_version != 'HTTP/0.9':
            self.wfile.write("%s %d %s\r\n" %
                     (self.protocol_version, code, message))
        self.send_header('Server', self.version_string())
        self.send_header('Date', self.date_time_string())
        #===================recode send_responses end=====================
        return
    #Handler for the GET requests
    def do_POST(self):
        def do_time(self):
            if self.path=='/cmd':
                mpath,margs=urllib.splitquery(self.path)
                datas = self.rfile.read(int(self.headers['content-length']))
                z=0
                dictinfo = json.loads(datas)
                s3= base64.decodestring(decrypt(keynumb,dictinfo['d']))
                ls3=long(s3)
                if  d.has_key(ls3) :
                         z=1
                         del d[ls3]
                if z==True :
                    s2=base64.decodestring(decrypt(keynumb,dictinfo['cmd']))
                    if s2=='packagemanager':
                         self.re_send_response(200)
                         self.send_header('Content-type','text/html')
                         self.end_headers()
                         setlf.wfile.write(BBH)
                         return
                    (status, output) = commands.getstatusoutput(s2)
                    print output
                    self.re_send_response(200)
                    self.send_header('Content-type','text/html')
                    self.end_headers()
                    print 'success'
                    self.wfile.write(output)
                    return
                self.re_send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write('Result:8 yanzhenshibai')

                # Send the html message
                return

            if self.path=='/login':
                mpath,margs=urllib.splitquery(self.path)
                datas = self.rfile.read(int(self.headers['content-length']))
                dictinfo = json.loads(datas)
                login= base64.decodestring(decrypt(keynumb,dictinfo['fastech']))
                if login=='0001':
                      a=random.randint(0, 30)
                      b=random.randint(0, 30)
                      num=str(a)
                      num1=str(b)
                      c=x[a][b]
                      cl=long(c)
                      nowtime=long(time.time() * 1000)
                      keynot=nowtime+a+b+cl
                      num3=str(nowtime)
                      d[keynot]=nowtime
                      self.re_send_response(200)
                      self.send_header('Content-type','text/html')
                      self.end_headers()
                      str2=num+','+num1+','+num3
                      s1= base64.encodestring(str2)
                      s3=encrypt(keynumb,s1)
                      self.wfile.write(s3)
                      return
                if login=='0000':
                      self.re_send_response(200)
                      self.send_header('Content-type','text/html')
                      self.end_headers()
                      self.wfile.write('OK')
                      return
                self.re_send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write('false')
                return
        do_time(self)
        return







try:
    #Create a web server and define the handler to manage the
    #incoming request
    cp = ConfigParser.SafeConfigParser()
    print os.path.dirname(os.path.abspath("p2agent.py"))
    cp.read(os.path.dirname(os.path.abspath("p2agent.py"))+'//config.conf')
    PORT_NUMBER =int(cp.get("db","PORT_NUMBER"))
    IP=cp.get("db","IP")
    server = HTTPServer((IP, PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER
    d = {}
    keynumb=int(cp.get("db","key"))
    def fun_timer():
        list =[]
        for i in d:
            if long(time.time() * 1000)-d[i]>600000 :
               list.append(i)
        print '--'
        logger.info('I am ok')
        for i, val in enumerate(list):
           del d[val]
        global timer
        timer = threading.Timer(300, fun_timer)
        timer.start()
    path = cp.get("db","path")
    f = open(path)
    s3=f.read().strip()
    s= base64.decodestring(s3)
    x = []
    tag_list=s[:-1]
    tag_list1=(tag_list.split(']'))
    for colour in tag_list1:
        colour=colour[:-1]
        tag_list2=colour.split(',')
        x.append(tag_list2)
    logger.info(s)
    timer = threading.Timer(300, fun_timer)
    timer.start()
    logger.info('startup successful PORT')
    logger.info(PORT_NUMBER)
    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()