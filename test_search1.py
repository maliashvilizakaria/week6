# Test Case
# Candidate needs to use: Chrome, selenium, python on ubuntu linux instance on EC2(Free instance). 
# Login to FB and go to marketplace and create a listing (it can be for anything you like)
# Then delete the listing

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Open browser and navigate to Facebook marketplace
chrome_url = "C:\dev\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_url)
home_url = "https://www.facebook.com/marketplace?ref=bookmark"
email = 'zmaliashvili@yahoo.com'
pasword = 'leninzakro1'
driver.get(home_url)
driver.maximize_window()

# Click on + Create New List 
driver.find_element_by_link_text("Create New Listing").click()
time.sleep(1)

#login
email = driver.find_element_by_xpath("//div[@class='_7mqs']//input[@id='email']")
email.send_keys('zmaliashvili@yahoo.com')
pasword = driver.find_element_by_xpath("//div[@class='_7mqs']//input[@id='pass']")
pasword.send_keys('leninzakro1\n')

# click item for sale
time.sleep(5)
item_forsale = driver.find_element_by_xpath("//div[contains(text(),'Sell one item in a single category.')]")
item_forsale.click()

# click upload photo
time.sleep(2)
photo = driver.find_element_by_xpath("//span[contains(text(),'Add Photos')]").click()
# driver.find_element_by_id("Id of the element").send_keys(Imagepath)

# type title
time.sleep(2)
title = driver.find_element_by_xpath('//div//div//div//div//div//div//div//div//div//div//div//div//div//div[3]//div[1]//div[1]//label[1]//div[1]//div[1]//input[1]')
title.send_keys('Iphone X')

#type price
time.sleep(2)
price = driver.find_element_by_xpath('//div//div//div//div//div[4]//div[1]//div[1]//label[1]//div[1]//div[1]//input[1]')
price.send_keys('1000')

# dropdown chose mobile phone
time.sleep(2)
driver.find_element_by_xpath('//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/label/div/div/div/div[1]').click()
time.sleep(2)
mobile_phone = driver.find_element_by_xpath('//div[22]//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]//span[1]//div[1]').click()

# drop down conditions chose New
time.sleep(2)
driver.find_element_by_xpath('//div[6]//div[1]//div[1]//label[1]//div[1]//div[1]//div[1]//div[1]').click()
time.sleep(2)
driver.find_element_by_xpath('//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div[1]/div[1]/span[1]').click()
time.sleep(5)

# # click Next 
# time.sleep(2)
# driver.find_element_by_xpath('//span[contains(text(),"Next")]').click()

# # click publish 
# time.sleep(2)
# driver.find_element_by_xpath('//body/div/div/div/div/div/div/div/div/div/div/div/div/div[5]/div[1]/div[1]').click()

# # Delate listing 
# time.sleep(2)
# driver.find_element_by_xpath('//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div[3]/div[1]/div[1]').click()
# driver.find_element_by_xpath('//span[contains(text(),"Delete")]')
# # confirming delete 
# time.sleep(2)
# driver.find_element_by_xpath('//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div[1]/span[1]')

driver.quit()

# Webdriverwait(driver,20).until(expected_conditions.presence_of_element_located(locator))
