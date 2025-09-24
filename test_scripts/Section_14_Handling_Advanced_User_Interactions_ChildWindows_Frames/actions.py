from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common import action_chains
from selenium.webdriver.chrome.service import Service

url =r"https://www.rahulshettyacademy.com/AutomationPractice/"
service_obj = Service(r"C:\Users\varun\PycharmProjects\PythonSelenium\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(15)
driver.get(url)

action = action_chains.ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()

wait = WebDriverWait(driver,20)
top_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Top")))

#action.context_click(top_link).perform()
#time.sleep(3)
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
time.sleep(3)



