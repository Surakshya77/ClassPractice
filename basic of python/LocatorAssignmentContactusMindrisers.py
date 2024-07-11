#path locator create and post method
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

#set the chromedriver manager
driver=webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

#set the website
website_url='https://www.mindrisers.com.np/contact-us'

#get the website
driver.get(website_url)

#maximize the window size
driver.maximize_window()
time.sleep(2)

#find the form webelement by their xPath
full_name=driver.find_element(By.XPATH,"//input[@name='name']")
email_field=driver.find_element(By.XPATH,"//input[@name='email']")
phone_number=driver.find_element(By.XPATH,"//input[@name='mobile_no']")
subject=driver.find_element(By.XPATH,"//input[@name='subject']")
query=driver.find_element(By.XPATH,"//textarea[@name='message']")

#fill the form
full_name.send_keys('Ram')
email_field.send_keys('ram@gmail.com')
phone_number.send_keys('987654321')
subject.send_keys('Regarding contact details')
query.send_keys('Please prove me the Fee Details of QA class')
time.sleep(4)

#finally quit the driver instance
driver.quit()