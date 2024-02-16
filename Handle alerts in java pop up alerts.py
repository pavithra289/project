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
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()

#till now the driver is not aware of this alert,but we can switch the driver web alert to pop -up text alert
alert = driver.switch_to.alert
#supoose if we want the alert pop to print in the output window follow the beow stpes
#just put this switch to alert mode to the object alert
alertText = alert.text
print(alertText)

# To click on Ok  in that alert
#alert.accept()
time.sleep(4)

