from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from webdriver_manager.core import driver


class CoursesPage:
    def __init__(self, driver):
        self.driver = driver

    dropdown = (By.XPATH, "//body/div/div/div/main/section/div/div/section/ul/li[1]/div[1]")

    def open_page(self, url):
        self.driver.get(url)
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    def enter_search_query(self, query):
        search_box = self.driver.find_element(By.NAME, 'searchTerm')  # Adjust the selector as needed
        search_box.clear()  # Clear any existing text
        search_box.send_keys(query)  # Enter the search query
        search_box.send_keys(Keys.RETURN)

    @property
    def get_search_results(self):
        # Wait for search results to appear and get them
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(
            (By.XPATH, "//input[@name='searchTerm']")))  # Update selector based on actual results
        results = self.driver.find_elements(By.XPATH, "//input[@name='searchTerm']")  # Adjust the selector as needed
        return results

