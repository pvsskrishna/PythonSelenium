import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep

service_obj = Service(r"C:\Users\varun\PycharmProjects\PythonSelenium\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.implicitly_wait(10)
action = action_chains.ActionChains(driver)
wait = WebDriverWait(driver,20)

driver.get(r"https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
sleep(2)
driver.switch_to.frame("courses-iframe")
QA_meetup_text = driver.find_element(By.CLASS_NAME,"header-top-link").text
print(f"text :: {QA_meetup_text}")
assert "QA Meetup" in QA_meetup_text

more = driver.find_element(By.CLASS_NAME,"dropdown-toggle")
action.move_to_element(more).perform()
driver.find_element(By.XPATH,"//li/a[text() = 'Contact']").click()
time.sleep(10)


