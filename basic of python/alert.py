#alert message capture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

#set the chromedriver manager
driver=webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

#set the website
website_url='https://demoqa.com/alerts'

#get the website
driver.get(website_url)

#maximize the window size
driver.maximize_window()
time.sleep(2)

#locate
click_me=driver.find_element(*(By.XPATH,"//button[@id='alertButton']"))
click_me.click()

#switch to alert
alert=driver.switch_to.alert
time.sleep(3)

#close the alert
alert.accept()
time.sleep(2)

#finally quit the driver instance
driver.quit()
driver.close()
print("Congratulations!!! alert message is captured and closed successfully")