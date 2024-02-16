import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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

#SUM VALIDATION
prices = driver.find_elements(By.XPATH,"//tr/td[5]/p")
#once we got the find elements , we  are going to put it into the object called "prices".

sum=0
for price in prices:
    sum=sum+int(price.text)  # price.text is int + text , but we cannot sum up int+str , so simple we are wrapping it in int()
print(sum)


# to check whether the sum calcumated above and the total amount shown in the web element is matching or not
# we have to do the below find elemnet:
#and the sum is in integer and the total amount is in text
so to get the total amount to integer we have to wrap it into int()

totalamount= int(driver.find_element(By.CSS_SELECTOR,"span[class='totAmt']").text)
assert totalamount == sum



driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

time.sleep(7)
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()


