import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(5)
#locator by Name
driver.find_element(By.NAME,"name").send_keys("rahul")
time.sleep(8)
#by Xpath
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")

time.sleep(6)
driver.find_element(By.XPATH,"//input[@id='exampleInputPassword1']").send_keys("123456")
time.sleep(9)
driver.find_element(By.CSS_SELECTOR,"input[type='checkbox']").click()
time.sleep(5)
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(0)
time.sleep(5)
driver.find_element(By.XPATH,"//input[@value='option1']").click()
time.sleep(4)

driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(5)
