#!/usr/bin/env python
import multiprocessing
import os,sys
import SocketServer,time
import pickle
 
 
 
class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
            print 'got a connection from:',self.client_address[0]
            self.data = self.request.recv(1024).strip()
            if not self.data:
                    print 'Client is disconnected...',self.client_address[0]
            if self.data == 'InsertData':
                    print self.data
                    print "going to receive date",self.data
                    self.request.send('ReadyToReceiveFile')
                    data = self.request.recv(4096)
                    if data == 'DataSendDone':
                            print 'Transfer is done.'
                    else:
                            Monitor_data = data
                            Monitor_data = pickle.loads(Monitor_data)
                            print Monitor_data
#                                mysql.InsertData(Monitor_data)
                            print "INserDatadone"
            if self.data == 'UpdateData':
                    print "going to receive date",self.data
                    self.request.send('ReadyToReceiveFile')
                    data = self.request.recv(4096)
                    print data
                    if data == 'DataSendDone':
                            print 'Transfer is done.'
                    else:
                            Monitor_data = data
                            Monitor_data = pickle.loads(Monitor_data)
#                                mysql.UpdateData(Monitor_data)
                            print 'updatedone......'

 
if __name__ == "__main__":
 
        HOST,PORT = "",9999
        server = SocketServer.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
        jobs=[]
        for i in range(3):
                server_thread = multiprocessing.Process(target=server.serve_forever)
                server_thread.daemon = True
                jobs.append(server_thread)
                server_thread.start()
                time.sleep(1)
          
        for j in jobs:
                j.join()
