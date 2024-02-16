import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.NAME,"name").send_keys("rahul")
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='exampleInputPassword1']").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.XPATH,"//input[@class='btn btn-success']").click()
driver.find_element(By.CLASS_NAME,"alert-success").text
