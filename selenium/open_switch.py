import win32gui,win32com.client
#import win32con
from selenium import webdriver
import time

def  Broswer(url,x,y):
    browser = webdriver.Firefox()
    #browser.set_window_size(x, y)
    browser.set_window_size(480, 800)
    browser.get(url)
    browser.set_window_position(x, y)
    #browser.get('https://www.163.com')
    #browser.close()
    #browser.quit()
    

def windowEnumerationHandler(hwnd, top_windows):
    if u"firefox" in win32gui.GetWindowText(hwnd).lower():
       top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))



Broswer('http://www.so.com',0,0)
Broswer('http://www.baidu.com',400,0)
Broswer('http://www.163.com',800,0)

if __name__ == "__main__":

    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    '''for i in top_windows:
        if u"so" in i[1].lower():
            print i
            #w3hd=win32gui.FindWindow('MozillaWindowClass',None)
            #w3hd=win32gui.FindWindow('MozillaWindowClass',i[1])
            #win32gui.MoveWindow(w3hd, 50, 50, 300, 200, True)
            #0:hiddle 1:display  2:min   3:max 
            #win32gui.ShowWindow(w3hd,0)
            #win32gui.ShowWindow(w3hd, win32con.SW_MAXIMIZE)
            

            
            win32gui.ShowWindow(i[0],1)
            win32gui.SetForegroundWindow(i[0])
            
            #break'''
            
    while True:
      for i in top_windows:
        #if u"firefox" in i[1].lower():
        print i 
        time.sleep(3)

        win32gui.ShowWindow(i[0],1)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(i[0])
        shell.SendKeys("^{F5}", 0)
        
        #break
