"""
Day 10
assignment question:
--------------------
https://www.landrecords.karnataka.gov.in/service2/RTC.aspx
launch above application select option from district > taluk > hobli > village dd
"""
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import ChromiumOptions
import time



o=ChromiumOptions()
o.add_experimental_option('detach',True)
driver = Chrome(options=o)
driver.get(r"https://www.landrecords.karnataka.gov.in/service2/RTC.aspx")
time.sleep(2)

talukdd = driver.find_element(By.XPATH,"//select[@id='ctl00_MainContent_ddlCTaluk']")
#talukddAfterRefresh = driver.find_element(By.XPATH,"//select[@name='ctl00$MainContent$ddlCTaluk']")

districtdd = driver.find_element(By.XPATH,"//select[@id='ctl00_MainContent_ddlCDistrict']")
dist = Select(districtdd)
print('is multiple',dist.is_multiple)
options = dist.options
for i in options:
    print(i.text)
print('Taluk is disabled:',not(talukdd.is_enabled())) #it should be False
dist.select_by_visible_text('BALLARI')
#print('Taluk is enabled:',talukddAfterRefresh.is_enabled()) #it should be True

talukdd = driver.find_element(By.XPATH,"//select[@id='ctl00_MainContent_ddlCTaluk']")
taluk = Select(talukdd)
taluk.select_by_index(1) #BALLARI

driver.refresh()
time.sleep(5)
hoblidd = driver.find_element(By.XPATH,"//select[@name='ctl00_MainContent_ddlCHobli']")
hobli = Select(hoblidd)
hobli.select_by_visible_text("KOLURU") #KOLURU


time.sleep(5)
villagedd = driver.find_element(By.XPATH,"//select[@name='ctl00_MainContent_ddlCVillage']")
village = Select(villagedd)
village.select_by_visible_text("DAMMURU KAGGAL")

time.sleep(2)
driver.close()



