"""
Day8
assignment
----------
https://www.nseindia.com/
inspect stock price of NIFTY NEXT 50

xpath to inspect no. of likes for a any video in youtube
xpath to inspect no. of subscribers of any channel in youtube
xpath to inspect price of any product in amazon
"""

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import ChromiumOptions
o = ChromiumOptions()
driver = Chrome(options = o)
import time

# Q1. inspect stock price of NIFTY NEXT 50
# driver.get(r"https://www.nseindia.com/")
# driver.maximize_window()
# time.sleep(5)
# price = driver.find_element(By.XPATH,"//p[contains(.,'NIFTY NEXT 50')]//following-sibling::h3").text
# print(price)
# driver.close()