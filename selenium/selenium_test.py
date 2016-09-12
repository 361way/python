from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def  Broswer(url,x,y):
    browser = webdriver.Firefox()
    #browser.set_window_size(x, y)
    browser.set_window_size(480, 800)
    browser.get(url)
    browser.set_window_position(x, y)
    #browser.get('https://www.163.com')
    #browser.close()
    #browser.quit()

Broswer('http://www.baidu.com',0,0)
Broswer('http://www.so.com',400,0)







