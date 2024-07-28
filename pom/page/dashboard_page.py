#dashboard_page

from selenium.webdriver.common.by import By
import time



class DashboardPage:
    def __init__(self,driver):
        self.driver = driver

    def open_dashboard_page(self, url):
        self.driver.get(url)
