#import the necessary modules :
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#set the chromedriver manager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


#get the website url;
website_url="https://merolagani.com/"

#open the website url
driver.get(website_url)

#maximize the window
driver.maximize_window()
print("Successfully locateded the dropdown menu")
time.sleep(5)

market_menu=driver.find_element(*(By.XPATH,"//a[normalize-space()='Market']"))
market_menu.click()
time.sleep(2)
indices=driver.find_element(By.LINK_TEXT,"Indices")
indices.click()

liveTrading=driver.find_element(By.LINK_TEXT,"Live Trading")
liveTrading.click()



#close the webdriver instance
driver.close()