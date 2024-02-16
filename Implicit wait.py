import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.refresh()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
time.sleep(5)

for result in results:
    result.find_element(By.XPATH,"div/button").click()
    time.sleep(7)

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(4)

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
time.sleep(7)

driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
time.sleep(6)
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
time.sleep(7)