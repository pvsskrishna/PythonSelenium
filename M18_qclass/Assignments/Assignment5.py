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
o.add_experimental_option("detach",False)
driver = Chrome(options = o)
import time

# # Q1. inspect stock price of NIFTY NEXT 50
driver.get(r"https://www.nseindia.com/")
driver.maximize_window()
time.sleep(5)
price = driver.find_element(By.XPATH,"(//p[contains(.,'NIFTY NEXT 50')]//following-sibling::h3)[2]").text
print(f"Price is :{price}")


# #Q2. xpath to inspect no. of likes for a any video in youtube
driver.get(r"https://www.youtube.com/watch?v=SoW2pBak1_Q")
driver.maximize_window()
time.sleep(5)
likesCount= driver.find_element(By.XPATH,"(//button[@aria-label[contains(.,'like')]])[3]//following-sibling::div[@class[contains(.,'button-text-content')]]").text
# #Q3. xpath to inspect no. of subscribers of any channel in youtube
#totalSubs= driver.find_element(By.XPATH,"//ytd-channel-name[@id='channel-name']//following-sibling::yt-formatted-string[contains(@id,'owner-sub-count')]").text
totalSubs= driver.find_element(By.XPATH,"//ytd-channel-name[@id='channel-name']//following-sibling::yt-formatted-string[@id='owner-sub-count']").text
print(f"count of likes :{likesCount}")
print(f"count of Subs :{totalSubs}")

# #Q4. xpath to inspect price of any product in amazon
driver.get(r"https://www.amazon.in/")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("sp 125 bike")
driver.find_element(By.ID,"nav-search-submit-button").click()
time.sleep(3)
#productPrice = driver.find_element(By.XPATH,"((//span[contains(.,'Shield Heavy Duty Bike Cover for Honda SP125')])[2]//div[@class='a-row a-size-base a-color-base']//span[@class='a-offscreen'])[1]").get_attribute("innerText")
productPrice = driver.find_element(By.XPATH,"((//span[contains(.,'Shield Heavy Duty Bike Cover for Honda SP125')])[2]//span[@class='a-offscreen'])[1]").get_attribute("textContent")
print(f"product price: {productPrice}")
driver.close()
