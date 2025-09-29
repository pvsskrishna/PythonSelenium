from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service(r"C:\Users\varun\PycharmProjects\PythonSelenium\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)

driver.get(r"https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.implicitly_wait(10)

wait = WebDriverWait(driver,20)
#wait.until(EC.presence_of_element_located())
action = action_chains.ActionChains(driver)

#dropdown = Select()

#TODO 1: Sort all the items present in the column by clicking the sort button
driver.find_element(By.XPATH,"//tr/th/span[text()='Veg/fruit name']").click()
time.sleep(2)

#TODO 2: collect them into a list lets say browserSortedVeggies
veggies_webelements = driver.find_elements(By.XPATH,"//tbody/tr/td[1]")
browserSortedVeggies = []
for element in veggies_webelements:
    browserSortedVeggies.append(element.text)

print(f"browserSortedVeggies:: {browserSortedVeggies}")


#TODO 3:sort the browserSortedVeggies lets say this new list generated is newSortedList
originalBrowserSortedList = browserSortedVeggies.copy()
print(f"originalBrowserSortedList:: .Copy::{originalBrowserSortedList}")

sortedList = sorted(originalBrowserSortedList)
print(f"sortedList:: {sortedList}")

'''
Use .sort() only when you want to rearrange the same list and don’t need a new one.
Use sorted() when you want a new sorted list while keeping the original intact.
'''


#TODO 4:compare this list_1 with list_2 to check whether the sort happened properly or not.
assert originalBrowserSortedList == sortedList

