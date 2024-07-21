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
website_url="https://meroshare.cdsc.com.np/#/login"

#open the website url
driver.get(website_url)

#maximize the window
driver.maximize_window()
print("Successfully locateded the dropdown menu")
time.sleep(5)

drop_down=driver.find_element(*(By.XPATH,"/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[1]/div/div/select2/span/span[1]/span/span[1]"))
drop_down.click()
time.sleep(2)
option_xpath="//li[contains(text(),'AAKASH CAPITAL LIMITED (19000)')]"
option=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,option_xpath)))
option.click()
time.sleep(5)


#close the webdriver instance
driver.close()