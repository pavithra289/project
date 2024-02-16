import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

radiobuttons=driver.find_elements(By.XPATH,"//input[@type='radio']")

print(len(radiobuttons))
radiobuttons[2].click()

driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
#ssert  not driver.find_element(By.ID,"displayed-text").is_displayed()
time.sleep(5)
#driver.find_element(By.ID,"show-textbox").click()
time.sleep(6)
#assert not driver.find_element(By.ID,"show-textbox").click()
time.sleep(6)