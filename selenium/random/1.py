from selenium import webdriver
driver = webdriver.PhantomJS()
driver.set_window_size(1024, 768)
driver.get('https://www.baidu.com/')
driver.save_screenshot('screen.png')

