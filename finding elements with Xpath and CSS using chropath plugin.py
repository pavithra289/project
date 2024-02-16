import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("rahul")
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#exampleInputPassword1").send_keys("123456")
driver.find_element(By.CSS_SELECTOR,"#exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("hello")
time.sleep(9)
value=driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
time.sleep(7)

#if i want to clear the entered data in the field you have to just add clear to that particular line
