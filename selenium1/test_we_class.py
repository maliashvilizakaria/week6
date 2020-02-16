# search_box = browser.find_element_by_xpath('search')
# search_box.send_keys(Keys.ENTER)
# search_box.submit()
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


def test_forms_textboxes(browser):
    """working with forms, textboxes, checkboxes, and radio buttons."""
    url = "http://the-internet.herokuapp.com/login"

    browser.get(url)
    sleep(5)
    # element locators
    username = browser.find_element_by_xpath("//input[@id='username']")
    passwrod = browser.find_element_by_xpath("//input[@id='password']")
    login = browser.find_element_by_xpath("//i[@class='fa fa-2x fa-sign-in']")

    username.send_keys("tomsmith")
    passwrod.send_keys("SuperSecretPassword!")
    login.click()
    sleep(10)

    # testing the message text area
    expected_message = "Welcome to the Secure Area. When you are done click logout below."
    message = browser.find_element_by_xpath("//h4[@class='subheader']").text
    assert expected_message == message.strip(), "Assert failed!!!"

    # verify logout button displayed, if displayed click logout
    logout = browser.find_element_by_xpath(
        "//i[@class='icon-2x icon-signout']")
    if logout.is_displayed():
        logout.click()
    else:
        print("logout is not displayed")

    # check the login page is opened
    assert url in browser.current_url, "This is the message if url assert fails"


def test_checkbox(browser):
    url = "http://the-internet.herokuapp.com/checkboxes"

    browser.get(url)
    sleep(5)
    element1 = browser.find_element_by_xpath("//body//input[1]")
    element2 = browser.find_element_by_xpath("//body//input[2]")

    # logic for element1
    if element1.is_selected():
        element1.click()
        print("unselecting the element1")
    else:
        element1.click()
        print("selecting the element1")

    # logic for element2
    if element2.is_selected():
        element2.click()
        print("unselecting the element2")
    else:
        element2.click()
        print("selecting the element2")

    sleep(15)
