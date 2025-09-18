from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.service import Service
service_obj = Service(r"C:\Users\varun\PycharmProjects\PythonSelenium\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
name = 'Varun'
url = r"https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"name").send_keys(name)
print(name)
alert_button = driver.find_element(By.CSS_SELECTOR,"input[id='alertbtn']")
alert_button.click()
print("is clicked")
time.sleep(5)
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
assert name in alert_text
alert.accept() #to click ok and alert.dismiss() to click cancel


