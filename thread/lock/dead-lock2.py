import threading
import time

class MyThread(threading.Thread):
    def do1(self):
        global resA, resB
        if mutexA.acquire():
             msg = self.name+' got resA'
             print msg
             
             if mutexB.acquire(1):
                 msg = self.name+' got resB'
                 print msg
                 mutexB.release()
             mutexA.release()
    def do2(self):
        global resA, resB
        if mutexB.acquire():
             msg = self.name+' got resB'
             print msg
             
             if mutexA.acquire(1):
                 msg = self.name+' got resA'
                 print msg
                 mutexA.release()
             mutexB.release()
 
    
    def run(self):
        self.do1()
        self.do2()
resA = 0
resB = 0

mutexA = threading.Lock()
mutexB = threading.Lock()

def test():
    for i in range(5):
        t = MyThread()
        t.start()
if __name__ == '__main__':
    test()
