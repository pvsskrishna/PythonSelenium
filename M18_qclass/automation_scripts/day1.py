"""
launching empty browser:
------------------------
*to launch empty browser developer has written code inside a browser specific class
constructor.
*constructor will execute when ever we create an object
*each browser specific class should be import from below statement.
    from selenium.webdriver import BrowserClassName
"""
from webbrowser import Chrome

"""
class Chrome:
    def __init__(self):
        #code to launch empty
        chrome browser

c = Chrome()            #object creation
"""
#ws to launch empty chrome browser
# from selenium.webdriver import Chrome
# c = Chrome()

#ws to launch empty firefox browser
# from selenium.webdriver import Firefox
# f = Firefox()

#ws to launch empty edge  browser
# from selenium.webdriver import Edge
# e = Edge()
###########################################################################################
#program to with stand a chrome browser for long duration
"""
*as per the latest version of selenium chrome browser will close automatically, if we
want to with stand a browser for long duration then we should follow the below code.
"""
"""
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
"""
##################################################################################################################
#10/12/2025
###############################################################################################
#get(): it is used to enter the URL
#       it will accept both secured(https) and non-secured(http) URL.
#       if we pass other than secured and non-secured URL then it will throw, InvalidArgumentException
#   syntax: driver.get("URL")

#example on secured URL
"""
driver = Chrome(options=o)
driver.get("https://www.fb.com")
"""
#example on non-secured URL
"""
driver = Chrome(options=o)
driver.get("http://www.fb.com")
"""
#example on invalid URL
"""
driver = Chrome(options=o)
driver.get("www.fb.com")
#InvalidArgumentException
"""
################################################################################################
#close():it will close the current window/tab.
#   syntax:driver.close()

#quit():it will close complete browser.
#   syntax:driver.quit()

#example on close() method
"""
driver = Chrome(options=o)
driver.get("https://www.instagram.com/")
sleep(1)
driver.close()
"""
#example on quit() method
"""
driver = Chrome(options=o)
driver.get("https://www.instagram.com/")
sleep(1)
driver.quit()
"""
###############################################################################################
# maximize_window(): it is used to maximize the window.
#   syntax: driver.maximize_window()
# minimize_window(): it is used to minimize the window.
#   syntax: driver.minimize_window()
# fullscreen_window(): it is used to set full screen window.
#   syntax: driver.fullscreen_window()

#ws to maximize, minimize and full screen the window.
"""
driver = Chrome(options=o)
driver.get("https://www.instagram.com/")
sleep(1)
driver.maximize_window()
sleep(1)
driver.minimize_window()
sleep(1)
driver.maximize_window()
sleep(1)
driver.fullscreen_window()
"""
#########################################################################################
#back(): it used to click on backward arrow in the browser.
#   syntax: driver.back()
#forward(): it used to click on forward arrow in the browser.
#   syntax: driver.forward()
#refresh(): it used to click on refresh icon in the browser.
#   syntax: driver.refresh()

#ws to perform backward, forward, refresh action in the browser.
"""
driver = Chrome(options=o)
driver.get("https://www.flipkart.com")
driver.maximize_window()
sleep(2)
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
"""
################################################################################################
#get_window_size(): it will return dictionary of height and width of a browser.
#   syntax: driver.get_window_size()
#get_window_position(): it will return dictionary of x and y axis of a browser.
#   syntax: driver.get_window_position()
#get_window_rect(): it will return dictionary of height, width, x and y axis of a browser.
#   syntax: driver.get_window_rect()

#ws to print x, y, width, height a of browser
"""
driver = Chrome(options=o)
driver.get("https://www.ajio.com")
driver.maximize_window()
data = driver.get_window_size()
print(data)     #{'width': 1382, 'height': 744}
data1 = driver.get_window_position()
print(data1)    #{'x': -8, 'y': -8}
data2 = driver.get_window_rect()
print(data2)    #{'height': 744, 'width': 1382, 'x': -8, 'y': -8}
"""
###################################################################################################
#set_window_size(): it is used to set the window based on height and width.
#   syntax: driver.set_window(width, height)
#set_window_position(): it is used to set the window based on x and y axis.
#   syntax: driver.set_window(x, y)
#set_window_rect(): it is used to set the window base on x, y, height and width.
#   syntax: driver.set_window(x, y, width, height)

#ws to set the window based on x, y, width, height a of browser
"""
driver = Chrome(options=o)
driver.get("https://www.fb.com")
driver.maximize_window()
sleep(2)
driver.set_window_size(100, 150)
sleep(2)
driver.set_window_position(67, 23)
sleep(2)
driver.set_window_rect(290, 87, 234, 500)
"""

##############################################################################################
"""
verification property
"""
#title: it will return current title of a webpage.
#   syntax: driver.title
#ws to print title of nike.com webpage
"""
driver = Chrome(options=o)
driver.get("https://www.nike.com/in/")
driver.maximize_window()
print(driver.title)         #Nike. Just Do It. Nike IN
sleep(2)
print(driver.title)         #Men's Shoes, Clothing & Accessories. Nike IN
"""
#current_url: it will return current URL of a webpage.
#   syntax: driver.current_url
#ws to print url of a webpage
"""
driver = Chrome(options=o)
driver.get("https://www.nike.com/in/")
driver.maximize_window()
print(driver.current_url)         #https://www.nike.com/in/
sleep(3)
print(driver.current_url)         #https://www.nike.com/in/women
"""
#page_source: it will return current webpage html source code
#   syntax: driver.page_source
#ws to print current webpage source code
"""
driver = Chrome(options=o)
driver.get("https://www.nike.com/in/")
driver.maximize_window()
print(driver.page_source)
#<html> ... </html>
"""
###############################################################################################











