
import requests
from selenium import webdriver
# used for inputting keys
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

'''wiki article count'''
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
''' id use '#' and classes use '.' '''
# article_count = driver.find_element_by_css_selector("#articlecount a")
# print(article_count.text)

'''automate click item on webpage'''
# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

'''Type and search something on webpage'''
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

'''Inputting info to sign up using test website http://secure-retreat-92358.herokuapp.com/'''
driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element_by_name("fName")
first_name.send_keys("firstname")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("lastname")
email = driver.find_element_by_name("email")
email.send_keys("test@gmail.com")
signup = driver.find_element_by_css_selector("form button")
signup.click()

# driver.quit()
