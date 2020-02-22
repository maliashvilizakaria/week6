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
# url = "https://learn.letskodeit.com/p/practice"

def test_take_screenshots(browser):
    """takes screenshots if no element found"""

    url = "http://the-internet.herokuapp.com/login"
    try:
        browser.get(url)
        # element locators
        username = browser.find_element_by_xpath("//input[@id='username']")
        passwrod = browser.find_element_by_xpath("//input[@id='password']")
        login = browser.find_element_by_xpath(
            "//i[@class='fa fa-2x fa-sign-in']")

        username.send_keys("tomsmith")
        passwrod.send_keys("SuperSecretPassword!")
        login.click()
        sleep(10)
    except NoSuchElementException:
        filepath = "./screenshots/"+utils.get_timestamp()+".png"
        browser.save_screenshot(filepath)
        sleep(5)


def test_popup_window(browser):
    """ Switching to new window and switch back."""

    url = "https://learn.letskodeit.com/p/practice"
    browser.get(url)
    # get handle
    parent_window_id = browser.current_window_handle
    sleep(10)
    openwindow_button = browser.find_element_by_xpath(
        "//button[@id='openwindow']")
    openwindow_button.click()
    handles = browser.window_handles
    for handle in handles:
        if handle not in parent_window_id:
            browser.switch_to.window(handle)
            sleep(10)
            search = browser.find_element_by_xpath(
                "//input[@id='search-courses']")
            search.send_keys("python")
            search.submit()
            sleep(10)
            browser.close()
            break

    browser.switch_to.window(parent_window_id)
    sleep(5)


def test_execute_js(browser):
    """ Demonstates executing some javaScript code with selenium."""

    url = "https://learn.letskodeit.com/p/practice"
    browser.get(url)
    browser.execute_script(
        "window.location = 'https://learn.letskodeit.com/p/practice';")

    # element = browser.find_element_by_id('name')
    element = browser.execute_script("return document.getElementById('name');")
    element.send_keys('Hello')

    # Scroll down
    browser.execute_script("window.scrollBy(0, 1300);")
    sleep(5)

    # Scroll up
    browser.execute_script("window.scrollBy(0, -1300);")
    sleep(5)


def test_hover_action(browser):
    """ Demonstates Mouse over action using ActionChains class."""

    url = "https://learn.letskodeit.com/p/practice"
    browser.get(url)

    element = browser.find_element_by_xpath("//button[@id='mousehover']")
    actions = ActionChains(browser)
    actions.move_to_element(element).perform()
    print("Mouse hovered on the element")
    sleep(5)
    topLink = browser.find_element_by_xpath("//a[contains(text(),'Top')]")
    topLink.click()
    sleep(3)
    print("top link clicked")


def test_drag_and_drop(browser):
    """ Demonstrates Drag and Drop mouse action using ActionChains class."""

    url = "http://the-internet.herokuapp.com/drag_and_drop"
    url = "https://jqueryui.com/droppable/"
    browser.get(url)

    # elementA = browser.find_element_by_xpath("//div[@id='column-a']")
    # elementB = browser.find_element_by_xpath("//div[@id='column-b']")
    elementA = browser.find_element_by_xpath("//div[@id='draggable']")
    elementB = browser.find_element_by_xpath("//div[@id='droppable']")

    actions = ActionChains(browser)
    actions.drag_and_drop(elementA, elementB).perform()
    print('dragged element A to B')
    sleep(5)

    # actions.click_and_hold(elementB).move_to_element(elementA).release().perform()
    # print("dragged element B to A .")
    # sleep(5)
