# -*- coding:utf-8 -*-
import random
import os,time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pages = ['SSL证书代理','联系我们','登录','注册','SSL证书','公司介绍','证书问题','解决方案','产品价格']

Browser = [
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2595.400 QQBrowser/9.6.10872.400'
]


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


def callpage(page):
    
    link = driver.find_element_by_link_text(page)
    link.click()
    time.sleep(random.randint(5, 40))

#def startFirefox(fromurl,totext):
def startFirefox(fromurl):
    profile = webdriver.FirefoxProfile()
    '''
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", "175.155.24.32")
    profile.set_preference("network.proxy.http_port", "808")
    '''
    choicebrowser = random.choice(Browser)
    print choicebrowser
    profile.set_preference("general.useragent.override",choicebrowser)
    profile.update_preferences()
    driver = webdriver.Firefox(firefox_profile=profile)
    
    """启动安装在默认位置的Firefox浏览器，并自动转到 百度 首页"""
    #driver = webdriver.Firefox(firefox_binary="D:\\Program Files\\firefox\\firefox.exe")
    driver.delete_all_cookies()
    #driver.execute_script('localStorage.clear();')
    driver.get(fromurl)
    time.sleep(random.randint(5, 20))
    link = driver.find_element_by_link_text('数安时代')
    link.click()
    time.sleep(random.randint(5, 40))
    
    

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

    driver.close()
    driver.quit()
    driver = None


'''
print random.choice(pages) 
random.randint(0, 3)
'''
url = randomFurl()
print url
startFirefox(url)
