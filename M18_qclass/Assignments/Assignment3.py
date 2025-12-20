"""
Day-6
Assignment3:
------------
launch https://www.crocs.in/ --> click on register icon --> click on signin/register link
--> click on create account --> enter values for all mandatory fields and click on register button

"""

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import time
from selenium.webdriver.chrome.options import ChromiumOptions
o=ChromiumOptions()
o.add_experimental_option("detach",True)
driver = Chrome(options = o)
driver.get(r"https://www.crocs.in/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"button[aria-label='Sign In']").click()
driver.find_element(By.XPATH,"//a[contains(text(),'Sign In / Register')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//span[text()='Create an Account']").click()
time.sleep(2)
driver.find_element(By.ID,"firstName").send_keys('TestFirstName')
driver.find_element(By.ID,"lastName").send_keys('TestLastName')
driver.find_element(By.NAME,"customer.phone").send_keys('9876543210')
driver.find_element(By.ID,"Email").send_keys('dobari4460@roratu.com')
driver.find_element(By.NAME,"password").send_keys('Password@123')
driver.find_element(By.NAME,"confirm").send_keys('Password@123')
driver.find_element(By.ID,"term_check").click()

#driver.find_element(By.NAME,"subscribe").click()
element = driver.find_element(By.NAME, "subscribe")
driver.execute_script("arguments[0].click();", element)

driver.find_element(By.XPATH,"//span[text()='Register']").click()
driver.quit()

