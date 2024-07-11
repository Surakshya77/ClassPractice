#path locator create and post method
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

#set the chromedriver manager
driver=webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

#set the website
website_url='https://demoqa.com/text-box'

#get the website
driver.get(website_url)

#maximize the window size
driver.maximize_window()
time.sleep(2)

#find the form webelement by their xPath
full_name=driver.find_element(By.XPATH,"//input[@id='userName']")
email_field=driver.find_element(By.XPATH,"//input[@id='userEmail']")
current_address=driver.find_element(By.XPATH,"//textarea[@id='currentAddress']")
permanent_address=driver.find_element(By.XPATH,"//textarea[@id='permanentAddress']")
submit_button=driver.find_element(By.ID,"submit")

#fill the form
full_name.send_keys('Ram')
email_field.send_keys('ram@gmail.com')
current_address.send_keys('Putalisadak')
permanent_address.send_keys('Kathmandu')
submit_button.click()

time.sleep(4)
#finally quit the driver instance
driver.quit()