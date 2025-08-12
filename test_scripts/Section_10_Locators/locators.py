# 35. Inspecting HTML to identify attributes of element
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url= r"https://apaims2.0.vassarlabs.com/login"

# chrome
service_obj= Service(r"C:\Users\varun\PycharmProjects\PythonSelenium\Drivers\chromedriver.exe")
driver= webdriver.Chrome(service= service_obj)
driver.get(url)

# driver= webdriver.Chrome()    #Either use this method or service method anything is fine

driver.maximize_window()
title = driver.title
print(title)
print(driver.current_url)
time.sleep(2)
driver.close()

driver.find_element(By.ID)