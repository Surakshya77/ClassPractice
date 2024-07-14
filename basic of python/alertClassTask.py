#alert message capture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


#set the chromedriver manager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


#get the website url;
website_url="https://sagar-test-qa.vercel.app/"

#open the website url
driver.get(website_url)

#maximize the window
driver.maximize_window()

#locate the element as
username=driver.find_element(*(By.XPATH,"//input[@id='username']"))
password=driver.find_element(By.XPATH,"//input[@id='password']")
login=driver.find_element(By.XPATH,"//button[normalize-space()='Login']")

#fill the web element as:
username.send_keys("Hari")
password.send_keys("12345")
login.click()

#switch to alert
alert=driver.switch_to.alert
time.sleep(2)

#close the alert
alert.accept()
time.sleep(2)

#close the instance
driver.quit()
print("congrats alert message is capture and close successfully!!!")