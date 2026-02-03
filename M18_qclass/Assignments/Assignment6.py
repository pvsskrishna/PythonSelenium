"""

Day 9
assignment:
***********
ws to verify create account and continue with google is enabled/not in zomato --> signup.
https://www.zomato.com/bangalore
ws select CPV delhi and verify cpv delhi radio button is selected or not
https://portal2.passportindia.gov.in/AppOnlineProject/user/RegistrationBaseAction?request_locale=en
ws to verify enter mobilenumber text field is displayed or not then enter number and check verify button and enter
OTP field is displayed or not in flipkart.com
https://www.flipkart.com/
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import ChromiumOptions
o = ChromiumOptions()
from selenium.webdriver import Chrome
import time
driver = Chrome(options = o)
o.add_experimental_option("detach",False)

driver.get("https://www.zomato.com/bangalore")
time.sleep(3)
driver.maximize_window()
driver.find_element(By.XPATH,"(//div[.='Delivery'])[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//a[.='Sign up']").click()
googleSignin = driver.find_element(By.XPATH,"//span[.='Sign in with Google']")
print(googleSignin.is_enabled())
print(googleSignin.is_displayed())


driver.get(r"https://services1.passportindia.gov.in/forms/registration")
time.sleep(2)
driver.maximize_window()
cpvButton = driver.find_element(By.XPATH,"(//div[.='CPV Delhi'])[4]")
cpvButton.click()
time.sleep(2)
print(cpvButton.is_enabled())

driver.get(r"https://www.flipkart.com/")
time.sleep(2)
driver.maximize_window()
driver.find_element(By.XPATH,"//span[.='Login']").click()
time.sleep(2)
mobileNoTxtfield = driver.find_element(By.XPATH,"//input[@autocomplete='off' and @type='text' and @class='c3Bd2c yXUQVt']")
print('is text field displayed:',mobileNoTxtfield.is_displayed())
mobileNoTxtfield.send_keys(9876543210)
driver.find_element(By.XPATH,"//button[.='Request OTP']").click()

driver.close()

