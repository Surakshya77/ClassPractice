from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Blogs:
    def __init__(self,driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def process_page(self):
        # Example function to process the current page
        print("Processing current blog page...")
        # Add code to extract blog post data or perform actions on the current page
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

    def go_to_next_page(self):
        try:
            # Adjust the XPath to match your pagination "Next" button
            next_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH,"//li[contains(@title,'下一页')]"))
            )
            next_button.click()
            WebDriverWait(self.driver, 5).until(
                EC.staleness_of(next_button)  # Wait until the button is no longer stale
            )
        except Exception as e:
            print(f"Error navigating to next page: {e}")
            return False
        return True
    def paginate_through_pages(self, max_pages=3):
        page_number = 1
        while page_number <= max_pages:
            self.process_page()
            if not self.go_to_next_page():
                break
            page_number += 1