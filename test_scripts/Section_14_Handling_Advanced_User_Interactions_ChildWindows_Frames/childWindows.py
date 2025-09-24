from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes
import time

service_obj = Service(r"C:\Users\varun\PycharmProjects\PythonSelenium\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
url = r"https://the-internet.herokuapp.com/windows"
driver.get(url)

driver.implicitly_wait(10)
action = action_chains.ActionChains(driver)
wait = WebDriverWait(driver,20)

driver.find_element(By.LINK_TEXT,"Click Here").click()
time.sleep(5)
openWindows = driver.window_handles

driver.switch_to.window(openWindows[1]) #0 ---> parent window
print(driver.find_element(By.TAG_NAME,"h3").text)
print(f"title:: {driver.title}")

driver.switch_to.window(openWindows[0]) #0 ---> parent window
print(driver.find_element(By.TAG_NAME,"h3").text)
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text
print(f"title:: {driver.title}")


