import pytest
from selenium.webdriver import Chrome

@pytest.fixture
def launch():
    driver = Chrome()
    driver.get("https://www.icici.bank.in/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()



