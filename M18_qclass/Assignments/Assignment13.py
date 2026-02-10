"""
Day 16
#01/01/2026 ---> Day 16

assignment
----------
open https://mohfw.gov.in/?q=en > click on Organisation > click on Departments of Health and Family Welfare
> click Disaster Management Cell > click on Provider Course Manual for Doctors (5.39 MB) >
click download icon.
"""
import time
from datetime import datetime
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

o = ChromiumOptions()
o.add_experimental_option("detach",False)
o.add_argument("--disable-sync")
o.add_argument("--log-level=3")
driver = Chrome(options=o)

def takeScreenshot():
    screenshot_name = datetime.now().strftime("%y-%m-%d_%H-%M-%S")
    driver.get_screenshot_as_file(f"./screenshots_test//{screenshot_name}.png")

def testCase1():
    try:
        driver.get(r"https://mohfw.gov.in/?q=en")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element(By.ID,"menu-5644-1").click()
        driver.find_element(By.XPATH,"(//a[.='Departments of Health and Family Welfare'])[1]").click()
        driver.find_element(By.XPATH,"//a[.='Disaster Management Cell']").click()

        window1 = driver.window_handles
        driver.switch_to.window(window1[-1])
        print('switched to new window')

        driver.find_element(By.XPATH,"(//a[@title='PDF that opens in a new window'])[2]").click()
        print("clicked on pdf link2")

        time.sleep(3)
        window1 = driver.window_handles
        driver.switch_to.window(window1[-1])

        assert driver.current_url == "https://mohfw.gov.in/sites/default/files/Provider%20course%20manual%20for%20Doctors.pdf"
        print("pdf preview working")
        driver.close()

    except Exception as e:
        takeScreenshot()
        print(f"error is:{e}")
        
    finally:
        driver.quit()

def testCase2():
    try:
        driver.get("https://www.shine.com/registration/")
        driver.maximize_window()
        time.sleep(2)
        try:
            driver.find_element(By.XPATH,"//input[@type='file']").send_keys(r"C:\Users\varun\Downloads\dummy1.pdf")
            time.sleep(2)
        except:
            driver.find_element(By.XPATH, "//input[@type='file']").send_keys(
                r"C:\Users\varun\Downloads\dummy-pdf_4.pdf")
        finally:
            print("test case 2 is executed")
    except Exception as e:
        takeScreenshot()
        print(f"error is: {e}")

    finally:
        driver.quit()

testCase1()
testCase2()
