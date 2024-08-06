#  import the necessary module
import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC

from MindrisersAutomation.Pages.Courses_page import CoursesPage
from MindrisersAutomation.Pages.admission_page import AdmissionPage
from MindrisersAutomation.Pages.blogs_page import Blogs
from MindrisersAutomation.Pages.contactus_page import ContactPage
from MindrisersAutomation.Pages.placementPartner_page import PlacementPartner
from MindrisersAutomation.Pages.postCourses_page import PostCourses
from MindrisersAutomation.Pages.successGallery_page import SuccessGallery


def scroll_page(driver):
    page_height = driver.execute_script("return document.body.scrollHeight")
    scroll_speed = 500
    scroll_iterations = int(page_height / scroll_speed)
    for _ in range(scroll_iterations):
        driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
        time.sleep(1)


@pytest.fixture()
def driver():
    # set the chromedriver manager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    # yield the driver
    yield driver
    # close the driver
    driver.quit()


def test_courses_page(driver):
    courses_page = CoursesPage(driver)
    courses_page.open_page("https://www.mindrisers.com.np/courses")
    driver.maximize_window()
    scroll_page(driver)
    time.sleep(2)
    # Perform a search
    search_query = "Quality Assurance"
    time.sleep(2)
    courses_page.enter_search_query(search_query)
    time.sleep(2)
    courses_page.open_page("https://www.mindrisers.com.np/courses/quality-assurance-training-in-nepal")
    time.sleep(2)
    scroll_page(driver)


def test_postCourses_page(driver):
    post_courses = PostCourses(driver)
    post_courses.open_page("https://www.mindrisers.com.np/after+2-courses")
    time.sleep(1)
    driver.maximize_window()
    scroll_page(driver)
    time.sleep(2)


def test_placementPartner_page(driver):
    placepartner = PlacementPartner(driver)
    placepartner.open_page("https://www.mindrisers.com.np/placement-partner")
    driver.maximize_window()
    time.sleep(2)
    scroll_page(driver)
    time.sleep(2)


def test_success_gallery_page(driver):
    success = SuccessGallery(driver)
    success.open_page("https://www.mindrisers.com.np/success-gallery")
    driver.maximize_window()

    scroll_page(driver)
    time.sleep(2)


def test_contactus_page(driver):
    contactus_page = ContactPage(driver)
    contactus_page.open_Page("https://www.mindrisers.com.np/contact-us")
    time.sleep(1)
    driver.maximize_window()
    time.sleep(5)
    contactus_page.enter_FullName("Surakshya")
    time.sleep(2)
    contactus_page.enter_Email("surakshya@gmail.com")
    time.sleep(2)
    contactus_page.enter_Phone("987654321")
    time.sleep(2)
    contactus_page.enter_Subject("Regarding Details")
    time.sleep(2)
    contactus_page.enter_Query("Fee details of QA classes")
    time.sleep(2)
    print(f"Congratulations!!! Contact page open successfully")


def test_admission_page(driver):
    admission_page = AdmissionPage(driver)
    admission_page.open_page("https://www.mindrisers.com.np/online-admission")
    time.sleep(1)
    driver.maximize_window()
    time.sleep(2)
    admission_page.enter_fullname("Surakshya")
    time.sleep(1)
    admission_page.enter_email("surakshya@gmail.com")
    time.sleep(2)
    admission_page.enter_phone("987654321")
    time.sleep(1)
    admission_page.enter_college("ACHS")
    time.sleep(1)
    admission_page.select_academicStatus("Bachelor Completed/Running")
    time.sleep(1)
    admission_page.interested_course("Quality Assurance Training in Nepal")
    time.sleep(1)
    admission_page.preferred_schedule("Evening")
    time.sleep(1)
    # admission_page.select_internshipProgram("No")
    # time.sleep(1)
    admission_page.enter_query("Details regarding Fee structure of QA Training ......")
    time.sleep(2)


def test_blogs_page(driver):
    blogs_page = Blogs(driver)
    blogs_page.open_page("https://www.mindrisers.com.np/blogs")
    driver.maximize_window()

    # Initial scroll to load content
    scroll_page(driver)

    # Paginate through pages
    blogs_page.paginate_through_pages(max_pages=3)

    # Scroll after pagination to load more content
    scroll_page(driver)

    # Paginate again if necessary
    blogs_page.paginate_through_pages(max_pages=3)

    # Scroll after second pagination to ensure all content is loaded
    scroll_page(driver)
    time.sleep(2)

    # Perform a search
    search_query = "Quality Assurance"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'searchTerm'))
    ).send_keys(search_query + Keys.RETURN)
    time.sleep(2)

    # Wait for search results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//input[@name='searchTerm']"))  # Adjust selector if needed
    )
    time.sleep(2)

    # Open a specific blog page
    blogs_page.open_page(
        "https://www.mindrisers.com.np/blogs/career-in-quality-assurance-qa-in-nepal"
        "-mindrisers-exploring-opportunities-in-kathmandu-lalitpur-and-bhaktapur")

    # Scroll the specific blog page
    scroll_page(driver)
