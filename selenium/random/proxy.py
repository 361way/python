# -*- coding:utf-8 -*-
import os,time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def startFirefox():

    profile = webdriver.FirefoxProfile()
    '''
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", "175.155.24.32")
    profile.set_preference("network.proxy.http_port", "808")
    '''
    profile.set_preference("general.useragent.override","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A")
    profile.update_preferences()
    driver = webdriver.Firefox(firefox_profile=profile)
    
    """启动安装在默认位置的Firefox浏览器，并自动转到 百度 首页"""
    #driver = webdriver.Firefox(firefox_binary="D:\\Program Files\\firefox\\firefox.exe")
    driver.delete_all_cookies()
    #driver.execute_script('localStorage.clear();')
    driver.get("http://www.361way.com")
    time.sleep(10)
    #driver.findElement(By.cssSelector("a[href*='trustauth']")).click()
    link = driver.find_element_by_link_text('数安时代')
    link.click()
    time.sleep(10)
    driver.close()
    driver.quit()
    driver = None

def my_proxy(PROXY_HOST,PROXY_PORT):
        fp = webdriver.FirefoxProfile()
        # Direct = 0, Manual = 1, PAC = 2, AUTODETECT = 4, SYSTEM = 5
        print PROXY_PORT
        print PROXY_HOST
        fp.set_preference("network.proxy.type", 1)
        fp.set_preference("network.proxy.http",PROXY_HOST)
        fp.set_preference("network.proxy.http_port",int(PROXY_PORT))
        fp.set_preference("general.useragent.override","whater_useragent")
        fp.update_preferences()
        return webdriver.Firefox(firefox_profile=fp)

# Then call in your code: my_proxy(PROXY_HOST,PROXY_PORT)
def install_proxy(PROXY_HOST,PROXY_PORT):
        fp = webdriver.FirefoxProfile()
        print PROXY_PORT
        print PROXY_HOST
        fp.set_preference("network.proxy.type", 1)
        fp.set_preference("network.proxy.http",PROXY_HOST)
        fp.set_preference("network.proxy.http_port",int(PROXY_PORT))
        fp.set_preference("network.proxy.https",PROXY_HOST)
        fp.set_preference("network.proxy.https_port",int(PROXY_PORT))
        fp.set_preference("network.proxy.ssl",PROXY_HOST)
        fp.set_preference("network.proxy.ssl_port",int(PROXY_PORT))  
        fp.set_preference("network.proxy.ftp",PROXY_HOST)
        fp.set_preference("network.proxy.ftp_port",int(PROXY_PORT))   
        fp.set_preference("network.proxy.socks",PROXY_HOST)
        fp.set_preference("network.proxy.socks_port",int(PROXY_PORT))   
        fp.set_preference("general.useragent.override","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A")
        fp.update_preferences()
        return webdriver.Firefox(firefox_profile=fp)

startFirefox()
