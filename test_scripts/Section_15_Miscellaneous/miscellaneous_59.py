import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service(r"C:\Users\varun\PycharmProjects\PythonSelenium\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options= chrome_options)


driver.maximize_window()
driver.implicitly_wait(10)
driver.get(r"https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)

driver.execute_script("window.scroll(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screenshot.png")
time.sleep(2)




