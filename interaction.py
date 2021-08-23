import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "../../Development/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# article_count = driver.find_element_by_css_selector('#articlecount a')
# article_count.click()

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# search = driver.find_element_by_name('search')
# search.send_keys('Python')
# search.send_keys(Keys.ENTER)
#
# first_name = driver.find_element_by_name('fName')
# first_name.send_keys('')
# last_name = driver.find_element_by_name('lName')
# last_name.send_keys('')
# email = driver.find_element_by_name('email')
# email.send_keys('')
#
# submit_button = driver.find_element_by_css_selector('.form-signin button')
# submit_button.send_keys(Keys.ENTER)

timeout = time.time() + 60   # 5 minutes from now

cookie = driver.find_element_by_id('bigCookie')
while True:
    test = 0
    if test == 1 or time.time() > timeout:
        break

    cookie.click()
    test = test - 1

driver.close()  # closes the active tab
driver.quit()   # shut down the entire browser
