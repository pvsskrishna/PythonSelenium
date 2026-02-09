"""
#31-12-2025 ---> Day 15

Assignment
open https://passbook.epfindia.gov.in/MemberPassBook/login > click on login button > handle the popup

open https://www.amazon.in/ref=nav_logo > click on all button > click on best seller > click on any product
> click on add to cart > click on proceed to buy
"""
import time
from datetime import datetime
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

o= ChromiumOptions()
o.add_experimental_option("detach",False)
driver = Chrome(options=o)
driver.implicitly_wait(10)
wait = WebDriverWait(driver,15)

def take_Screenshot():
    SCREENSHOT_NAME = datetime.now().strftime("%y-%m-%d_%H-%M-%S")
    driver.get_screenshot_as_file(f"./screenshots_test//{SCREENSHOT_NAME}.png")


def testCase1():
    try:
        driver.get("https://licindia.in/")
        time.sleep(2)
        driver.maximize_window()
        try:
            driver.find_element(By.XPATH,"//button[.='English']").click()
        except:
            a = driver.switch_to.alert
            a.accept()
    except Exception as e:
        take_Screenshot()
        print(f"testCase1 error is: {e}")
    finally:
        driver.close()

def testCase2():
    try:
        driver.get("https://licindia.in/")
        time.sleep(1)
        driver.maximize_window()
        if driver.find_element(By.XPATH, "//button[.='English']").is_displayed():
            driver.find_element(By.XPATH, "//button[.='English']").click()
            print("Clicked on English")

            driver.find_element(By.XPATH, "//a[@title='Login']").click()
            print("clicked on login")

            a = driver.switch_to.alert
            a.accept()
            print("Accepted")
            # a.dismiss()
            # print("clicked on Dismiss")

        else:
            driver.find_element(By.XPATH,"//a[@title='Login']").click()
            a = driver.switch_to.alert

            a.accept()
            print("Accepted")
            # a.dismiss()
            # print("clicked on Dismiss")

    except Exception as e:
        take_Screenshot()
        print(f"testCase2 error is: {e}")
    finally:
        driver.close()


def testCase3():
    try:
        driver.get("https://demowebshop.tricentis.com/")
        time.sleep(3)
        driver.maximize_window()
        driver.find_element("xpath", "//input[@value='Search']").click()
        a = driver.switch_to.alert
        a.accept()
    except Exception as e:
        take_Screenshot()
        print(f"testCase3 error is: {e}")
    finally:
        driver.close()

def testCase4():
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    driver.find_element("xpath", "//input[@value='Search']").click()
    a = driver.switch_to.alert
    print(a.text)
    # Please enter some search keyword

def testCase5():
    try:
        driver.get(r"https://www.redbus.in/")
        driver.maximize_window()
        driver.find_element(By.XPATH,"//button[.='Account']").click()
        driver.find_element(By.XPATH,"//button[.='Log in']").click()
        driver.find_element(By.XPATH,"//input[@inputmode='numeric']").send_keys("987654321")
        driver.close()
    except Exception as e:
        take_Screenshot()
        print(f"testCase5 error is: {e}")
        driver.close()
        raise

def testCase6():
    try:
        driver.get(r"https://mamaearth.in/")
        driver.maximize_window()
        driver.find_element(By.XPATH,"//div[.='Login']").click()
        driver.find_element(By.XPATH,"//input[@type='number']").send_keys("9876543210")
        driver.find_element(By.XPATH,"//button[.='Login with OTP']").click()
        print("clicked on otp")
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//button[.='VERIFY']")))
        assert driver.find_element(By.XPATH,"//button[.='VERIFY']").is_displayed()
        time.sleep(2)
        driver.close()
    except Exception as e:
        take_Screenshot()
        print(f"testCase5 error is: {e}")
        driver.close()
        raise

# Assignment Solutions

def test_Assignment1():
    try:
        driver.get(r"https://passbook.epfindia.gov.in/MemberPassBook/login")
        driver.maximize_window()
        driver.find_element(By.ID,"login").click()
        a = driver.switch_to.alert
        time.sleep(2)
        a.accept()

    except Exception as e:
        take_Screenshot()
        print(f"Error in Assignment: {e}")
        driver.close()
        raise

def test_Assignment2():
    try:
        driver.get(r"https://www.amazon.in/ref=nav_logo")
        driver.maximize_window()
        driver.find_element(By.XPATH,"(//span[.='All'])[2]").click()
        driver.find_element(By.XPATH,"(//a[.='Bestsellers'])[2]").click()
        time.sleep(3)
        item = driver.find_element(By.XPATH,"//div[.='Ghar Soaps Sandalwood & Saffron Magic Soaps For Bath (300 Gms Pack Of 3) | Paraben Free | Chandan & Kesar Bath Soap |…']")

        # location = item.location
        # x=location['x']
        # y=location['y']
        #
        # driver.execute(f"window.scrollBy(0,-300);")
        #wait.until(EC.visibility_of_element_located(item)).click()

        item.click()
        driver.find_element(By.XPATH,"//input[@id='add-to-cart-button']").click()
        driver.find_element(By.XPATH,"//input[@name='proceedToRetailCheckout']").click()
    except Exception as e:
        take_Screenshot()
        print(f"Error in Assignment: {e}")
        driver.close()
        raise
