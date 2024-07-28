#import the necessary module
import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from pom.page.company_page import CompanyPage
from pom.page.dashboard_page import DashboardPage
from pom.page.aboutyourself_page import AboutYourselfPage
from pom.page.article_page import ArticlePage
from pom.page.contact_page import ContactPage
from pom.page.qa_testing_page import QaTestingPage


# from pom.page.login_page import LoginPage
# from selenium.webdriver.common.by import By



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

#
# @pytest.mark.parametrize("username,password",[
#     ("TestQA","password"),
#     ("A","password"),
#     ("1",""),
# ])
#
# def test_login(driver, username, password):
#     login_page=LoginPage(driver)
#     login_page.open_page("https://sagar-test-qa.vercel.app/")
#     driver.maximize_window()
#     login_page.enter_username(username)
#     login_page.enter_password(password)
#     login_page.click_login()
#
#     alert_text=login_page.get_alert_text_and_accept()
#     if alert_text and "Invalid username or password" in alert_text:
#         print(f"Invalid username or password for {username}")
#     else:
#         if login_page.is_dashboard_present():
#             print(f"Login successful for {username}")
#         else:
#             print(f"Unexpected error or login failed for {username}")

def test_dashboard_page(driver):
    dashboard_page = DashboardPage(driver)
    dashboard_page.open_dashboard_page("https://sagar-test-qa.vercel.app/dashboard.html")
    driver.maximize_window()
    time.sleep(2)
    print(f"Congratulations!!!! Dashboard page is open successfully")


def test_about_yourself_page(driver):
    about_page = AboutYourselfPage(driver)
    about_page.open_page("https://sagar-test-qa.vercel.app/about.html")
    time.sleep(1)
    driver.maximize_window()
    about_page.enter_fullname("Ram")
    time.sleep(1)
    about_page.enter_phone("987654321")
    time.sleep(1)
    about_page.enter_email("ram@gmail.com")
    time.sleep(1)
    about_page.enter_hobby("Football")
    time.sleep(2)
    about_page.click_submit_button()
    time.sleep(2)
    print(f"Congratulations!!! About us page open successfully")

def test_article_page(driver):
    article_page=ArticlePage(driver)
    article_page.open_page("https://sagar-test-qa.vercel.app/articles.html")
    time.sleep(2)
    driver.maximize_window()

    # calculate the height of the web page
    page_height = driver.execute_script("return document.body.scrollHeight")

    # scroll down the content
    scroll_speed = 100
    scroll_iterations = int(page_height / scroll_speed)
    # loop the iteration performance
    for _ in range(scroll_iterations):
        driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
        time.sleep(1)

def test_contact_page(driver):
    contact_page=ContactPage(driver)
    contact_page.open_page("https://sagar-test-qa.vercel.app/contact.html")
    time.sleep(1)
    driver.maximize_window()
    contact_page.enter_fullname("Surakshya")
    time.sleep(1)
    contact_page.enter_email("surakshya@gmail.com")
    time.sleep(1)
    contact_page.enter_message("Hello there !!!")
    time.sleep(1)
    contact_page.click_send_message_button()
    print(f"Cpngratulations!!! Contact page open successfully")

def test_qa_testing_page(driver):
    qaTesting_page=QaTestingPage(driver)
    qaTesting_page.open_page("https://sagar-test-qa.vercel.app/qa.html")
    time.sleep(2)
    driver.maximize_window()

    # calculate the height of the web page
    page_height = driver.execute_script("return document.body.scrollHeight")

    # scroll down the content
    scroll_speed = 100
    scroll_iterations = int(page_height / scroll_speed)
    # loop the iteration performance
    for _ in range(scroll_iterations):
        driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
        time.sleep(1)

def test_company_page(driver):
    company_page=CompanyPage(driver)
    company_page.open_page("https://sagar-test-qa.vercel.app/company.html")
    time.sleep(2)
    driver.maximize_window()

    # calculate the height of the web page
    page_height = driver.execute_script("return document.body.scrollHeight")

    # scroll down the content
    scroll_speed = 100
    scroll_iterations = int(page_height / scroll_speed)
    # loop the iteration performance
    for _ in range(scroll_iterations):
        driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
        time.sleep(1)