from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\varun\PycharmProjects\PythonSelenium\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

url = r"https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(15)

#handling the checkboxes dynamically and using is_selected() method
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        if checkbox.is_selected():
            print("selected the checkbox")
        break
time.sleep(3)

#handling the radio buttons dynamically and using is_selected() method
radiobuttons = driver.find_elements(By.XPATH,"//input[@type='radio']")
for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == 'radio2':
        radiobutton.click()
        if radiobutton.is_selected():
            print('selected the radiobutton')
        break
time.sleep(2)

#handling the textboxes and using is_displayed() method
displayed_textBox = driver.find_element(By.ID,"displayed-text")
if displayed_textBox.is_displayed():
    print("text box is displayed")
hideButton = driver.find_element(By.ID,"hide-textbox")
hideButton.click()
assert not displayed_textBox.is_displayed()



