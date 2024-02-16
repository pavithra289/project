import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(10)
driver.find_element(By.NAME,"name").send_keys("hello@gmail.com")
driver.find_element(By.NAME,"email").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()
time.sleep(10)









