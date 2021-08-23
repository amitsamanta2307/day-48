from selenium import webdriver

chrome_driver_path = "../../Development/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))
#
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)
#
# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_times = driver.find_elements_by_css_selector('.event-widget time')
event_names = driver.find_elements_by_css_selector('.event-widget li a')

events = {}

for i in range(len(event_times)):
    events[i] = {
        'times': event_times[i].text,
        'names': event_names[i].text
    }

print(events)

driver.close()  # closes the active tab
driver.quit()   # shut down the entire browser
