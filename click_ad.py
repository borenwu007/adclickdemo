from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import zipfile
import time 
# from get_random_link import get_link

class_name = 'ad_link'
 
driver = webdriver.Chrome()
driver.get("http://taotuman.com/2019/12/10/blog-entry-1395.html")
time.sleep(1)

driver.switch_to.frame(0)
elem = WebDriverWait(driver,100).until(lambda dirver:driver.find_element_by_class_name(class_name))
elem.click()
time.sleep(2)
driver.quit()
