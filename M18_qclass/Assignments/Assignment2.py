"""
Day - 4
Assignment-2
-----------
launch --> https://services2.passportindia.gov.in/forms/login --> click on register now link
-->select radio CPV Delhi--> enter full name, email, select no radio button --> enter login id
, password and click on signin button.

"""
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.common.by import By
o = ChromiumOptions()

o.add_experimental_option('detach',True)
driver = Chrome(options=o)
driver.get("https://services2.passportindia.gov.in/forms/login")
driver.maximize_window()
driver.find_element(By.XPATH, "//div[text()='Register Now!']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[text()='CPV Delhi']").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("selenium")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("selenium@gmail.com")
driver.find_element(By.XPATH, "//div[text()='No']").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys("seleniumautomation")
driver.find_element(By.XPATH, "(//input[@type='password'])[2]").send_keys("seLEnium@123")
driver.find_element(By.XPATH, "//div[text()='Sign Up']").click()
driver.quit()

