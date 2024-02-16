import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
name="rahul"

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR,"#confirmbtn").click()
time.sleep(5)
alert = driver.switch_to.alert
alertText= alert.text
#To check whether the rahul text is present in the alert text use the below function

assert name in alertText


print(alertText)
#To click on Ok we have to use accept
alert.accept()
#To click on reject we have to use dismiss
#alert.dismiss()