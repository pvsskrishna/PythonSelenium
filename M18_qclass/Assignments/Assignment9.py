"""
Day 12

assignment:
-----------
launch --> https://english.bmrc.co.in/ --> click on english button --> mouse hover on travel-info
element --> print all the suggestion/options.
"""
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.common.by import By
o = ChromiumOptions()
o.add_experimental_option("detach",False)
driver = Chrome(options=o)
import time
driver.implicitly_wait(15)


driver.get("https://english.bmrc.co.in/")
driver.maximize_window()
a = ActionChains(driver)
englishButton = driver.find_element(By.XPATH,"//span[.='English']")
# a.move_to_element(englishButton).perform()
englishButton.click()

time.sleep(2)
travelInfo = driver.find_element(By.XPATH,"//a[.='TRAVEL INFO']")
a.move_to_element(travelInfo).perform()
time.sleep(2)
dropdownValues = driver.find_elements(By.XPATH,"//a[.='TRAVEL INFO']/following-sibling::ul/li/a")
for value in dropdownValues:
    print(value.text)


