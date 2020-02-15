# Test Case
# 1. Open browser chrome browser
# 2. Launch the 'automationpractice.com'
# 3. Enter 't-shirt' in search box
# 4. Click search button (option2: hit ENTER key on keyboard)
# 5. Verify at least one product displayed/appeared

from selenium import webdriver
import time

# CONSTANTS
# chrome_url = "C:\\dev\\chromedriver_win32\\chromedriver.exe"
home_url = "http://automationpractice.com"
keyword = 't-shirt'


def test_launching_site(browser):
    browser.get(home_url)


def test_entering_the_keyword(browser):
    browser.find_element_by_name("search_query").send_keys(keyword)
    time.sleep(5)
    browser.find_element_by_name("submit_search").click()


def test_verify_result(browser):
    products_list = browser.find_elements_by_xpath(
        "//*[@id='center_column']/ul/li")
    assert len(products_list) >= 1
    time.sleep(5)
