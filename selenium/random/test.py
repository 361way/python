# -*- coding:utf-8 -*-

import random
import os,time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

pages = ['SSL证书代理','联系我们','登录','注册','SSL证书','公司介绍','证书问题','解决方案','产品价格']

Browsers = [
'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
]

def randomurl():
    with open('siteurl.txt') as f:
        lines = f.read().splitlines()
        return random.choice(lines)


def callpage(page):
    link = driver.find_element_by_link_text('page')
    link.click()
    time.sleep(random.randint(5, 40))
    

def startFirefox(fromurl):


    choicebrowser = random.choice(Browsers)
    print choicebrowser
    
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override",choicebrowser)
    profile.update_preferences()
    driver = webdriver.Firefox(firefox_profile=profile)
    
    """启动安装在默认位置的Firefox浏览器，并自动转到 百度 首页"""
    #driver = webdriver.Firefox(firefox_binary="D:\\Program Files\\firefox\\firefox.exe")
    driver.delete_all_cookies()
    #driver.execute_script('localStorage.clear();')
    driver.get(fromurl)
    time.sleep(random.randint(5, 20))
    #driver.findElement(By.cssSelector("a[href*='trustauth']")).click()
    link = driver.find_element_by_link_text('数安时代')
    link.click()
    time.sleep(random.randint(5, 40))
    driver.switch_to_window(driver.window_handles[-1])
    link = driver.find_element_by_link_text('首页')
    link.click()
    time.sleep(random.randint(5, 40))
    
    driver.close()
    driver.quit()
    driver = None


url = randomurl()
print url
startFirefox(url)
