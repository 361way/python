#!/usr/bin/python
#-*- coding: utf-8 -*-
# code by www.361way.com <yangbk>
# mail:itybku@139.com
import sys
import json
import time,random
import base64
import requests
import argparse

x = []
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


def splitx(path):
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
    return x

def encrypt_ba64(s):
    s1 = base64.encodestring(str(s))
    s2 = encrypt(keynumb,s1.strip())
    return s2

def dkey(ss):
    #ss = 'PEIHGHJHOECEGHJHPEFFMELHPELHAFCDPEFFAFCDPEFFAEGHLA'
    s1 = decrypt(1,ss)
    a,b,nowtime = (base64.decodestring(s1)).split(',')

    x = splitx('key.txt')
    c = x[int(a)][int(b)]
    keynot = int(nowtime) + int(a) + int(b) + long(c)

    dv1 = base64.encodestring(str(keynot))
    dv2 = encrypt(keynumb,dv1.strip())
    return dv2


def gresult(url,cmd):
    authdata = {"fastech":"MEFEAEGHMEAFMDMD"}
    u1 = url + '/login' 
    r = requests.post(u1, data = json.dumps(authdata))
    ss = r.text
    key = dkey(ss)
    #pdata = {"d":dkey,"cmd":"LFGFPEOGDGIHAEIGEFMGHFLHFGGFJHBDOELGAFGGIEIGAEGDLFPGLENGLFCFAEFHDGCFLFKGLFIGAEFHAGFECHGGLFGFPEOGDGIHAEIGOEIHIEMD","key":"1"}
    
    cmdx = encrypt_ba64(cmd)
    pdata = {"d":key,"cmd":cmdx,"key":"1"}
    u2 = url + '/cmd'
    r = requests.post(u2, data = json.dumps(pdata))
    return r.text

#url = 'http://200.200.16.8:8899'
#cmd = 'free -m && df -hl'
#print gresult(url,cmd)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Run command use hailuo agent")
  parser.add_argument("--port",help="Please enter the port of the target host(default:8899)",type=int,default=8899)
  parser.add_argument("-c","--cmd", help="Input the commands to be executed",metavar="")
  parser.add_argument("-i", help="Input the host to be executed",metavar='IPaddress')
  parser.add_argument("-f",help="Hosts information, including the URL of the host and port,one line example: http://192.168.0.1:8899",type=file,metavar="filename")
  args = parser.parse_args()
  if args.i and args.cmd:
    url = 'http://' + args.i + ':' + str(args.port)
    cmd = args.cmd
    print gresult(url,cmd)
  elif args.f and args.cmd:
    for url in args.f.readlines():
        url = url.strip()
        ip = url.split(':')[1]
        ip = ip.split('/')[2]
        print ip
        print '='*50
        print gresult(url,args.cmd) + '\n'
  else:
    parser.print_help()
