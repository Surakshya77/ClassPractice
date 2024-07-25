#import the necessary module
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from pom.page.login_page import LoginPage


@pytest.fixture()
def driver():
    # set the chromedriver manager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(1)
    # yield the driver
    yield driver
    # close the driver
    driver.quit()

# def test_login(driver):
#     login_page=LoginPage(driver)
#     login_page.open_page("https://tax.digitalpalika.org/login")
#     driver.maximize_window()
#     time.sleep(2)
#     login_page.enter_username("malikacounter5")
#     time.sleep(1)
#     login_page.enter_password("password")
#     time.sleep(1)
#     login_page.click_login()
#     time.sleep(1)


@pytest.mark.parametrize("username,password",[
    ("TestQA","password"),
    ("A","password"),
    ("1",""),
])

def test_login(driver, username, password):
    login_page=LoginPage(driver)
    login_page.open_page("https://sagar-test-qa.vercel.app/")
    driver.maximize_window()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    alert_text=login_page.get_alert_text_and_accept()
    if alert_text and "Invalid username or password" in alert_text:
        print(f"Invalid username or password for {username}")
    else:
        if login_page.is_dashboard_present():
            print(f"Login successful for {username}")
        else:
            print(f"Unexpected error or login failed for {username}")