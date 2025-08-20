from selenium import webdriver
#browser exposes an executable file
#Through Selenium test we need to invoke the executable file which will then invoke actual browser
driver = webdriver.Chrome()
#driver=webdriver.Firefox()
#driver = webdriver.Ie()
driver.maximize_window()
driver.get(r"https://rahulshettyacademy.com/")  #get method to hit url on  browser

print(driver.title)
print(driver.current_url)
driver.get(r"https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()









