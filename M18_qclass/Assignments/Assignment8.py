"""
Day 11
assignment
----------
ws to print all the options from all drop-down in amazon
https://www.amazon.in/ref=nav_logo

ws to search for shirt > print all the suggestions in amazon
https://www.amazon.in/ref=nav_logo

question:
--------------------
https://www.landrecords.karnataka.gov.in/service2/RTC.aspx
launch above application select option from district > taluk > hobli > village dd
"""
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver import Chrome
o = ChromiumOptions()
o.add_experimental_option("detach",False)
driver = Chrome(options=o)

# Question 1
driver.get(r'https://www.amazon.in/ref=nav_logo')
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"(//span[.='All'])[2]").click()
time.sleep(1)

trendingOptionsList = driver.find_elements(By.XPATH,"//div[.='Trending']//following-sibling::ul/li/a[normalize-space()]")
trendingOptions = [i.text for i in trendingOptionsList if i.text.strip()]
print("trendingOptions",trendingOptions)

digitalContentOptionsList = driver.find_elements(By.XPATH,"//div[.='Digital Content and Devices']//following-sibling::ul/li/a/div[normalize-space()]")
digitalContentOptions = [i.text for i in digitalContentOptionsList if i.text.strip()]
print("digitalContentOptions",digitalContentOptions)

shopByCategoryList = driver.find_elements(By.XPATH,"//div[.='Shop by Category']//following-sibling::ul/li/a/div[normalize-space()]")
shopByCategoryOptions = [i.text for i in shopByCategoryList if i.text.strip()]
print("shopByCategoryOptions",shopByCategoryOptions)

programesAndFeaturesList = driver.find_elements(By.XPATH,"//div[.='Programs & Features']//following-sibling::ul/li/a/div[normalize-space()]")
programesAndFeaturesOptions = [i.text for i in shopByCategoryList if i.text.strip()]
print("programesAndFeaturesOptions",programesAndFeaturesOptions)

helpAndSettingsList = driver.find_elements(By.XPATH,"//div[.='Help & Settings']//following-sibling::ul/li/a[normalize-space()]")
helpAndSettingsOptions = [i.text for i in shopByCategoryList if i.text.strip()]
print("helpAndSettingsOptions",helpAndSettingsOptions)

# Question 2