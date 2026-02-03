"""
launching empty browser:
------------------------
*to launch empty browser developer has written code inside a browser specific class
constructor.
*constructor will execute when ever we create an object
*each browser specific class should be import from below statement.
    from selenium.webdriver import BrowserClassName
"""
from operator import contains
from time import sleep
from webbrowser import Chrome

from selenium.webdriver.common.by import By

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
###########################################################################################3
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
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

o = ChromeOptions()
o.add_experimental_option("detach", True)
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
#refresh(): it used to cick on refresh icon in the browser.
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
#11/12/2025
"""
html:
-----
*html stands for hyper text markup language.
*html is used to design and develop the webpages.
*a webpage will be developed by html tags.
*a keyword which is enclosed within angular brackets(<keyword>) is called as tags.
*if we open any tag it is mandatory to close the tag(</keyword>).

general structure of html:
==========================
<html>
    <head>
        <title> title of the webpage </title>
    </head>
    <body>
        #all the components
    </body>
</html>

steps to create a webpage:
==========================
step1: open notepad
step2: type the html code and save with .html extension
step3: select save as type and "all files" option
"""
"""
<html>
          <head>	
                <title>E20 Selenium Batch</title>
          </head>
          <body bgcolor="pink">		
         	Username:<input type="text" id="a1"><br/>	
            Password:<input type="password" id="a2"><br/>
            <input type="radio" name="n1">New User
            <input type="radio" name="n2">Old User<br/>
            <input type="checkbox" class="c1">I accept T&C**<br/>
            <a href="https://www.gmail.com" class="c2">Forgotten Passwod</a><br/>
            <img src="C:\\Users\\Hp\\Downloads\\selenium-image.png"><br/>
            <input type="submit" value="Submit">
            <input type="reset" value="Cancel">
         </body>	
</html>
"""
#########################################################################################################
"""
locators:
---------
*finding/inspecting/searching/locating the path of an element in a webpage is called
as locators.
*all locators are belongs to "By" clas

why locators?
-------------
*before performing any action(entering, clicking, selecting,..) in a webpage first we 
need to find the path of an element in a webpage because selenium is not a human it 
doesn't know the path of element in a webpage. 

types of locators:
------------------
1.id            5.link text
2.name          6.partial link text
3.class name    7.css selector
4.tag name      8.xpath

*to find an element in a webpage there are 2 methods are present,
1.find_element()                2.find_elements()

find_element():
---------------
*it is used to find single element in a webpage.
*the return type of find_element() is web element.
*if locator value matches with multiple element then it will return 1st element address.
*if the locator value not matches with any element then it will return "NoSuchElementException".
syntax: driver.find_element(locator_name, "locator_value")
                                |
                                |_By.ID, By.NAME, ...
find_elements():
----------------
*it is used to find multiple elements in a webpage.
"""

#1.id
#possiablity1: locator value matches with exactly 1 element
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/demo.html")
driver.maximize_window()
#way1: find the element and storing address in a variable -> webelement
username = driver.find_element(By.ID, 'a1')
username.send_keys("selenium@gmail.com")
                    (or)
#way2: find the element and performing action on same line
driver.find_element(By.ID, 'a1').send_keys("selenium@gmail.com")
"""
#possiablity2: if locator matches with multiple elements then it will return 1st element address
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/demo.html")
driver.maximize_window()
driver.find_element(By.ID, "a1").send_keys("selenium@123")
"""
#possiablity3: locator values doesn't match with any element then it will throw "NoSuchElementException"
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/demo.html")
driver.maximize_window()
driver.find_element(By.ID, "a10").send_keys("selenium@123")
#NoSuchElementException
"""
#########################################################################################################
#12/12/2025
#ws to login into facebook.com
"""
driver = Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.ID, 'email').send_keys('selenium@gmail.com')
driver.find_element(By.ID, 'pass').send_keys('selenium@123')
driver.find_element(By.NAME, 'login').click()
"""
##############################################################################################
#2.name
#ws to search for python selenium videos in youtube.com
"""
driver = Chrome(options=o)
driver.get("https://www.youtube.com/")
driver.maximize_window()
driver.find_element(By.NAME, "search_query").send_keys("python selenium")
driver.find_element(By.CLASS_NAME, "ytSearchboxComponentSearchButton").click()
"""
##############################################################################################
#3.class name
#ws to search for shirts in myntra.com
"""
driver = Chrome(options=o)
driver.get("https://www.myntra.com/")
driver.maximize_window()
driver.find_element(By.CLASS_NAME, "desktop-searchBar").send_keys("shirts")
driver.find_element(By.CLASS_NAME, "desktop-submit").click()
"""
#ws to search for movie in book my show
"""
driver = Chrome(options=o)
driver.get("https://in.bookmyshow.com/explore/home/bengaluru")
driver.maximize_window()
driver.find_element(By.CLASS_NAME, "sc-1or3vea-15.bMjnfo").click()
driver.find_element(By.CLASS_NAME, "sc-vuznvr-5.extnng").send_keys("Kantara")
"""
#ws to search for shirts in amazon
"""
driver = Chrome(options=o)
driver.get("https://www.amazon.in/ref=nav_logo")
driver.maximize_window()
driver.find_element(By.CLASS_NAME, "nav-input.nav-progressive-attribute").send_keys("shirts")
driver.find_element(By.ID, "nav-search-submit-button").click()
"""
##############################################################################################
#4.tag name
#ws to enter password in password text field
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/demo.html")
driver.maximize_window()
driver.find_element(By.TAG_NAME, 'input').send_keys('selenium@123')
"""

"""
way to inspect html code
========================
*Fn+F12 (or) F12
*ctrl+shift+i
*click on 3 dots on(:) top right corner --> click on more tools --> click on developer tools
"""
"""
sample html code:
=================
*a html code will have 3 component,
1.tag name: anything which is present after angular brackets(<tag_name)    
2.attribute: LHS=RHS (LHS --> attribute name, RHS --> attribute value)     
3.text: anything which is present before closing tag

         attribute_name  attribute_value
             /              /
<  a        href="https://www.gmail.com"     id="a1"     name="n1" >  Gmail </a>
   |                 |                          |           |           \
1.tag name      2.attribute1                    attribute2  attribute3   3.text
"""
"""
assignment:
-----------
launch --> https://demowebshop.tricentis.com/ --> click on register link --> enter values for 
all the fields and register --> click on logout link --> click on login link --> enter un&pwd 
login  
"""
#####################################################################################################
#15/12/2025
#5.link text
"""
*link text locator will work only for a text present in <a> tag (or) <span> tag inside <a>
*both are case sensitive.
*when the link text is very lengthy then we go partial link text.
"""
#ws to click on downloads, other lang exist and register now link in selenium.dev
"""
driver = Chrome(options=o)
driver.get("https://www.selenium.dev/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Downloads").click()
sleep(1)
driver.find_element(By.LINK_TEXT, "other languages exist").click()
sleep(1)
driver.find_element(By.LINK_TEXT, "Register now!").click()
"""
#example on text present in other than <a> or <span> tag
"""
driver = Chrome(options=o)
driver.get("https://blinkit.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.LINK_TEXT, "Detect my location").click()
"""
#6.partial link text
#ws to click on samsung phone in amazon.com
"""
driver = Chrome(options=o)
driver.get("https://www.amazon.in/s?k=samsung+mobile+5g+phone&crid=3OFWOFG9GOEJA&sprefix=samsung+mobile%2Caps%2C267&ref=nb_sb_ss_mvt-t11-ranker_1_14")
driver.maximize_window()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "Samsung Galaxy M06").click()
"""
##############################################################################################
#7.css selector
"""
*css stands for cascading style sheet
*css is used for decorating a webpage like font, size, color, image, animation, effects, etc..
*in automation we will css expression.

syntax of css expression:
-------------------------
tagname[attribute_name = 'attribute_value']


         attribute_name  attribute_value
             /              /
<  a        href="https://www.gmail.com"     id="a1"     name="n1" >  Gmail </a>
   |                 |                          |           |           \
1.tag name      2.attribute1                    attribute2  attribute3   3.text

example:
--------
a[href="https://www.gmail.com"] 
a[id='a1']      (or)  a#a1
a[name='n1']
a[class='c1'] (or) a.c1

steps to verify the css expression:
***********************************
step1: right click and inspect
step2: press ctrl+f --> now find by string search field will appear
step3: write css expression and press enter

if expression is valid verify the below things:
-----------------------------------------------
*the count should display 1of1
*element should be highlight
*code should be highlight in yellow color 

drawbacks:
----------
*we can't use text in css expression
"""
#wsto login to instgram.com
"""
driver = Chrome(options=o)
driver.get("https://www.instagram.com/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input[name='username']").send_keys("selenium")
driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("selenium@123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
"""
##############################################################################################
#8.xpath
"""
*path of an element in html tree structure is called as xpath.
*xpath is classified into 2 types
1.absolute xpath:
-----------------
*it indicates by single forward slash(/)
* (/) --> traverse from parent to its own child element. 
2.relative xpath 
----------------
*it indicates by double forward slash(//)
* (//) --> traverse from parent to any ch
"""
# sample html code:
# -----------------
"""
<html>
          <body>		
	<div>
	          UN1:<input type='text' id='a1'>	
	          UN2:<input type='text' id='a2'>	
	</div>
	<div>
	          UN3:<input type='text' id='a3'>	
	          UN4:<input type='text' id='a4'>	
	</div>
         </body>	
</html>
"""
#html tree
"""
html
  |
  |___body
        |
        |___div -->1
        |   |
        |   |__input -->1 (UN1) 
        |   |
        |   |__input -->2 (UN2)
        |
        |___div -->2
            |
            |__input -->1 (UN3)
            |
            |__input -->2 (UN4)
"""
"""
assignment2
------------
launch --> https://services2.passportindia.gov.in/forms/login --> click on register now link
-->select radio CPV Delhi--> enter full name, email, select no radio button --> enter login id
, password and click on signin button.
"""
###############################################################################################
#16/12/2025
"""
element                 absolute xpath
=======                 ==============
UN1                     html/body/div[1]/input[1]
UN2                     html/body/div[1]/input[2]
UN3                     html/body/div[2]/input[1]
UN4                     html/body/div[2]/input[2]
UN1, UN2                html/body/div[1]/input
UN3, UN4                html/body/div[2]/input
UN1, UN3                html/body/div/input[1]
UN2, UN4                html/body/div/input[2]
UN1, UN2, UN3, UN4      html/body/div/input
UN1, UN4                html/body/div[1]/input[1] | html/body/div[2]/input[2]
UN2, UN3                html/body/div[1]/input[2] | html/body/div[2]/input[1]
"""
#drawbck: always it will traverse from parent to its own child
#         it is very lengthy

"""
element                 relative xpath
=======                 ==============
UN1                     //div[1]//input[1]
UN2                     //div[1]//input[2]
UN3                     //div[2]//input[1]
UN4                     //div[2]//input[2]
UN1, UN2                //div[1]//input
UN3, UN4                //div[2]//input
UN1, UN3                //div//input[1]
UN2, UN4                //div//input[2]
UN1, UN2, UN3, UN4      //div//input (or) //input
UN1, UN4                //div[1]//input[1] | //div[2]//input[2] 
UN2, UN3                //div[1]//input[2] | //div[2]//input[1] 
"""
"""
what is the difference b/w absolute xpath and relative xpath
************************************************************
    absolute xpath                      relative xpath
    ==============                      ===============
*indicated by single forward slash(/)   *indicated by double forward slash(//)
*/ -> it will traverse from parent to   *// -> it will traverse from parent to 
its own child                             any child
*xpath is very lengthy                  *xpath is short 
"""

"""
xpath by attribute:
===================
*inspecting an element by specifying attribute in xpath is called as xpath by attribute.

sample html code:
-----------------
<a   href="https://www.gmail.com"   id="a1"   name="n1"> Gmail </a>
              |                        |          |
          attribute1              attribute2   attribute3

syntax:
-------
//tagname[@attribute_name = 'attribute_value']

example:
--------
//a[@href='https://www.gmail.com']
//a[@id='a1']
//a[@name='n1']

xpath to inspect mobile number in goibibo
//input[@name='phone']
xpath to inspect search button
//a[@class='primaryBtn font24 latoBold widgetSearchBtn ']
xpath to inspect signin button in swiggy
//a[@class='_5-C04']

xpath by group by index:
========================
*if xpath is matches with multiple elements to get the particular element then we go
xpath by group by index.
*index will starts from 1.
*write complete xpath in round brackets() and write index in square brackets[]

syntax:
-------
(xpath)[index]

xpath to inspect group tours 
(//a[@href='https://group.gtholidays.in/'])[1]
xpath to inspect mobile number in goibibo
(//input[@type='text'])[5]
//a[@href="https://www.decathlon.in/shop/decathlon-fitness"]

xpath by text() function:
=========================
*inspecting and element by specifying text in xpath is called as xpath by text

sample html code:
-----------------
<a   href="https://www.gmail.com"   id="a1"   name="n1"> Gmail </a>
                                                            \\
syntax:
-------                                                            text
//tagname[text() = 'text_value']
        (or)
//tagname[. = 'text_value']

example:
--------
//a[text() = 'Gmail']
    (or)
//a[.='Gmail']

xpath to inspect search buses in goibibo
//button[text()='Search buses']
        (or)
//button[.='Search buses']
xpath to inspect gym & fitness in decathlon
//span[.='Gym & Fitness']
"""
#############################################################################################
#17/12/2025
#assignment2 solution
"""
driver = Chrome(options=o)
driver.get("https://services2.passportindia.gov.in/forms/login")
driver.maximize_window()
driver.find_element(By.XPATH, "//div[text()='Register Now!']").click()
sleep(2)
driver.find_element(By.XPATH, "//div[text()='CPV Delhi']").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("selenium")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("selenium@gmail.com")
driver.find_element(By.XPATH, "//div[text()='No']").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[4]").send_keys("seleniumautomation")
driver.find_element(By.XPATH, "(//input[@type='password'])[2]").send_keys("seLEnium@123")
driver.find_element(By.XPATH, "//div[text()='Sign Up']").click()
"""
################################################################################################
"""
handling partially dynamic element:
-----------------------------------
*in an element some portion is static and some portion is dynamic is called as partially
dynamic element.
*to handle partially dynamic element we use contains().

when to go contains() function?
-------------------------------
*to handle partially dynamic element.
*if text value/attribute value is very lengthy.
*if text value begins/ends with spaces.
*if text contains &nbsp

contains with attribute syntax:
-------------------------------
//tagname[contains(@attribute_name , 'attribute_value')]

contains with text:
-------------------
//tagname[contains(. , 'text_value')]

xpath to inspect windows version
(//span[contains(., 'Get Windows')])[1]

xpath to inspect python version in python.org
(//a[contains(., 'Download Python')])[2]

xpath to inspect fruits and vegetables in zepto
(//span[contains(@class , 'Label-sc-15v1nk5-0')])[9]

xpath to inspect mobile in amazon
//a[contains(@href, '/mobile-phones/')]

xpath to inspect power bank in dunnzo
//h5[contains(., '20000 mAh')]

xpath to inspect admissions in jain.com
(//a[contains(., 'Admissions')])[3]

xpath to inspect books in demo webshop
(//a[contains(.,'Books')])[1]
"""
"""
assignment3:
------------
launch https://www.crocs.in/ --> click on register icon --> click on signin/register link
--> click on create account --> enter values for all mandatory fields and click on register button

send assignment to below mail-id:
---------------------------------
assignmentsql@gmail.com
"""
################################################################################################
#18/12/2025
"""
handling completely dynamic element:
------------------------------------
*an element is completely changing then it is called as completely dynamic element.
*we can handle in 2 ways,
    1.xpath by traversing
    2.xpath by siblings

1.xpath by traversing:
======================
*navigating from one element to another element is called as traversing.
*traversing is classified into 2 types,
1.forward traversing
2.backward traversing

1.forward traversing:
---------------------
*navigating from parent to child element by using / (or) // is called as forward traversing.

2.backward traversing:
----------------------
*navigating from child to parent element by using /.. (or) //ancestor is called as backward traversing.

how to handle completely dynamic element:
=========================================
step1: inspect static element 
step2: navigate from static element to common parent(common parent means it should be a parent of
both static and dynamic element)
step3: navigate from common parent to dynamic element
"""
#sample html code
"""
<html>
          <body>		
	        <table border=3>
	             <tr>
                    <td>sl.no</td>
                    <td>certificate</td>
                    <td>movie name</td>
                    <td>collection</td>
                    <td>rating</td>
	             </tr>
	             <tr>
                    <td>1</td>
                    <td>U</td>
                    <td>Kantara</td>
                    <td>800CR</td>
                    <td>*****</td>
	            </tr>	
	             <tr>
                    <td>2</td>
                    <td>U/A</td>
                    <td>Pushpa2</td>
                    <td>80CR</td>
                    <td>**</td>
	            </tr>
	             <tr>
                    <td>3</td>
                    <td>U/A</td>
                    <td>KGF</td>
                    <td>100CR</td>
                    <td>***</td>
	            </tr>
	             <tr>
                    <td>4</td>
                    <td>A</td>
                    <td>Coolie</td>
                    <td>300CR</td>
                    <td>****</td>
	            </tr>
	        </table>
          </body>	
</html>
"""
################################################################################################
"""
xpath to inspect collection of kantara movie
(//td[.='Kantara']/..//td)[4]

xpath to inspect ratings of pushpa2 movie
(//td[.='Pushpa2']/..//td)[5]

xpath to inspect sl.no of kgf movie
(//td[.='KGF']/..//td)[1]

xpath to inspect stock price of nifty bank
(//p[.='NIFTY BANK']/..//h3)[2]

xpath to inspect trp of sun tv channel
(//td[contains(., 'Sun TV')]/..//td)[3]	

xpath to inspect version of python 
(//p[.='Python']/..//a)[1]
"""
##############################################################################################
"""
assignment question:
====================
https://www.accuweather.com/en/in/india-weather
inspect weather of Bengaluru

https://www.goodreturns.in/gold-rates/
inspect price of 22K gold
"""
#################################################################################################
#19/12/2025
"""
2.xpath by siblings
===================
*a child under a common parent is called as siblings.
*is used to navigate from one child element to another child element.
*there are 2 types of sibling tags,
1.following sibling:
********************
*traversing from a child element(static) to below(younger)siblings is called as following sibling.
syntax:-
========
//following-sibling::tag-name

2.preceding sibling:
********************
*traversing from a child element(static) to above(elder)siblings is called as preceding sibling.
syntax:-
========
//preceding-sibling::tag-name

sample html-code:
*****************
                    preceding sibling
<tr>                    ^
    <td>1</td>          |   -->2
    <td>U/A</td>        |   -->1
    <td>Kantara</td>---->static-element
    <td>100CR</td>      |   -->1    
    <td>kan</td>        |   -->2
    <td>*****</td>      |   -->3
</tr>                   V
                    following sibling

steps to follow siblings
========================
step1: inspect static element
step2: check for static element dynamic element should be sibling

#xpath to inspect kantara collection in demo website
(//td[.='Kantara']//following-sibling::td)[1]
#xpath to inspect pushpa sl.no in demo website
(//td[.='Pushpa']//preceding-sibling::td)[1]
#xpath to inspect stock price of nifty next 50 in nse
(//p[.='NIFTY NEXT 50'])[2]//following-sibling::h3
#xpath to inspect stable version of python
(//p[.='Python']//following-sibling::p)[1]//a
#xpath to inspect bengaluru weather
//span[.='Bengaluru']//following-sibling::span
#xpath to inspect price of 24k gold
//p[contains(., '24K')]/..//following-sibling::div//span

ancestor:
---------
*navigate from child to any parent then we go ancestor.

syntax:
-------
    //ancestor::tagname

#xpath to navigate from pushpa to html
//td[.='Pushpa']//ancestor::html
#xpath to navigate from pushpa to tbody
//td[.='Pushpa']//ancestor::tbody
#xpath to navigate from pushpa to own parent
//td[.='Pushpa']//ancestor::tr
"""
#xpath by axes
#following-sibling, preceding-sibling, ancestor are called as xpath by axes
#####################################################################################################
"""
assignment
----------
https://www.nseindia.com/
inspect stock price of NIFTY NEXT 50

xpath to inspect no. of likes for a any video in youtube
xpath to inspect no. of subscribers of any channel in youtube
xpath to inspect price of any product in amazon
"""
################################################################################################
#23/12/2025 --->Day 09
"""
web-element methods:
********************
"""
"""
*find-element() method return type is web-element.
*a element present in a webpage is called as web-element.
syntax:
-------
var_name = driver.find_element("locator_name", "locator_value")
  |
webelement

methods:
--------
*click():       
    *it will perform click on action on web-element.
*send_keys():
    *it will send/enter a data in text/text area field.
clear():
    *it is used to clear/remove value from text/text area field.
is_enabled():
    *it will return True if element is enabled else return False.
is_selected():  
    *it will return True if check box/radio button is selected else it will return False.
    *only if default radio/check box if selected it will work and it should be developed by input.
is_displayed():
    *it will return if the element is present/visible/displayed in webpage else it will throw NoSuchElement Exception.
"""
#ws to send "hello" in UN text-field and clear the value in UN text field
"""
driver =  Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
username = driver.find_element("id", "email")
username.send_keys("selenium")
username.clear()
username.send_keys("python selenium")
"""
#ws to check an element is enabled/disabled
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/E7batch.html")
driver.maximize_window()
un1 = driver.find_element("id", "a1")
print(un1.is_enabled())             #True
un2 = driver.find_element("id", "a2")
print(un2.is_enabled())             #False
"""
#ws to verify register now and upload resume is enaboled/not
"""
driver = Chrome(options=o)
driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
driver.maximize_window()
login = driver.find_element("xpath", "//button[.='Register now']")
print(login.is_enabled())           #False
"""
#wsto verif the checkbox is selected or not
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/E7batch.html")
driver.maximize_window()
check1 = driver.find_element("id", "c1")
print(check1.is_selected())         #False
check2 = driver.find_element("id", "c2")
print(check2.is_selected())         #True
"""
#wsto verif the radio button is selected or not in ksrtc.com
"""
driver = Chrome(options=o)
driver.get("https://ksrtc.in/")
driver.maximize_window()
check1 = driver.find_element(By.ID, "radio_oneway")
check2 = driver.find_element(By.ID, "radio_roundtrip")
print(check1.is_selected())             #True
print(check2.is_selected())             #False
"""
#ws to verify google and gmail link is present or not
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/E7batch.html")
driver.maximize_window()
link1 = driver.find_element("id", "l1")
print(link1.is_displayed())         #False
link2 = driver.find_element("id", "l2")
print(link2.is_displayed())         #True
"""
"""
get_attribute():
    *it will return the value of specified attribute name.
    *if th attribute name is invalid then it will return None.
    *we need to write/use locator both getting attribute value and inspecting should be under a same tag/html code.
    *most of we use this method for getting tool-tip.

size:
    *it will return dictionary of height and width.
location:
    *it will return dictionary of x and y axis.
rect:   
    *it will return dictionary of height, width, x and y axis.
text:
    *it will return a text of an element.
tag_name:    
    *it will return a tag-name of an element.
"""
#ws to get the text value of google link
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/E7batch.html")
driver.maximize_window()
link2 = driver.find_element("id", "l2")
print(link2.text)               #Google
"""
#ws to get the text value of red velvet cake from amma's pastries
"""
driver = Chrome(options=o)
driver.get("https://ammaspastries.in/")
driver.maximize_window()
link2 = driver.find_element("xpath", "(//a[contains(@href, '/red-velvet/')])[2]")
print(link2.text)               #Red Velvet
"""
#ws to extract and print tag name of red velvet cake from amma's pastries
"""
driver = Chrome(options=o)
driver.get("https://ammaspastries.in/")
driver.maximize_window()
link2 = driver.find_element("xpath", "(//a[contains(@href, '/red-velvet/')])[2]")
print(link2.tag_name)               #a
"""
#ws to verify pizza element text is present in webpage or not
"""
driver = Chrome(options=o)
driver.get("https://www.zomato.com/bangalore/delivery")
driver.maximize_window()
pizza = driver.find_element(By.XPATH, "//a[@href='/bangalore/delivery/dish-pizza']")
print(pizza.text)
if pizza.text == 'Pizza':
    print("Pizza element is present in application")
else:
    print("Pizza element is not present in application")
"""
#sample html code for enabled, selected, displayed method elements
"""
<html>
           <body bgcolor="pink">	
               	UN1:<input type="text"  id="a1">
               	UN2:<input type="text"  id="a2" disabled><hr/>
	            <input type="checkbox" id="c1">Old user
	            <input type="checkbox" id="c2" checked>New user<hr/>
	            <a href="https://www.gmail.com" id="l1" style="display: none;">Gmail</a>
	            <a href="https://www.google.com" id="l2">Google</a>
           </body>
</html>

"""
"""
assignemnt:
***********
ws to verify create account and continue with google is enabled/not in zomato --> signup.
https://www.zomato.com/bangalore
ws select CPV delhi and verify cpv delhi radio button is selected or not
https://portal2.passportindia.gov.in/AppOnlineProject/user/RegistrationBaseAction?request_locale=en
ws to verify enter mobilenumber text field is displayed or not then enter number and check verify button and enter
OTP field is displayed or not in flipkart.com
https://www.flipkart.com/
"""
############################################################################################################
#ws to print tooltip of english in wikipedia
"""
driver = Chrome()
driver.get("https://www.wikipedia.org/")
driver.maximize_window()
eng = driver.find_element("xpath", "//a[@id='js-link-box-en']")
tooltip = eng.get_attribute("title")
print(tooltip)
#English — Wikipedia — The Free Encyclopedia
"""

#ws to print google apps tooltip
"""
driver = Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
eng = driver.find_element("xpath", "//a[@aria-label='Google apps']")
tooltip = eng.get_attribute("aria-label")
print(tooltip)
#Google apps
"""

#example on getting invalid attribute value.
"""
driver = Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
eng = driver.find_element("xpath", "//a[@aria-label='Google apps']")
tooltip = eng.get_attribute("aria-label-name")
print(tooltip)
#None
"""

#ws to get x,y axis and height,width of an element
"""
driver = Chrome()
driver.get("https://www.fb.com/")
driver.maximize_window()
un = driver.find_element("id", "email")
l = un.location
print(l)
#{'x': 780, 'y': 148}
s = un.size
print(s)
# {'height': 52, 'width': 364}
r = un.rect
print(r)
# {'height': 52, 'width': 364, 'x': 780.5, 'y': 148}
"""

#ws to get the text value of about wipro
"""
driver = Chrome()
driver.get("https://www.wipro.com/")
driver.maximize_window()
about = driver.find_element("xpath", "(//a[contains(., 'About')])[1]")
print(about.text)
# About Wipro
"""

#ws to verify error message is displaying or not
"""
driver = Chrome()
driver.get("http://localhost/login.do")
log_btn = driver.find_element("xpath", "//div[.='Login ']")
log_btn.click()
error = driver.find_element("xpath", "(//span[@class='errormsg'])[1]")
if error.text=="Username or Password is invalid. Please try again.":
    print("error message is displaying")
else:
    print("error message is not displaying")
"""

#ws to get the tag name of login button
"""
driver = Chrome()
driver.get("http://localhost/login.do")
log_btn = driver.find_element("xpath", "//div[.='Login ']")
print(log_btn.tag_name)
#div
"""
##############################################################################################
#24/12/2025 --->Day 10
"""
handling drop-down:
*******************
"""
"""
*a collection of options is called as drop-down.
*drop-down classified into 2 types,
    1.standard drop-down
    2.Non-standard drop-down

1.standard drop-down:
*********************
*a drop-down is developed by "select" tag is called as standard drop-down.
*standard drop-down is classified into 2 types,
1.single select drop down(SSDD):
********************************
    *we can select only single option.
    *we can't select multiple option.
    *we can't deselect option.

2.multi select drop down(MSDD):
*******************************
    *we can select single option
    *we can select multiple option.
    *we can deselect option.

how to automate standard DD
===========================
*to automate standard dropdown we use "Select" class.
*select class constructor will accept one argument that is drop-down address/web-element.
*need to import Select class from below.

from selenium.webdriver.support.select import Select

class Select:
    def __init__(self, WebElement):
        ...

s = Select(DD_address/DD_webelement)

*to select an option we have 3 methods,
1.select_index(int) --> need to pass index, index starts from 0
2.select_by_value(string) --> value attribute value we need to pass
3.select_by_visible_text(text) --> text of an option

*to deselect an option we have methods,
1.deselect_index(int) --> need to pass index, index starts from 0
2.deselect_by_value(string) --> value attribute value we need to pass
3.deselect_by_visible_text(text) --> text of an option
4.deselect_all()
"""
# sample html code of developing drop-down
"""
<html>
           <body bgcolor="pink">	
               	Subject:<select id="s1">
	              <option value="v1">Sql</option>	
	              <option value="v2">Selenium</option>	
	              <option value="v3">Python</option>	
	              <option value="v4">Manual</option>	
	              <option value="v5">API</option>	
	            </select>
               	Topic:<select id="s2" multiple>
	              <option value="v11">Query</option>	
	              <option value="v22">Scripts</option>	
	              <option value="v33">Programs</option>	
	              <option value="v44">SDLC</option>	
	              <option value="v55">Defect</option>	
	            </select>
           </body>
</html>

"""
from selenium.webdriver.support.select import Select

# single select drop-down(SSDD)
# ws to select option from SSDD
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/E7batch.html")
driver.maximize_window()
sub = driver.find_element("id", "s1")
s = Select(sub)
s.select_by_index(2)
s.select_by_value("v4")
s.select_by_visible_text("Selenium")
"""
# example on index not matches
"""
driver = Chrome()
driver.get("file:///C:/Users/Admin/Desktop/sample.html")
driver.maximize_window()
dd = driver.find_element("id", "a1")        
s = Select(dd)
s.select_by_index(10)
#NoSuchElementException: Message: Could not locate element with index 10
"""
# multi select drop down
# ws to select options in MSDD
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/E7batch.html")
driver.maximize_window()
top = driver.find_element("id", "s2")
s = Select(top)
s.select_by_index(1)
s.select_by_value("v44")
s.select_by_visible_text("Query")
"""
# ws to select and deselct options from MSDD
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/E7batch.html")
driver.maximize_window()
top = driver.find_element("id", "s2")
s = Select(top)
s.select_by_index(1)
s.select_by_value("v44")
s.select_by_visible_text("Query")
sleep(2)
s.deselect_by_index(3)
s.deselect_by_value("v11")
s.deselect_by_visible_text("Scripts")
"""
# example on deselcting option from SSDD
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/E7batch.html")
driver.maximize_window()
sub = driver.find_element("id", "s1")
s = Select(sub)
s.select_by_index(2)
sleep(2)
s.deselect_by_index(2)
#NotImplementedError: You may only deselect options of a multi-select
"""
#ws to select date, month, year from dd
"""
driver = Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element("link text", "Create new account").click()
sleep(2)
day_dd = driver.find_element("id", "day")
s = Select(day_dd)
s.select_by_index(14)
month_dd = driver.find_element("id", "month")
s = Select(month_dd)
s.select_by_value("8")
year_dd = driver.find_element("id", "year")
s = Select(year_dd)
s.select_by_visible_text("2022")
"""

"""
is_multiple:
   *it will return True if a drop-down is MSDD else it will return None.
options:
    *it will return list specified drop-down web-element(option) address.
    *to get the correct output we should run for loop and use .text property of web-element.
    *it will work for both single select and multi select drop-down.
all_selected_options:   
    *it will return list all select options from specified drop-down web-element(option) address.
    *to get the correct output we should run for loop and use .text property of web-element.
    *it will work for both single select and multi select drop-down but it's prefferd to use for multi select drop-down.
"""
#ws to check dropdown is multi select or not
"""
driver = Chrome()
driver.get("file:///C:/Users/Admin/Desktop/sample.html")
driver.maximize_window()
sdd = driver.find_element("id", "a1")               #sdd --> single select drop down address
mdd = driver.find_element("id", "a2")               #mdd --> multi select drop-down address
s1 = Select(sdd)
s2 = Select(mdd)
print(s1.is_multiple)           #None
print(s2.is_multiple)           #True
"""

#ws to print all options of a dropdown
"""
driver = Chrome()
driver.get("file:///C:/Users/Admin/Desktop/sample.html")
driver.maximize_window()
sdd = driver.find_element("id", "a1")
s = Select(sdd)
ops = s.options
print(ops)
#[<selenium.webdriver.remote.webelement.WebElement (session="b0d2594914d1b476228fba05b6c97e7c", element="FA8E7F8FAA2F92C124945E72FCAF6449_element_4")>, <selenium.webdriver.remote.webelement.WebElement (session="b0d2594914d1b476228fba05b6c97e7c", element="FA8E7F8FAA2F92C124945E72FCAF6449_element_6")>, <selenium.webdriver.remote.webelement.WebElement (session="b0d2594914d1b476228fba05b6c97e7c", element="FA8E7F8FAA2F92C124945E72FCAF6449_element_8")>, <selenium.webdriver.remote.webelement.WebElement (session="b0d2594914d1b476228fba05b6c97e7c", element="FA8E7F8FAA2F92C124945E72FCAF6449_element_10")>, <selenium.webdriver.remote.webelement.WebElement (session="b0d2594914d1b476228fba05b6c97e7c", element="FA8E7F8FAA2F92C124945E72FCAF6449_element_12")>]
"""
#wsto print all the options from DD
"""
driver =  Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/E7batch.html")
driver.maximize_window()
sub = driver.find_element("id", "s1")
s1 = Select(sub)
eles = s1.options   #eles=[webele1, webele2, webele3, .. ]
for i in eles:
    print(i.text)
"""
#ws to print all selected options from multi select drop-down
"""
driver =  Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/E7batch.html")
driver.maximize_window()
top = driver.find_element("id", "s2")
s2 = Select(top)
s2.select_by_index(0)
s2.select_by_index(2)
s2.select_by_index(3)
eles = s2.all_selected_options
for i in eles:
    print(i.text)
"""

"""
assignment question:
--------------------
https://www.landrecords.karnataka.gov.in/service2/RTC.aspx
launch above application select option from district > taluk > hobli > village dd
"""


####################################################################################################
#25/12/2025 --->Day 11
#find_elements():
#----------------
"""
*it is used to find multiple elements.
*the return type of find_elements() is list of webelement.
*if the locator value not matches with any element then it will return empty list[].
*to get the correct o/p we should run for loop and .text property

syntax: var_name = driver.find_elements("locator_name", "locator_value")
            |
        list of web-elemet  
"""
#sample html code
"""
<html>
             <body>	
	<a href="https://www.gmail.com" id="a1">Gmail</a>
	<a href="https://www.google.com" id="a2">Google</a>
	<a href="https://www.instgram.com" id="a3">Instagram</a>
	<a href="https://www.wikipedia.com" id="a4">Wikipedia</a>
             </body>
</html>
"""

#ws to print all link text present in demo webpage
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/demo.html")
driver.maximize_window()
ops = driver.find_elements("tag name", "a")    #ops = [webelement1, webelement2, ..]
for i in ops:
    print(i.text)
# Gmail
# Youtube
"""

#example on locator value not matches with any element
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/demo.html")
driver.maximize_window()
ops = driver.find_elements("tag name", "b")    #ops = [webelement1, webelement2, ..]
print(ops)
#[]
"""

#ws to print total no. of links present in amazon webpage
"""
driver = Chrome(options=o)
driver.get("https://www.amazon.in/")
driver.maximize_window()
ops = driver.find_elements("xpath", "//a")
print(len(ops))         #338
"""

"""
xpath to to count total no. of links
//a
xpath to to count total no. of images
//img
xpath to to count total no. of text fields
//input
xpath to to count total no. of drop down
//select
"""

"""
what is the difference b/w find_element() and find_elements()
=============================================================
            find_element                    find_elements
            ------------                    -------------
*it is used to find single element      *it is used to find multiple elements
*return type is webelement              *return type is list of webelements
*if the locator value matches with      *if the locator value matches with
multiple elements then it will return   multiple elements then it will return
1st element address                     all elements address
*if locator value not matches           *if locator value not matches then it 
then it will throw NoSuchElement        will return empty list []
exception
"""
#ws to print auto suggestion of google
"""
driver = Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element("name", "q").send_keys("python selenium")
sleep(2)
ops = driver.find_elements("xpath", "//div[@class='lnnVSe']")
for i in ops[:10]:
    print(i.get_attribute("aria-label"))
"""
#ws toprint travel info in bmrcl
"""
driver = Chrome(options=o)
driver.get("https://english.bmrc.co.in/")
driver.maximize_window()
sleep(2)
driver.find_element("xpath", "//span[.='English']").click()
driver.find_element("xpath", "//a[.='TRAVEL INFO']").click()
ops = driver.find_elements("xpath", "(//li[@class='nav-item'])[11]//a")
for i in ops:
    print(i.text)
"""
#ws to print all biryani name in zomato
"""
driver = Chrome(options=o)
driver.get("https://www.zomato.com/bangalore/restaurants")
driver.maximize_window()
search = driver.find_element("xpath", "//input[@placeholder='Search for restaurant, cuisine or a dish']")
search.send_keys("biryani")
search.click()
sleep(3)
results = driver.find_elements(By.XPATH, "//p[@class='sc-1hez2tp-0 sc-gFXMyG jkvifB']")
for i in results:
    print(i.text)
"""

"""
assignment
----------
ws to print all the options from all drop-down in amazon
https://www.amazon.in/ref=nav_logo

ws to search for shirt > print all the suggestions in amazon
https://www.amazon.in/ref=nav_logo
"""
###########################################################################################################
"""
action chains class:
--------------------
*action chains class used for following uses,
1.mouse hover action
2.drag and drop 
3.double click
4.right click

*action chains class shoul import from below
    from selenium.webdriver.common.action_chains import ActionChains

class ActionChains:
    def __init__(self, driver):
        ...

a = ActionChains(driver)

note:any method of action chains class should be end with .perform() method
"""

#1.mouse hover action:
#---------------------
#keeping a cursor on an element is called as mouse hover action
# syntax: a.move_to_element(web_element).perform()

from selenium.webdriver.common.action_chains import ActionChains

#ws to mouse hover on men and click on jeans link
"""
driver = Chrome(options=o)
driver.get("https://www.ajio.com/")
driver.maximize_window()
men = driver.find_element("xpath", "//span[.='MEN']")
a = ActionChains(driver)
a.move_to_element(men).perform()
driver.find_element("xpath", "//a[.='Jeans']").click()
"""
#ws to mouse hover on baby tab in mamaearth
"""
driver = Chrome(options=o)
driver.get("https://mamaearth.in/")
driver.maximize_window()
baby = driver.find_element("xpath", "//a[text()='Baby']")
a = ActionChains(driver)
a.move_to_element(baby).perform()
"""

###############################################################################################
#2.drag and drop:
#----------------
#dragging an element from position and dropping to another position is called as
# drag and drop
#syntax: a.drag_and_drop(src_webelement, dest_webelement)

#ws to drag and drop
"""
driver = Chrome(options=o)
driver.get("https://pschool.in/science-3-sc/drag-drop-organs")
driver.maximize_window()
src1 = driver.find_element("xpath", "//div[.='Brain']")
dest1 = driver.find_element("xpath", "(//div[@class='blank '])[1]")
a = ActionChains(driver)
a.drag_and_drop(src1, dest1).perform()
src2 = driver.find_element("xpath", "//div[.='Heart']")
dest2 = driver.find_element("xpath", "(//div[@class='blank '])[2]")
a.drag_and_drop(src2, dest2).perform()
"""
#############################################################################################
#3.double click:
#---------------
# when ever we want to double click on an element then we use below methods of action
#chains class.
# syntax: a.double_click(web_element).perform()

#ws to double click in demo webapplication
"""
driver = Chrome(options=o)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
double = driver.find_element("xpath", "//button[.='Double-Click Me To See Alert']")
a = ActionChains(driver)
a.double_click(double).perform()
"""
###############################################################################################
#4.right click:
#to right on an element in a webpage we use below method.
#syntax: a.context_click(webelement).perform()

#wsto right click on study material in byjus
"""
driver = Chrome(options=o)
driver.get("https://byjus.com/")
driver.maximize_window()
study = driver.find_element("link text", "Study Materials")
a = ActionChains(driver)
a.context_click(study).perform()
"""
"""
assignment:
-----------
launch --> https://english.bmrc.co.in/ --> click on english button --> mouse hover on travel-info 
element --> print all the suggestion/options.
"""

#########################################################################################################
#29/12/2025 ---> Day 13
"""
handling frames:
----------------
*a webpage inside another webpage is called as frames/nested frames/embedded webpage.
*to develop a frame developer will use <iframe> tag.
*by default control will present in parent webpage, we need to switch control from
parent to child webpage will use following method.
    driver.switch_to.frame(arg)
*frame() method will accept 3 different types of arguments,
    *index : starts from 0
    *name : name attribute value
    *webelement : address of a frame
*to switch control from child to parent there are 2 methods are present,
    driver.switch_to.parent_frame() -->it switch from child to its own parent
    driver.switch_to.default_content() ->it will switch from child to main parent(ancestor)
*frame() method is an example for polymorphism.
*if argument(index/name/webelement) is not matches then it will throw "NoSuchFrameException" 
"""
#ws to enter hello in UN1 and bye in UN2
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/parent.html")
driver.maximize_window()
un1 = driver.find_element("id", "a1")
un1.send_keys("hello")
un2 = driver.find_element("id", "a2")
un2.send_keys("bye")
#NoSuchElementException
#according to above script the control is present in parent webpage, we need to switch 
control from parent to child webpage.
"""
#ws to enter hello in UN1, bye in UN2, good in UN3 by using index as argument
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/parent.html")
driver.maximize_window()
un1 = driver.find_element("id", "a1")
un1.send_keys("hello")
driver.switch_to.frame(0)
un2 = driver.find_element("id", "a2")
un2.send_keys("bye")
driver.switch_to.frame(0)
un3 = driver.find_element("id", "a3")
un3.send_keys("good")
"""
#ws to enter hello in UN1, bye in UN2, good in UN3 by using name as argument
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/parent.html")
driver.maximize_window()
un1 = driver.find_element("id", "a1")
un1.send_keys("hello")
driver.switch_to.frame("n1")
un2 = driver.find_element("id", "a2")
un2.send_keys("bye")
driver.switch_to.frame("n2")
un3 = driver.find_element("id", "a3")
un3.send_keys("good")
"""
#ws to enter hello in UN1, bye in UN2, good in UN3 by using webelement as argument
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/parent.html")
driver.maximize_window()
un1 = driver.find_element("id", "a1")
un1.send_keys("hello")
frame1 = driver.find_element("xpath", "//iframe[@id='f1']")
driver.switch_to.frame(frame1)
un2 = driver.find_element("id", "a2")
un2.send_keys("bye")
frame2 = driver.find_element("xpath", "//iframe[@id='f2']")
driver.switch_to.frame(frame2)
un3 = driver.find_element("id", "a3")
un3.send_keys("good")
"""
#example on switching control from child to its own parent
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/parent.html")
driver.maximize_window()
un1 = driver.find_element("id", "a1")
un1.send_keys("hello")
frame1 = driver.find_element("xpath", "//iframe[@id='f1']")
driver.switch_to.frame(frame1)
un2 = driver.find_element("id", "a2")
un2.send_keys("bye")
frame2 = driver.find_element("xpath", "//iframe[@id='f2']")
driver.switch_to.frame(frame2)
un3 = driver.find_element("id", "a3")
un3.send_keys("good")
driver.switch_to.parent_frame()
un2.send_keys("back to parent")
"""
#example on switching control from child to main parent(ancestor)
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/parent.html")
driver.maximize_window()
un1 = driver.find_element("id", "a1")
un1.send_keys("hello")
frame1 = driver.find_element("xpath", "//iframe[@id='f1']")
driver.switch_to.frame(frame1)
un2 = driver.find_element("id", "a2")
un2.send_keys("bye")
frame2 = driver.find_element("xpath", "//iframe[@id='f2']")
driver.switch_to.frame(frame2)
un3 = driver.find_element("id", "a3")
un3.send_keys("good")
driver.switch_to.default_content()
un1.send_keys("back to main parent")
"""
#################################################################################################
#example on NoSuchFrameException
"""
driver = Chrome(options=o)
driver.get("file:///C:/Users/Hp/Desktop/parent.html")
driver.maximize_window()
un1 = driver.find_element("id", "a1")
un1.send_keys("hello")
driver.switch_to.frame(10)
un2 = driver.find_element("id", "a2")
un2.send_keys("bye")
#NoSuchFrameException
"""
#ws to click on signup with google button in x.com
"""
driver = Chrome(options=o)
driver.get("https://x.com/nopCommerce")
driver.maximize_window()
sleep(4)
sign_frame = driver.find_element("xpath", "//iframe[contains(@title, 'Google')]")
driver.switch_to.frame(sign_frame)
driver.find_element("xpath", "//span[.='Sign up with Google']").click()
"""
##############################################################################################

"""
assignment
----------
open https://www.zomato.com/bangalore/restaurants > click on login button > click on sign in with google
"""

###########################################################################################################
#30/12/2025 ---> Day 14
"""
assert:
-------
*assert is a keyword it is used for conditional checking.
*we will specify the condition in assert, id condition is True then it will continue
the execution, if condition become False then it will stop the execution and throw
"AssertionError".
syntax: assert condition, ["message"]
"""

#example on assert condition True
"""
assert 10==10, "number not matches"
print("same")
print("end")
# same
# end
"""
#example on assert condtion False
"""
assert 10==100, "number not matches"
print("same")
print("end")
#AssertionError: number not matches
"""

###############################################################################################
"""
taking screenshot:
------------------
*while testing if TE find any defect then will take screenshot, because it is a proof
to show for developer we got defect.
*in selenium to take screenshot we have below method.
    driver.save_screenshot("filename.png") 
*by default it will save in current location.
*if we want to save in particular location then need to specify the path.
"""

#ws to save a screenshot(it will save in current location)
"""
driver = Chrome(options=o)
driver.get("https://www.redbus.in/")
driver.maximize_window()
driver.save_screenshot("defect1.png")
"""

#ws to save a screenshot in screenshot folder
"""
file_path = "C:\\Users\\Hp\\PycharmProjects\\SeleneiumE7\\screenshots"
driver = Chrome(options=o)
driver.get("https://www.redbus.in/")
driver.maximize_window()
driver.save_screenshot(f"{file_path}\\defect.png")
"""
#extracting current date and time
"""
from datetime import datetime

d = datetime.now()
print(d)                #2025-07-24 20:35:43.112124
d = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
print(d)                #24-07-2025 20-38-27
"""
from datetime import datetime

#saving screenshot with current date and time
"""
d = datetime.now().strftime("%d-%m-%Y %H-%M-%S")

file_path = "C:\\Users\\Hp\\PycharmProjects\\SeleneiumE7\\screenshots"
driver = Chrome(options=o)
driver.get("https://www.redbus.in/")
driver.maximize_window()
driver.save_screenshot(f"{file_path}\\{d}.png")
"""
#real time example on assert and screenshot
"""
step1: open the browser and enter URl           welcome page should display
step2: click on medicine tab                    buy medicine page should display
step3: search a medicine and select             order medicine page should display
step4: click on add to cart, select a qty       cart page should display 
        and click on view cart 
step5: click on add delivery address, 
        enter mobile number and click on OTP
"""
"""
d = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
driver = Chrome(options=o)
driver.get("https://pharmeasy.in/")
driver.maximize_window()
assert driver.title == "PharmEasy – Online Pharmacy & Medical Store with Healthcare Services in India | 50 Lakhs+ Customers", driver.save_screenshot(f"C:\\Users\\Hp\\PycharmProjects\\M18_selenium79AM\\screenshots\\{d}.png")
driver.find_element("xpath", "(//a[text()='Medicine'])[2]").click()
assert driver.title == "Buy Medicines Online - Up to 24% OFF | Fast Delivery by PharmEasy", driver.save_screenshot(f"C:\\Users\\Hp\\PycharmProjects\\M18_selenium79AM\\screenshots\\{d}.png")
driver.find_element("xpath", "//span[text()='Search for Medicines...']").click()
driver.find_element("xpath", "//input[@type='text']").send_keys("dolo 650")
sleep(3)
driver.find_element("xpath", "(//div[text()='Dolo 650'])[1]").click()
assert driver.title == "Order DOLO 650 Online - PharmEasy", driver.save_screenshot(f"C:\\Users\\Hp\\PycharmProjects\\M18_selenium79AM\\screenshots\\{d}.png")
driver.find_element("xpath","//button[.='Add To Cart']").click()
driver.find_element("xpath","//li[text()='1']").click()
driver.find_element("xpath","//span[text()='View Cart']").click()
sleep(3)
assert driver.title == "Order Medicines Online - Cart - PharmEasy", driver.save_screenshot(f"C:\\Users\\Hp\\PycharmProjects\\M18_selenium79AM\\screenshots\\{d}.png")
driver.find_element("xpath", "//span[text()='Add Delivery Address']").click()
driver.find_element("id", "mobile").send_keys("9988776655")
driver.find_element("xpath", "//button[text()='Send OTP']").click()
"""
"""
assignment on assert and take screenshot
launch https://medlineplus.gov/ > click on genetics > click on genetic conditions > click on see Triple A syndrome  
> Autonomic Nervous System Disorders > Find an Expert 
"""

###########################################################################################################
#31-12-2025 ---> Day 15
"""
handling popup's
----------------
*a popup is a small window/small tab.
*popups are classified into 5 types,
1.alert and confirmation/java script popup
2.hidden division popup
3.file upload popup
4.file download popup
5.child browser popup 
6.notification popup
"""
#1.alert and confirmation/java script popup
"""
*a popup which consisting of "OK/Cancel" button thn it is called as alert and confirmation popup.
*it is classified into 2 types,
1.simple alert : a alert which consist of either "OK"/"Cancel" button.
2.alert and confirmation : a alert which consist of both "OK and Cancel" button.

*to automate alert and confirmation popup, first we need to switch control from webpage
 to alert.
*we use below method for handling alert,
    driver.switch_to.alert
*to click on OK button we use accept()
*to click on Cancel button we use dismiss()

characteristics of alert and confirmation:
-----------------------------------------
*we can't inspect the popup
*we can't move/drag the popup

note:
-----
we can't use both accept() and dismiss() method for single alert, if we use then it will
throw "NoAlertPresentException".
"""
#ws to handle simple alert
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//input[@value='Search']").click()
a = driver.switch_to.alert
a.accept()
"""
#ws to click on ok button in alert and confirmartion popup
"""
driver = Chrome(options=o)
driver.get("https://licindia.in/")
driver.maximize_window()
driver.find_element("xpath", "//a[@title='Login']").click()
a = driver.switch_to.alert
a.accept()
"""
#ws to click on cancel button in alert and confirmartion popup
"""
driver = Chrome(options=o)
driver.get("https://licindia.in/")
driver.maximize_window()
driver.find_element("xpath", "//a[@title='Login']").click()
a = driver.switch_to.alert
a.dismiss()
"""
#example on using both accept and dismiss method
"""
driver = Chrome(options=o)
driver.get("https://licindia.in/")
driver.maximize_window()
driver.find_element("xpath", "//a[@title='Login']").click()
a = driver.switch_to.alert
a.accept()
a.dismiss()
#NoAlertPresentException
"""
#ws to print text of a popup
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//input[@value='Search']").click()
a = driver.switch_to.alert
print(a.text)
#Please enter some search keyword
"""
########################################################################################
#2.hidden division popup
"""
*initially a popup will be hidden, if we perform any action then a popup will be appear 
this is called as hidden division popup.
*will automate this popup by find_element(), click(), send_keys() methods.

characteristics of alert and confirmation:
-----------------------------------------
*we can inspect the popup
*we can't move/drag the popup
"""
#ws to enter mobile number in redbus login page
"""
driver = Chrome(options=o)
driver.get("https://www.redbus.in/")
driver.maximize_window()
driver.find_element("xpath", "//div[.='Account']").click()
sleep(2)
driver.find_element("xpath", "//button[.='Log in']").click()
sleep(2)
driver.find_element("xpath", "//input[@inputmode='numeric']").send_keys("9988776655")
"""
#ws to generate a otp in mamaearth
"""
driver = Chrome(options=o)
driver.get("https://mamaearth.in/")
driver.maximize_window()
driver.find_element("xpath", "//div[.='Login']").click()
sleep(2)
driver.find_element("xpath", "//input[@type='number']").send_keys("9988776655")
driver.find_element("xpath", "//button[.='Login with OTP']").click()
"""
#########################################################################################
"""
Assignment
open https://passbook.epfindia.gov.in/MemberPassBook/login > click on login button > handle the popup

open https://www.amazon.in/ref=nav_logo > click on all button > click on best seller > click on any product
> click on add to cart > click on proceed to buy
"""

######################################################################################################
#01/01/2026 ---> Day 16
#3.file upload popup
"""
*uploading a file in webpage is called as file upload popup
*to automate this popup we use send_keys(r"path of a file")
*file upload popup should be developed by "input tag and type="file" attribute"

characteristics of alert and confirmation:
-----------------------------------------
*we can't inspect the popup
*we can move/drag the popup
"""
#ws to upload resume in naukri.com
"""
driver = Chrome(options=o)
driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
driver.maximize_window()
sleep(3)
driver.find_element("xpath", "(//h2[@class='main-3'])[1]").click()
driver.find_element("id", "resumeUpload").send_keys(r"C:\\Users\\Hp\\Desktop\\manual grooming notes.pdf")
"""
#ws to upload resume in shine.com
"""
driver = Chrome(options=o)
driver.get("https://www.shine.com/registration/")
driver.maximize_window()
driver.find_element("xpath", "//input[@type='file']").send_keys("C:\\Users\\Hp\\Downloads\\pshort resume.pdf")
"""
##################################################################################################
#4.file download popup
"""
*downloading a file from a webpage is a called as file download popup.
*when ever we are downloading browser will think un-authorized person is downloading, 
it will not download, and default it will download in downloads folder, to over come 
this we use below code.

o = ChromeOptions()
o.add_experimental_option("prefs", {"safebrowsing.enabled":True,
                                    "download.default_directory":r"path of folder"})
"""
#ws to download python version from python.org(it will throw error)
"""
driver = Chrome(options=o)
driver.get("https://www.python.org/downloads/")
driver.maximize_window()
driver.find_element("xpath", "(//a[.='Download Python 3.12.5'])[2]").click()
#unverified person is downloading, ON Safe Browsing
"""
#ws to download python version from python.org
"""
o = ChromeOptions()
o.add_experimental_option("prefs", {"safebrowsing.enabled":True})
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.get("https://www.python.org/downloads/")
driver.maximize_window()
driver.find_element("xpath", "(//a[.='Download Python 3.12.5'])[2]").click()
"""
#ws to download python version from python.org in specified location
"""
o = ChromeOptions()
o.add_experimental_option("prefs", {"safebrowsing.enabled":True,
                                    "download.default_directory":r"E:\\pythonnnn"})
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.get("https://www.python.org/downloads/")
driver.maximize_window()
driver.find_element("xpath", "(//a[.='Download Python 3.12.5'])[2]").click()
"""
#ws to verify file is downloaded in the specified location or not
"""
import os

driver = Chrome(options=o)
driver.get("https://www.python.org/downloads/")
driver.maximize_window()
sleep(5)
driver.find_element("xpath", "(//a[text()='Python 3.14.2'])[4]").click()
sleep(15)
files = os.listdir("E:\\SQL 11G")
assert "python-3.14.2-amd64.exe" in files, "file not downloaded"
print("file downloaded successfully")
"""
######################################################################################################
#5.child browser popup
"""
*a browser inside another browser is called as child browser.
*by default a control will be present in parent window, we need to switch control
from parent to child window, by following method.
    syntax: driver.switch_to.window(window_address)
*to get the window address there are 2 property,
    1.driver.current_window_handle --> it will return only parent window address 
    2.driver.window_handles --> it will return list of parent followed by child window address
                            [parent, child1, child2, ... ] 
"""
#ws to click on settings in twitter page
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Facebook']").click()
driver.find_element("xpath", "//a[.='Twitter']").click()
driver.find_element("xpath", "//a[.='Google+']").click()
driver.find_element("xpath", "//span[.='Settings']").click()
#NoSuchElementException
#because by default control will be present in parent webpage, we need to switch 
control from parent to child webpage.
"""
#example on parent and all child window address
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Facebook']").click()
driver.find_element("xpath", "//a[.='Twitter']").click()
driver.find_element("xpath", "//a[.='Google+']").click()
pid = driver.current_window_handle
print(pid)              #51EA5808430D2C8BBCF32FD376D1D1C1
all_id = driver.window_handles
print(all_id)           #['51EA5808430D2C8BBCF32FD376D1D1C1', '112ADB9A56EF4AB26D37B08C74ED9E3F', 'A119BB326D867D39DA99587F74D55D48', '2B69761AF745A5CE41C37B7FA70F9D13']
"""
#ws to print all window title
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Facebook']").click()
driver.find_element("xpath", "//a[.='Twitter']").click()
driver.find_element("xpath", "//a[.='Google+']").click()
all_id = driver.window_handles  #[parent, child1, child2, child3]
for i in all_id:                #i=parent
    driver.switch_to.window(i)  #switch_to.window(parent)
    sleep(5)
    print(driver.title)
# Demo Web Shop
# Google Workspace Updates: New community features for Google Chat and an update on Currents
# NopCommerce | Facebook
# nopCommerce (@nopCommerce) / X
"""
#ws to print all child window title
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Facebook']").click()
driver.find_element("xpath", "//a[.='Twitter']").click()
driver.find_element("xpath", "//a[.='Google+']").click()
all_id = driver.window_handles      #[parent, child1, child2, child3]
for i in all_id[1:]:                #i=child1
    driver.switch_to.window(i)      #switch_to.window(child1)
    sleep(5)
    print(driver.title)
# NopCommerce | Facebook
# nopCommerce (@nopCommerce) / X
# Google Workspace Updates: New community features for Google Chat and an update on Currents
"""
#ws to close all windows one by one
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Facebook']").click()
driver.find_element("xpath", "//a[.='Twitter']").click()
driver.find_element("xpath", "//a[.='Google+']").click()
all_id = driver.window_handles      #[parent, child1, child2, child3]
for i in all_id:                #i=child1
    driver.switch_to.window(i)      #switch_to.window(child1)
    sleep(2)
    driver.close()
"""
#ws to close all child window
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Facebook']").click()
driver.find_element("xpath", "//a[.='Twitter']").click()
driver.find_element("xpath", "//a[.='Google+']").click()
all_id = driver.window_handles      #[parent, child1, child2, child3]
for i in all_id[1:]:                #i=child1
    driver.switch_to.window(i)      #switch_to.window(child1)
    sleep(2)
    driver.close()
"""
#ws to close only parent window
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Facebook']").click()
driver.find_element("xpath", "//a[.='Twitter']").click()
driver.find_element("xpath", "//a[.='Google+']").click()
driver.close()
"""
#ws to click on settings in twitter page
"""
driver = Chrome(options=o)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("xpath", "//a[.='Twitter']").click()
driver.find_element("xpath", "//a[.='Facebook']").click()
driver.find_element("xpath", "//a[.='Google+']").click()
all_ids = driver.window_handles     #allids=[parent, child1, child2, child3]
for i in all_ids:                   #i=parent
    driver.switch_to.window(i)      #switch_to.window(parent)
    sleep(4)
    if driver.title=="nopCommerce (@nopCommerce) / X":
        driver.find_element("xpath","//span[.='Settings']").click()
        break
"""
"""
assignment
----------
open https://mohfw.gov.in/?q=en > click on Organisation > click on Departments of Health and Family Welfare
> click Disaster Management Cell > click on Provider Course Manual for Doctors (5.39 MB) >  
click download icon.
"""
##########################################################################################################
#02/01/2026 ---> Day 17
#notification popup
"""
o = ChromeOptions()
o.add_argument("--disable-notifications")
o.add_experimental_option("detach", True)

driver = Chrome(options=o)
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
"""
"""
data driven testing
===================

*testing an application with different set of input, reading data from excel is as
data driven testing.
*will store multiple set of inputs inside a excel file.
*since excel is a standalone application selenium will not support, so we use xlrd
as a 3rd plugin/application.

steps to install xlrd:
----------------------
option1: click on hamburger(4lines) --> click on settings --> click on python --> click on interpreter
--> click on + --> search for xlrd and select version as 1.2.0 --> click on install package 

option2: open terminal -> type the command > pip install xlrd==1.2.0
steps to create a excel file in pycharm:
----------------------------------------
*create a directory in pycharm named as excel_file
*go to pycharm project location(right click on project-->click on open in --> click on explorer)
*click on excel_file folder
*create a new excel file(right click --> click on new --> click on microsoft excel)

steps to read data from excel file:
-----------------------------------
step1: open excel file
step2: specify the sheet name
step3: specify the row, colum number(both row and column index starts from 0)

method of extracting row and colum values
-----------------------------------------
row_values(row_num) : it will return list of the specified row all columns values
row_values(row_num, start_col): it will return list of specified row, from specified column
                            to till last column values
row_values(row_num, start_col, end_col): it will return list of specified row, from specified
start colum to specified end colum values
"""
from xlrd import *

#wp to print 4th row all columns
"""
#step1
wb = open_workbook("../excel_files/demo.xlsx")
#step2
sh = wb.sheet_by_name("Sheet1")
#step3
data = sh.row_values(3)
print(data)
#['simpledimple', 'simdim@12221']
"""
#wp to print 2nd row all columns
"""
wb = open_workbook("../excel_files/demo.xlsx")
sh = wb.sheet_by_name("Sheet1")
data = sh.row_values(2)
print(data)
#['test', 'test@12345', 'pass', 'fail']
"""
#wp to print 3rd row from 1st to last column
"""
wb = open_workbook("../excel_files/demo.xlsx")
sh = wb.sheet_by_name("Sheet1")
data = sh.row_values(2, 1)
print(data)
#['test@12345', 'pass', 'fail']
"""
#ws to print 3rd row 1st and 2nd column
"""
wb = open_workbook("../excel_files/demo.xlsx")
sh = wb.sheet_by_name("Sheet1")
data = sh.row_values(2, 0, 2)
print(data)
#['test', 'test@12345']
"""
#wp to print total number of rows and column
"""
wb = open_workbook("../excel_files/demo.xlsx")
sh = wb.sheet_by_name("Sheet1")
row_count = sh.nrows
print(row_count)            #6
col_count = sh.ncols
print(col_count)            #4
"""
#wp to print all username and password present in excel file
"""
wb = open_workbook("../excel_files/demo.xlsx")
sh = wb.sheet_by_name("Sheet1")
row_count = sh.nrows        #6
for i in range(row_count):  #[0, 1, .. 5]
    data = sh.row_values(i, 0, 2)
    print(data)
# ['username', 'password']
# ['demo', 'demo@123']
"""
#create a dictionary of username and password pair
"""
d = {}
wb = open_workbook("../excel_files/demo.xlsx")
sh = wb.sheet_by_name("Sheet1")
row_count = sh.nrows                        #6
for i in range(row_count):                  #[0, 1, .. 5]
    data = sh.row_values(i, 0, 2)           #['username', 'password']
    d[data[0]] = data[1]
print(d)        #{'username': 'password', 'demo': 'demo@123', 'test': 'test@12345', 'simpledimple': 'simdim@12221', 'admin': 'manager', 'a1b2': '1a2b'}
"""
###############################################################################################
#ws to test facebook login page by entering 5 set of inputs
"""
wb = open_workbook("E:\\github_topic\\test1\\E20_SeleniumBatch\\excel_files\\data.xlsx")
sh = wb.sheet_by_name("Sheet1")
row_count = sh.nrows        #6
for i in range(1, row_count):           #i=1                        i=2
    data = sh.row_values(i, 0, 2)       #(1, 0, 2)                  (2, 0, 2)
    print(data) 
"""                        #['amith', 'amith@1234']    ['praveen@gmail.com', 'praveen112233']
"""
d = {}   #{'amith': 'amith@1234', 'praveen@gmail.com': 'praveen112233', 'hemanth123': 'hemanth123', 'akash': '', '': 'akash@123'}
wb = open_workbook("E:\\github_topic\\test1\\E20_SeleniumBatch\\excel_files\\data.xlsx")
sh = wb.sheet_by_name("Sheet1")
row_count = sh.nrows        #6
for i in range(1, row_count):           #i=1                        i=2
    data = sh.row_values(i, 0, 2)       #data = ['amith', 'amith@1234']
    d[data[0]] = data[1]

for un, pwd in d.items():
    driver = Chrome(options=o)
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    driver.find_element("id", "email").send_keys(un)
    driver.find_element("id", "pass").send_keys(pwd)
    driver.find_element("name", "login").click()
    sleep(3)
    driver.close()
"""



























































