# Automating Codechef Submissions using Selenium

#Install Selenium - pip install selenium

#Chrome Webdriver - https://sites.google.com/a/chromium.org/chromedriver/downloads

#Importing Selenium & Webdriver
from selenium import webdriver

#Path to the Chrome Driver
path = "C:\Program Files (x86)\chromedriver.exe"

#Start Webdriver Session (Choose any Web browser)
browser = webdriver.Chrome(path)

#Starting session (Open link in Web browser)
browser.get("https://codechef.com")

#Login to codechef account

#Username
usernameE = browser.find_element_by_id("edit-name")

usernameE.send_keys("your_username")

#Password
password = browser.find_element_by_id("edit-pass")

#To hide password while entering in Input
from getpass import getpass

password.send_keys(getpass("Your Password: "))

#Submit/Login
browser.find_element_by_id("edit-submit").click()

#Enter URL of Problem
test = browser.get("https://www.codechef.com/submit/TEST")

#Switch to non-ide mode
browser.find_element_by_class_name("form-submit").click()

#Uncheck Toggle editor box
browser.find_element_by_id("edit_area_toggle_checkbox_edit-program").click()

#Reading input file
with open("solution.cpp",'r') as f:
    code = f.read()

codeElement = browser.find_element_by_id("edit-program")

#Passing input file/code to body of code tab
codeElement.send_keys(code)

#Choosing preferred language (C++ chosen here)
codeLanguage = browser.find_element_by_xpath('//*[@id="edit-language"]/option[1]').click()

# Submit Solution
browser.find_element_by_id("edit-submit-1").click()
