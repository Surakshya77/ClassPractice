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

def test_login(driver):
    login_page=LoginPage(driver)
    login_page.open_page("https://tax.digitalpalika.org/login")
    driver.maximize_window()
    time.sleep(2)
    login_page.enter_username("malikacounter5")
    time.sleep(1)
    login_page.enter_password("password")
    time.sleep(1)
    login_page.click_login()
    time.sleep(1)

