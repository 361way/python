#!/usr/bin/env python
# coding=utf-8
import socket,time
def tcping(server, port):
    ''' Check if a server accepts connections on a specific TCP port '''
    try:
        start = time.time()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server, port))
        s.close()
        #print server + ':' + str(port) + '/tcp - ' +  str(port) + ' port is open' + ' - time=' + str(round((time.time()-start)*10000)/10) + 'ms'
        print server + ':' + str(port) + '/tcp - ' +  str(port) + ' port is open' + ' - time=' + str((time.time()-start)*1000) + 'ms'
    except socket.error:
        print str(port) + ' port not open'

while 1:
    tcping('192.168.52.252',6556)
    time.sleep(1)
