# -*- coding:utf-8 -*-
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
练习启动各种浏览器：Firefox， Chrome， IE
练习启动各种浏览器的同时加载插件：Firefox， Chrome， IE
"""

def startFirefox():
    """启动安装在默认位置的Firefox浏览器，并自动转到 百度 首页"""
    driver = webdriver.Firefox()
    driver.get("http://www.baidu.com")
    assert("百度" in driver.title)
    elem = driver.find_element_by_name("wd")
    elem.send_keys("selenium")
    elem.send_keys(Keys.RETURN)
    assert "百度" in driver.title
    driver.close()
    driver.quit()
    driver = None
    
def startFirefoxWithSpecificLocation():
    """启动安装在 非 默认位置的Firefox浏览器，并自动转到 百度 首页"""
    firefoxBin = os.path.abspath(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
    os.environ["webdriver.firefox.bin"] = firefoxBin
    
    driver = webdriver.Firefox()
    driver.get("http://www.baidu.com")
    assert("百度" in driver.title)
    elem = driver.find_element_by_name("wd")
    elem.send_keys("selenium")
    elem.send_keys(Keys.RETURN)
    assert "百度" in driver.title
    driver.close()
    driver.quit()
    driver = None

    
def startChrome():
    """启动Chrome浏览器，并自动转到 百度 首页
    启动Chrome浏览器需要指定驱动的位置
    """
    chrome_driver = os.path.abspath(r"D:\云盘\360云\360云盘\我的自动双向同步文件夹\01-PersonalInfo\DataGuru\12-软件自动化测试Selenium2\1-课程\练习代码_Python版本\Selenium_python\Files\chromedriver.exe")
    os.environ["webdriver.chrome.driver"] = chrome_driver
    
    driver = webdriver.Chrome(chrome_driver)
    driver.get("http://www.baidu.com")
    assert("百度" in driver.title)
    elem = driver.find_element_by_name("wd")
    elem.send_keys("selenium")
    elem.send_keys(Keys.RETURN)
    assert "百度" in driver.title
    driver.close()
    driver.quit()
    driver = None

def startIE():
    """启动IE浏览器，并自动转到 百度 首页
    启动 IE 浏览器需要指定驱动的位置
    """
    ie_driver = os.path.abspath(r"D:\云盘\360云\360云盘\我的自动双向同步文件夹\01-PersonalInfo\DataGuru\12-软件自动化测试Selenium2\1-课程\练习代码_Python版本\Selenium_python\Files\IEDriverServer.exe")
    os.environ["webdriver.ie.driver"] = ie_driver
    
    driver = webdriver.Ie(ie_driver)
    driver.get("http://www.python.org")
    assert("Python" in driver.title)
    elem = driver.find_element_by_id("id-search-field")
    elem.send_keys("selenium")
    '''
    elem.send_keys(Keys.RETURN)
    assert "百度" in driver.title
    driver.close()
    driver.quit()
    driver = None    
    ''' 
    

def start_firefox_with_firebug_plug():
    """启动Firefox，并自动加载插件Firebug"""
    firefoxBin = os.path.abspath(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
    os.environ["webdriver.firefox.bin"] = firefoxBin
    
    firefoxProfile = webdriver.FirefoxProfile()
    tempDir = os.getcwd()
    tempDir = os.path.split(tempDir)[0]
    firebugPlugFile = os.path.join(os.path.join(tempDir,"Files"), "firebug-2.0.7.xpi")    
    firefoxProfile.add_extension(firebugPlugFile)
    firefoxProfile.set_preference("extensions.firebug.currentVersion", "2.0.7")
    
    driver = webdriver.Firefox(firefox_profile=firefoxProfile)
    driver.get("http://www.baidu.com")

def start_chrome_with_chrometomobile_plug():
    """启动Chrome，并自动加载插件Chrome to Mobile"""
    tempDir = os.getcwd()
    tempDir = os.path.split(tempDir)[0]
    chrome_driver_file = os.path.join(os.path.join(tempDir,"Files"), "chromedriver.exe")        
    os.environ["webdriver.chrome.driver"] = chrome_driver_file
    
    chrome_to_mobile_plug_file =  os.path.join(os.path.join(tempDir,"Files"), "Chrome-to-Mobile_v3.3.crx")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_extension(chrome_to_mobile_plug_file)
    driver = webdriver.Chrome(executable_path=chrome_driver_file, 
                             chrome_options=chrome_options)
    driver.get("http://www.baidu.com")
    '''
    driver.close()
    driver.quit()
    driver = None
    '''

def start_firefox_with_default_settings():
    """启动Firefox浏览器， 使用本地配置文件中的选项配置浏览器
    自动将页面载入过程导出为Har文件，并存放在
    配置项 extensions.firebug.netexport.defaultLogDir指定的D:\temp\selenium2目录下    
    """
    firefox_bin = os.path.abspath(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")
    os.environ["webdriver.firefox.bin"] = firefox_bin
    
    # 使用从别的机器上拷贝来的浏览器配置
    firefox_profile = webdriver.FirefoxProfile(os.path.abspath(r"D:\Temp\selenium2\Profiles\mm9zxom8.default"))
    # 使用本地的默认配置
    #firefox_profile = webdriver.FirefoxProfile(r"C:\Users\eli\AppData\Roaming\Mozilla\Firefox\Profiles\mm9zxom8.default")
    driver = webdriver.Firefox(firefox_profile=firefox_profile)
    driver.get("http://www.baidu.com")
    driver.get("http://www.baidu.com")
    '''
    driver.close()
    driver.quit()
    driver = None
    '''

def start_chrome_with_default_settings():
    """启动Firefox浏览器， 使用本地配置文件中的选项配置浏览器"""
    tempDir = os.getcwd()
    tempDir = os.path.split(tempDir)[0]
    chrome_driver = chrome_driver_file = os.path.join(os.path.join(tempDir,"Files"), "chromedriver.exe")        
    os.environ["webdriver.chrome.driver"] = chrome_driver
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--test-type")
    #chrome_options.add_argument("user-data-dir="+os.path.abspath(r"D:\Temp\selenium2\User Data"))
    chrome_options.add_argument("user-data-dir="+os.path.abspath(r"C:\Users\eli\AppData\Local\Google\Chrome\User Data"))
    driver = webdriver.Chrome(executable_path=chrome_driver, 
                             chrome_options=chrome_options)
    driver.get("http://www.baidu.com")
    
    
if __name__ == "__main__":  
    # 2.启动浏览器时自动加载插件， 如Firefox -> Firebug ; Chrome -> Chrome to Mobile
    # start_firefox_with_firebug_plug()
    # start_chrome_with_chrometomobile_plug()
    # start_firefox_with_default_settings()
    start_chrome_with_default_settings()
    
    
    # 1.启动各种浏览器
    #startFirefox()
    #startFirefoxWithSpecificLocation()
    #startChrome()
    #startIE()   
