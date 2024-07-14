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
website_url="https://demoqa.com/automation-practice-form"

#open the website url
driver.get(website_url)

#maximize the window
driver.maximize_window()

#calculate the height of page
page_height=driver.execute_script("return document.body.scrollHeight")

#scroll the page
scroll_speed=200
scroll_iteration=int(page_height/scroll_speed)

for _ in range(scroll_iteration):
    driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
time.sleep(0.5)

#wait for page load
driver.implicitly_wait(10)

#find the fields locator xpath as:
first_name=driver.find_element(By.XPATH, "//input[@id='firstName']")
last_name=driver.find_element(By.XPATH, "//input[@id='lastName']")
email_field=driver.find_element(By.XPATH, "//input[@id='userEmail']")
gender_button_male=driver.find_element(By.XPATH, "//label[normalize-space()='Male']")
mobile_number=driver.find_element(By.XPATH, "//input[@id='userNumber']")
date_of_birth=driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']")
#select hobbies
hobby_sport_checkbox=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Sports']")))
current_address=driver.find_element(By.XPATH,"//textarea[@id='currentAddress']")

#pass the value
first_name.send_keys("ram")
last_name.send_keys("thapa")
email_field.send_keys("test@gmail.com")
gender_button_male.click()
mobile_number.send_keys("987654")
date_of_birth.send_keys("07/14/2024")

#interact with the sports checkbox
driver.execute_script("arguments[0].click();", hobby_sport_checkbox)
time.sleep(5)

current_address.send_keys("kathmandu")
print("successfully run date and checkbox module:")

#close the webdriver instance
driver.close()