from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


service_obj = Service(r"C:\Users\varun\PycharmProjects\PythonSelenium\Drivers\chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.implicitly_wait(10)
action = action_chains.ActionChains(driver)
wait = WebDriverWait(driver,20)

driver.maximize_window()
driver.get(r"https://the-internet.herokuapp.com/")
driver.find_element(By.LINK_TEXT,"Frames").click()
driver.find_element(By.LINK_TEXT,"iFrame").click()
sleep(2)

driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("Hello")

driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)


