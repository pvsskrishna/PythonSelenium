"""
send assignment to below mail-id:
---------------------------------
assignmentsql@gmail.com

Day - 2
Assignment:1
-----------
launch --> https://demowebshop.tricentis.com/ --> click on register link --> enter values for
all the fields and register --> click on logout link --> click on login link --> enter un&pwd
login
"""
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import ChromiumOptions

o = ChromiumOptions()
o.add_experimental_option("detach",True)

driver = Chrome(options=o)

driver.get(r"https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element(By.CLASS_NAME,'ico-register').click()
driver.find_element(By.ID,'gender-male').click()
driver.find_element(By.ID,'FirstName').send_keys('johny')
driver.find_element(By.ID,'LastName').send_keys('dep')
driver.find_element(By.ID,'Email').send_keys('dobari4460012@roratu.com')
driver.find_element(By.ID,'Password').send_keys('pirates@123')
driver.find_element(By.ID,'ConfirmPassword').send_keys('pirates@123')
time.sleep(2)
driver.find_element(By.NAME,'register-button').click()
time.sleep(2)
driver.find_element(By.CLASS_NAME,'ico-logout').click()
time.sleep(2)
driver.find_element(By.CLASS_NAME,'ico-login').click()
driver.find_element(By.ID,'Email').send_keys('dobari4460012@roratu.com')
driver.find_element(By.ID,'Password').send_keys('pirates@123')
driver.find_element(By.XPATH,"(//input[@type='submit'])[2]").click()
driver.quit()