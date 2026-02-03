from generic.take_screenshot import screenshot
from time import sleep

def text_assertion(etext, atext, driver):
    try:
        sleep(2)
        assert etext == atext, f"Expected text is {etext} and actual text is {atext}"
    except:
        screenshot(driver)
