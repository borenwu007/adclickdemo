from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import zipfile
import time 
from get_random_link import get_link

file_name = 'links.txt'
class_name = 'ad_link'

while(1):
    try:
        link = get_link(file_name)
        driver = webdriver.Chrome()
        driver.get(link)
        time.sleep(1)

        driver.switch_to.frame(0)
        elem = WebDriverWait(driver,100).until(lambda dirver:driver.find_element_by_class_name(class_name))
        elem.click()
        time.sleep(5)
        driver.quit()
    except:
        print("未知异常")
        driver.quit()
