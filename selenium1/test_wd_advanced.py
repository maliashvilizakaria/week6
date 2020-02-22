from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import selenium1.utilities as utils


# methods for performing keyboard and mouse actions using Actions class
# simulating mouse operations such as draand driop and double click
# Running JacaScript code
# capturing screenshots and movies of test runs
# Handling browser navigation and cookies

# print(utilities.get_timestamp())


def test_take_screenshots(browser):
    """takes screenshots if no element found"""
    
    url = "http://the-internet.herokuapp.com/login"
    try:
        browser.get(url)
        # element locators
        username = browser.find_element_by_xpath("//input[@id='username']")
        passwrod = browser.find_element_by_xpath("//input[@id='password']")
        login = browser.find_element_by_xpath("//i[@class='fa fa-2x fa-sign-in']")

        username.send_keys("tomsmith")
        passwrod.send_keys("SuperSecretPassword!")
        login.click()
        sleep(10)
    except NoSuchElementException:
        filepath = "./screenshots/"+utils.get_timestamp()+".png"
        browser.save_screenshot(filepath)
        sleep(5)
        
