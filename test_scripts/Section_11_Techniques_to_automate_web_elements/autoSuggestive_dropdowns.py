import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj= Service(r"C:\Users\varun\PycharmProjects\PythonSelenium\Drivers\chromedriver.exe")
driver= webdriver.Chrome(service= service_obj)

url= r"https://rahulshettyacademy.com/dropdownsPractise/"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(15)

dropdown = driver.find_element(By.ID,"autosuggest")
dropdown.send_keys("ind")
countries = driver.find_elements(By.CSS_SELECTOR,"li[class ='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == 'India':
        country.click()
        break
#print(dropdown.text) ---> wont work
print(dropdown.get_attribute("value"))
assert dropdown.get_attribute("value") == "India"
time.sleep(5)


