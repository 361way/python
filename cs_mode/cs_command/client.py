#!/usr/bin/env python
import socket,os,sys
#host=sys.argv[1]
port=4567
for host in os.popen('cat ip.list').readlines():
  print host
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.connect((host,port))
  while 1:
    data=sys.argv[2]
    if not data:
        break
    s.sendall(data)
    data=s.recv(1024)
    if not data:
        break
    print data
  s.close()
