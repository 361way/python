#coding:utf-8
import threading
import time
cond = threading.Condition()
class kongbaige(threading.Thread):
    def __init__(self, cond, diaosiname):
        threading.Thread.__init__(self, name = diaosiname)
        self.cond = cond
           
    def run(self):
        self.cond.acquire() #获取锁
           
        print self.getName() + ':一支穿云箭'  #空白哥说的第一句话
        self.cond.notify()                   #唤醒其他wait状态的线程(通知西米哥 让他说话)
        #然后进入wait线程挂起状态等待notify通知(等西米哥的回复，接下来俩人就开始扯蛋)
        self.cond.wait()
           
        print self.getName() + ':山无棱，天地合，乃敢与君绝!'
        self.cond.notify()
        self.cond.wait()
           
        print self.getName() + ':紫薇！！！！(此处图片省略)'
        self.cond.notify()
        self.cond.wait()
           
        print self.getName() + ':是你'
        self.cond.notify()
        self.cond.wait()
           
        #这里是空白哥说的最后一段话，接下来就没有对白了
        print self.getName() + ':有钱吗 借点'
        self.cond.notify()             #通知西米哥
        self.cond.release()            #释放锁
           
           
           
class ximige(threading.Thread):
    def __init__(self, cond, diaosiname):
        threading.Thread.__init__(self, name = diaosiname)
        self.cond = cond
           
    def run(self):
        self.cond.acquire()
        self.cond.wait()   #线程挂起(等西米哥的notify通知)
           
        print self.getName() +':千军万马来相见'
        self.cond.notify()  #说完话了notify空白哥wait的线程
        self.cond.wait()    #线程挂起等待空白哥的notify通知
           
        print self.getName() + ':海可枯，石可烂，激情永不散！'
        self.cond.notify()
        self.cond.wait()
           
        print self.getName() + ':尔康！！！(此处图片省略)'
        self.cond.notify()
        self.cond.wait()
           
        print self.getName() + ':是我'
        self.cond.notify()
        self.cond.wait()
           
        #这里是最后一段话，后面空白哥没接话了 所以说完就释放锁 结束线程
        print self.getName() + ':滚' 
        self.cond.release()
           
           
kongbai = kongbaige(cond, '    ')
ximi = ximige(cond, '西米')
#尼玛下面这2个启动标志是关键，虽然是空白哥先开的口，但是不能让他先启动，
#因为他先启动的可能直到发完notify通知了，西米哥才开始启动，
#西米哥启动后会一直处于44行的wait状态，因为空白哥已经发完notify通知了进入wait状态了，
#而西米哥没收到
#造成的结果就是2根线程就一直在那挂起，什么都不干，也不扯蛋了
ximi.start()
kongbai.start()
