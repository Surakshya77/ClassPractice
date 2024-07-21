#email validation
#import the necessary modules :
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#set the chromedriver manager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#define the as email validation
def is_valid_email(email):
    try:
        #check the format using RE
         email_pattern= r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

         if re.search(email_pattern,email):
             return True

         else:
             return False

    except Exception as e:
        print(e)
        return False

#def the phone number field
def is_valid_phone(phone):
     return bool(re.match(r'^\d{10}$', phone))

#open the website as
driver.get("https://www.mindrisers.com.np/contact-us")

driver.maximize_window()

#set the scroll parameter:

target_y=6000
scroll_distance =1000
current_y=0

#loop the scrolling
while current_y< target_y:
    driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
    current_y += scroll_distance
    time.sleep(0.25)

#interact with the path locator
first_name_field=driver.find_element(*(By.XPATH,"//input[@placeholder='Name']"))
email_field=driver.find_element(*(By.XPATH,"//input[@placeholder='Email']"))
phone_field=driver.find_element(*(By.XPATH,"//input[@placeholder='Phone']"))

first_name="ram"

#invalid email params are:
#email=john123
#email=ram@@123gmail.com
#email=ram@gmail..com

#valid email :
email="ram@gmail.com"
phone="09876543345678"
time.sleep(2)
#clear the field and pass the value
first_name_field.clear()
first_name_field.send_keys(first_name)
time.sleep(0.75)

#check the validity of email:
if is_valid_email(email):

    print("valid email address")
else:
    print("invalid email address")

#clear the email field and pass the value:
email_field.clear()
email_field.send_keys(email)
time.sleep(0.75)
#check phone is empty or not
if not phone:
    print("Phone cannot be empty")

#clear the phone field
phone_field.clear()
phone_field.send_keys(phone)
time.sleep(0.75)

#close the driver instance:
driver.quit()
print("email validation is checked successfully!!!")



