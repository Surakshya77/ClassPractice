#import the necessary module
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time
@pytest.fixture()
def driver():
    # set the chromedriver manager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    #yield the driver
    yield driver
    #close the driver
    driver.close()
    
@pytest.mark.parametrize("username, password",[
    ("TestQA", "password"),  #valid username and password
    ("invalid", "password"),  #invalid username and password
    ("1", "1"),  #invalid username and password
    ("a", "pass"),  #invalid username and password
])
def test_login(driver, username, password):
    driver.get("https://sagar-test-qa.vercel.app/")
    username_field = driver.find_element(By.XPATH, "//input[@id='username']")
    password_field = driver.find_element(By.XPATH, "//input[@id='password']")
    login_button = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

    try:
        #check if an alert message is present
        alert = driver.switch_to.alert
        #alert_text = alert.text
        alert.accept()
        #assert "Invalid username or password" in alert_text
        print(f"Invalid username or password for {username}")

    except:
        #if there is no alert then login is successful:
        time.sleep(2)
        page_source = driver.page_source
        if "Welcome to the Dashboard" in page_source:
            print(f"Login was successful for {username}")
        else:
            print(f"Unexpected error or login failed for for {username}")
