import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

o=ChromiumOptions()
o.add_argument("--disable-notifications")
o.add_experimental_option("detach",True)

driver = Chrome(options=o)
wait = WebDriverWait(driver,10)
#wait.until(EC.presence_of_element_located((By.XPATH,"XPATH Value")))
#dropdown = driver.find_element(By.XPATH,"")
#select = Select(dropdown)
action = ActionChains(driver)
key = Keys()

def takescreenshot():
    screenshotname=datetime.datetime.now().strftime("%y-%m-%d_%H-%M-%S")
    driver.get_screenshot_as_file(f"./screenshots_test/{screenshotname}.png")

def test_case1():   #only backspace
    try:
        driver.get(r"https://www.facebook.com/")
        driver.implicitly_wait(20)
        driver.maximize_window()
        un= driver.find_element(By.ID,"email")
        email="test1@gmail.com"
        un.send_keys(email)
        for i in range(len(email)):
            un.send_keys(key.BACKSPACE)
            time.sleep(1)
    except Exception as e:
        takescreenshot()
        print(f"exception is: {e}")
        raise
    finally:
        driver.close()

def test_case2():   #ctrl+a and backspace
    try:
        driver.get(r"https://www.facebook.com/")
        driver.implicitly_wait(20)
        driver.maximize_window()
        un= driver.find_element(By.ID,"email")
        email="test1@gmail.com"
        un.send_keys(email)
        un.send_keys(key.CONTROL+"a")
        time.sleep(2)
        un.send_keys(key.BACKSPACE)
        time.sleep(2)

    except Exception as e:
        takescreenshot()
        print(f"exception is: {e}")
        raise
    finally:
        driver.close()

def test_case3():   #send keys to UN and copied and pasted in pwd
    try:
        driver.get(r"https://www.facebook.com/")
        driver.implicitly_wait(20)
        driver.maximize_window()
        un= driver.find_element(By.ID,"email")
        pwd = driver.find_element(By.ID,"pass")
        email="test1@gmail.com"
        un.send_keys(email)
        un.send_keys(key.CONTROL+"a")
        time.sleep(2)
        un.send_keys(key.CONTROL+"C")
        time.sleep(2)
        pwd.clear()
        pwd.send_keys(key.CONTROL+"V")
        time.sleep(2)

    except Exception as e:
        takescreenshot()
        print(f"exception is: {e}")
        raise
    finally:
        driver.close()

def test_case4():   #clicking on hyperlink without using click method and mouse actions
    try:
        driver.get(r"https://www.facebook.com/")
        driver.implicitly_wait(20)
        driver.maximize_window()
        un= driver.find_element(By.ID,"email")
        pwd = driver.find_element(By.ID,"pass")
        forgot_password = driver.find_element(By.XPATH,"//a[.='Forgotten password?']")
        forgot_password.send_keys(key.ENTER)
        time.sleep(2)

    except Exception as e:
        takescreenshot()
        print(f"exception is: {e}")
        raise
    finally:
        driver.close()

def test_case5():   #deleting a unwanted using arrow and shift with backspace.
    try:
        driver.get(r"https://www.facebook.com/")
        driver.implicitly_wait(20)
        driver.maximize_window()
        un= driver.find_element(By.ID,"email")
        pwd = driver.find_element(By.ID,"pass")
        forgot_password = driver.find_element(By.XPATH,"//a[.='Forgotten password?']")
        un.send_keys("Selenium")
        un.send_keys(key.ARROW_LEFT,key.SHIFT,key.ARROW_LEFT,key.BACKSPACE)
        print(un.get_attribute("value"))
        time.sleep(2)

    except Exception as e:
        takescreenshot()
        print(f"exception is: {e}")
        raise
    finally:
        driver.close()

def test_case6():   #clicking tab and extracting active element data.
    try:
        driver.get(r"https://www.facebook.com/")
        driver.implicitly_wait(20)
        driver.maximize_window()
        un= driver.find_element(By.ID,"email")
        pwd = driver.find_element(By.ID,"pass")
        forgot_password = driver.find_element(By.XPATH,"//a[.='Forgotten password?']")
        forgot_password.send_keys(Keys.TAB)
        time.sleep(2)
        active = driver.switch_to.active_element
        print(active.get_attribute('outerHTML'))
    except Exception as e:
        takescreenshot()
        print(f"exception is: {e}")
        raise
    finally:
        driver.close()

# Scrolling test Cases
def test_case7():   #.Scrolling down 500 units
    try:
        driver.get(r"https://www.decathlon.in/")
        driver.implicitly_wait(20)
        driver.maximize_window()
        driver.execute_script("window.scrollBy(0, 500)")
        time.sleep(10)

    except Exception as e:
        takescreenshot()
        print(f"exception is: {e}")
        raise
    finally:
        driver.close()


def test_case8():   #.Scrolling down 500 units 4 times
    try:
        driver.get(r"https://www.decathlon.in/")
        driver.implicitly_wait(20)
        driver.maximize_window()
        for i in range(4):
            driver.execute_script("window.scrollBy(0, 500)")
            time.sleep(2)
        time.sleep(10)
    except Exception as e:
        takescreenshot()
        print(f"exception is: {e}")
        raise
    finally:
        driver.close()

def test_case9():   #.scrolling to particular element
    try:
        driver.get(r"https://www.lenskart.com/")
        driver.implicitly_wait(20)
        driver.maximize_window()
        brands = driver.find_element(By.XPATH,"//h1[.='Our Brands']")
        location = brands.location
        print(location)
        driver.execute_script(f"window.scrollBy({location['x'],location['y']})")
        time.sleep(10)
    except Exception as e:
        takescreenshot()
        print(f"exception is: {e}")
        raise
    finally:
        driver.close()

def test_case10():   #.scroll down and up again.
    try:
        driver.get(r"https://www.lenskart.com/")
        driver.implicitly_wait(20)
        driver.maximize_window()
        time.sleep(2)
        driver.execute_script(f"window.scrollBy(0, 1700)")
        time.sleep(2)
        driver.execute_script("window.scrollTo(500, 0)")

        ele = driver.find_element("xpath", "//h4[.='Trending Sunglasses']")
        d = ele.location  # d={'x': 40, 'y': 2239}
        driver.execute_script(f"window.scrollBy({d['x']}, {d['y']})")
        sleep(2)
        ele = driver.find_element("xpath", "//h4[.='Free Online Eye Test']")
        d = ele.location  # d={'x': 40, 'y': 2239}
        driver.execute_script(f"window.scrollTo({d['x']}, {d['y']})")
    except Exception as e:
        takescreenshot()
        print(f"exception is: {e}")
        raise
    finally:
        driver.close()

def test_case11():   #.scroll down and up again.
    try:
        driver.get(r"https://www.lenskart.com/")
        driver.implicitly_wait(20)
        driver.maximize_window()
        time.sleep(2)

        ele = driver.find_element("xpath", "//h1[.='Nearby Stores & Services']")
        d = ele.location  # d={'x': 40, 'y': 2239}
        driver.execute_script(f"window.scrollBy({d['x']}, {d['y']})")
        time.sleep(2)
        ele = driver.find_element("xpath", "//h1[.='Top Categories']")
        d = ele.location  # d={'x': 40, 'y': 2239}
        driver.execute_script(f"window.scrollTo({d['x']}, {d['y']})")
    except Exception as e:
        takescreenshot()
        print(f"exception is: {e}")
        raise
    finally:
        driver.close()