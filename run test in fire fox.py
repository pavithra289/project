import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service_obj=Service()
driver=webdriver.Firefox(service=service_obj)

driver.get("https://naukri.com")
driver.maximize_window()
time.sleep(6)
driver.refresh()
driver.get("https://www.flipkart.com")
driver.back()
print(driver.title)
driver.close()
