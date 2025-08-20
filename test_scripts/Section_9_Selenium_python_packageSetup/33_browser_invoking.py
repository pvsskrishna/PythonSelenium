# 33. RUnning Tests in Chrome, Firefox, Edge on basic WebDriver Methods

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.edge.service import Service

import time
url= r"https://apaims2.0.vassarlabs.com/login"

# chrome
service_obj= Service(r"C:\Users\varun\PycharmProjects\PythonSelenium\Drivers\chromedriver.exe")
driver= webdriver.Chrome(service= service_obj)
driver.get(url)

# edge
# service_obj= Service(r"C:\Users\varun\PycharmProjects\PythonSelenium\Drivers\msedgedriver.exe")
# driver= webdriver.Edge(service= service_obj)
# driver.get(url)

# firefox
# service_obj= Service(r"C:\Users\varun\PycharmProjects\PythonSelenium\Drivers\gechodriver.exe")
# driver= webdriver.firefox(service= service_obj)
# driver.get(url)

# driver= webdriver.Chrome()    #Either use this method or service method anything is fine
# driver= webdriver.Firefox()
# driver= webdriver.Edge()

driver.maximize_window()
title = driver.title
print(title)
print(driver.current_url)
time.sleep(2)
driver.close()