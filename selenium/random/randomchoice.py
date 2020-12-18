# -*- coding:utf-8 -*-
import random
import os,time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import win32api


pages = ['SSL证书代理','联系我们','登录','注册','SSL证书','公司介绍','证书问题','解决方案','产品价格']

Browser = [
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2595.400 QQBrowser/9.6.10872.400',
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36 QIHU 360EE'
]

dis = [(1600,900),(1440,900),(1366,768),(1360,768)]

def randomFurl():
    with open('siteurl.txt') as f:
        lines = f.read().splitlines()
        return random.choice(lines)

def install_proxy(PROXY_HOST,PROXY_PORT):
        choicebrowser = random.choice(Browser)
        fp = webdriver.FirefoxProfile()
        print PROXY_PORT
        print PROXY_HOST
        fp.set_preference("network.proxy.type", 1)
        fp.set_preference("network.proxy.https",PROXY_HOST)
        fp.set_preference("network.proxy.https_port",int(PROXY_PORT))
        fp.set_preference("network.proxy.ssl",PROXY_HOST)
        fp.set_preference("network.proxy.ssl_port",int(PROXY_PORT))     
        fp.set_preference("general.useragent.override",choicebrowser)
        fp.update_preferences()
        return webdriver.Firefox(firefox_profile=fp)

def display(width,high):
    dm = win32api.EnumDisplaySettings(None, 0)
    dm.PelsWidth = width
    dm.PelsHeight = high
    dm.BitsPerPel = 32
    dm.DisplayFixedOutput = 0
    try:
        win32api.ChangeDisplaySettings(dm, 0)
    except:
        print 'display setting error'


def callpage(page):
    
    link = driver.find_element_by_link_text(page)
    link.click()
    time.sleep(random.randint(5, 40))

#def startFirefox(fromurl,totext):
def startFirefox():
    with open('proxy.txt') as f:         
       lines = f.read().splitlines()
       for ipport in lines:
            ip = ipport.split()[0]
            port = ipport.split()[1]
            driver = install_proxy(ip,port)


            #driver = webdriver.Firefox(firefox_binary="D:\\Program Files\\firefox\\firefox.exe")
            driver.delete_all_cookies()
            #driver.execute_script('localStorage.clear();')
            wh = random.choice(dis)
            width = wh[0]
            high = wh[1]
            display(width,high)

            url = randomFurl()
            print url
            driver.get(url)
            time.sleep(random.randint(5, 20))
            try:
                link = driver.find_element_by_link_text('数安时代')
                link.click()
                time.sleep(random.randint(20, 60))
                
                

                times = random.randint(0,3)
                print times
                for  t in  range(times):
                     page = random.choice(pages)
                     print page
                     driver.switch_to_window(driver.window_handles[-1])
                     print(driver.current_url)
                     link = driver.find_element_by_link_text(page)
                     link.click()
                     time.sleep(random.randint(5, 40))
            except:
                print 'proxy wuxiao!'
            driver.close()
            driver.quit()
            driver = None
            comand = 'taskkill /im WerFault.exe /f'
            os.system(comand)
            

startFirefox()
