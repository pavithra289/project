import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client")


driver.find_element(By.ID,"userEmail").send_keys("demo@gmail.com")
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("12345")
time.sleep(7)
#the HTML that is starting with 'a' means anchor is named as link

driver.find_element(By.LINK_TEXT,"Forgot password?").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("demo@gmail.com")
time.sleep(5)
driver.find_element(By.ID,"userPassword").send_keys("123456")
time.sleep(5)
driver.find_element(By.ID,"confirmPassword").send_keys("123456")
time.sleep(5)

driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
