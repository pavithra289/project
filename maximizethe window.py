from datetime import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
#time is importing to wait the web page after launch
service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
time.sleep(20)
print(driver.title)
driver.get("https://www.google.com")
driver.minimize_window()  #minimize window
time.sleep(20)
print(driver.title)