#Day7
"""
Assignment-4

assignment question:
====================
https://www.accuweather.com/en/in/india-weather
Q1. inspect weather of Bengaluru

https://www.goodreturns.in/gold-rates/
Q2. inspect price of 22K gold

"""

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import time
from selenium.webdriver.chrome.options import ChromiumOptions
o=ChromiumOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options = o)

#Q1. inspect weather of Bengaluru
driver.get(r"https://www.accuweather.com/en/in/india-weather")
driver.maximize_window()
bangaloreTemp = driver.find_element(By.XPATH,"//span[.='Bengaluru']/..//span[@class='text temp']").text
print(bangaloreTemp) #27°


#Q2. inspect price of 22K gold
driver.get(r"https://www.goodreturns.in/gold-rates/")
driver.maximize_window()
# goldCost = driver.find_element(By.ID,"22K-price").text
# print(goldCost)

cost = driver.find_element(By.XPATH,"//p[contains(., '22K')][1]/../..//span[@id='22K-price']").text
print(cost) #₹12,300
driver.close()