from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.set_page_load_timeout(60)
driver.implicitly_wait(15)

# First Tab
driver.get("https://www.baidu.com")
oldtab = driver.current_window_handle
print driver.title
time.sleep(3)

# Second Tab
driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + "t")
driver.get("http://mirrors.aliyun.com/")
newtab = driver.current_window_handle
print driver.title
time.sleep(3)

# Go back to First Tab
driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + Keys.PAGE_UP)
driver.switch_to_window(oldtab)
print driver.title
driver.refresh()
time.sleep(3)

# Go to Second Tab again
driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + Keys.PAGE_UP)
driver.switch_to_window(newtab)
print driver.title
time.sleep(3)

driver.close()
