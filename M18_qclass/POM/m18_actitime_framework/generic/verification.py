from generic.take_screenshot import screenshot
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def verify_title(etitle, driver):
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(EC.title_is(etitle))
    except:
        screenshot(driver)
        raise Exception ("Title not found")
