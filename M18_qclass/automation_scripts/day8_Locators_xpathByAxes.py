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
#19/12/2025 ---Day8
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
































