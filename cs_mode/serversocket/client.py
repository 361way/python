#!/usr/bin/env python
# coding=utf8
import commands
import time
import os
import socket
import pickle
def get_ip():
        ip={}
        status,interface = commands.getstatusoutput("ifconfig -s|grep -v Iface|grep -v lo |awk '{print $1}'")
        inface = interface.split('\n')
        for i in range(len(inface)):
                var=inface[i]
                os.environ['var']=str(var)
                status,inter_ip=commands.getstatusoutput("ifconfig `echo $var`|sed -n 2p|awk  '{ print $2 }'|awk -F : '{ print $2 }'")
                ip[inface[i]]=inter_ip
        return ip
  
  
#if __name__ == '__main__':
MonitorData=pickle.loads(pickle.dumps(get_ip()))
#        local_file = file('/tmp/monitor_data.pickle','w')
#        pickle.dump(ip_data,local_file)
 
 
 
def UpTime():
    Uptime = time.strftime('%Y-%m-%d %H:%M:%S')
    return Uptime
 
 
def Write_local_data():
    try:
        local_file = file('/tmp/monitor_data.pickle','w')
        pickle.dump(MonitorData,local_file)
    except IOError:
        print "Write Error"
 
def check_local_data():
    try:
        local_file = file('/tmp/monitor_data.pickle')
        local_data = pickle.load(local_file)
        print local_data
    except EOFError:
        Write_local_data()
        print 'Write monitor to file'
        return False
    if MonitorData == local_data:
        Update = {}
        Update['Uptime'] = UpTime()
        return Update
    else:
        Write_local_data()
        return False
 
 
 
 
 
def SendMonitorData():
 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.0.103', 9999))
    check_data = check_local_data()
    print check_data
    if check_data is False:
        MonitorData['Uptime'] = UpTime()
        monitor_data = pickle.dumps(MonitorData)
        while True:
            s.sendall('InsertData')
            data = s.recv(1024)
            if data == 'ReadyToReceiveFile':
                s.sendall(monitor_data)
                time.sleep(30)
                s.sendall('DataSendDone')
                break
        s.close()
 
    else:
        monitor_data = pickle.dumps(check_data)
        print monitor_data
        while True:
            s.sendall('UpdateData')
            data = s.recv(1024)
            if data == 'ReadyToReceiveFile':
                s.sendall(monitor_data)
                time.sleep(30)
                s.sendall('DataSendDone')
                break
        s.close()
 
if __name__ == '__main__':
    SendMonitorData()
