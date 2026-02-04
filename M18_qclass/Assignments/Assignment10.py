# """
# Day 13 ---> 29/12/2025
#
# assignment
# ----------
# open https://www.zomato.com/bangalore/restaurants > click on login button > click on sign in with google
# """

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import ChromiumOptions
o = ChromiumOptions()
o.add_experimental_option("detach", False)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = Chrome(options = o)
driver.implicitly_wait(10)
driver.get(r"https://www.zomato.com/bangalore/restaurants")
#driver.maximize_window()
wait = WebDriverWait(driver,10)

login = (By.XPATH,"//a[.='Log in']")
wait.until(EC.visibility_of_element_located(login))
driver.find_element(*login).click()
import time
time.sleep(2)
try:
    print('Searching for Google iframe...')
    google_iframe = (By.XPATH, "(//iframe[contains(@title, 'Google')])[1]")
    wait.until(EC.frame_to_be_available_and_switch_to_it(google_iframe))
    print('Switched to iframe successfully')
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH,"//span[contains(text(),'Sign in')]"))).click()
    time.sleep(2)
except Exception as e:
    print(f"Click failed: {e}")
finally:
    driver.quit()