
from selenium import webdriver

'''
https://selenium-python.readthedocs.io/
https://www.w3schools.com/xml/xpath_intro.asp
'''

CHROME_DRIVER_PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

'''Amazon price on Volleyball shoes'''
# URL = "https://www.amazon.com/ASICS-Gel-Rocket-Volleyball-Shoes-Black/dp/B07KDLS56Z/ref=sr_1_2?dchild=1&keywords=volleyball+shoes+men&qid=1625779984&sr=8-2"
# driver.get(URL)
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

'''---Python.org---'''
# URL = "https://www.python.org/"
# driver.get(URL)

# search_bar = driver.find_element_by_name("q")

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

'''Dictionary of Upcoming python.org Events'''
# event_times = driver.find_elements_by_css_selector(".event-widget time")
# event_names = driver.find_elements_by_css_selector(".event-widget li a")
# events = {}
# for n in range(len(event_times)):
#     events[n] = {
#         "time":event_times[n].text,
#         "event":event_names[n].text,
#     }
# print(events)


# driver.close()
driver.quit()
