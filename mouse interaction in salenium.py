from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service

service_obj=Service()
driver= webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice")

action =  ActionChains(driver)
#action.click_and_hold()
#action.context_click()
#action.double_click()
#action.drag_and_drop()