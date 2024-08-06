from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AdmissionPage:
    def __init__(self, driver):
        self.driver = driver
        self.FullName_textbox = (By.XPATH, "//input[@id='full_name']")
        self.Email_textbox = (By.XPATH, "//input[@id='email']")
        self.Phone_textbox = (By.XPATH, "//input[@id='mobile_no']")
        self.College_textbox = (By.XPATH, "//input[@id='college']")
        self.AcademicStatus = (By.XPATH, "//select[@id='qualification']")
        self.InterestedCourse = (By.XPATH, "//select[@id='course']")
        self.PreferredSchedule = (By.XPATH,"//select[@id='shedule']")
        self.Queries_textbox = (By.XPATH, "//textarea[@id='question']")
        self.InternshipYes = (By.XPATH,"//label[normalize-space()='Yes']")
        self.InternshipNo = (By.XPATH,"//label[normalize-space()='No']")

    def open_page(self, url):
        self.driver.get(url)

    def enter_fullname(self, name):
        self.driver.find_element(*self.FullName_textbox).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*self.Email_textbox).send_keys(email)

    def enter_phone(self, phone):
        self.driver.find_element(*self.Phone_textbox).send_keys(phone)

    def enter_college(self, college):
        self.driver.find_element(*self.College_textbox).send_keys(college)

    def select_academicStatus(self, academic_status):
        select_element = self.driver.find_element(*self.AcademicStatus)
        select = Select(select_element)
        select.select_by_visible_text(academic_status)

    def interested_course(self, course):
        select_course = self.driver.find_element(*self.InterestedCourse)
        select = Select(select_course)
        select.select_by_visible_text(course)

    def preferred_schedule(self,schedule):
        select_schedule = self.driver.find_element(*self.PreferredSchedule)
        select = Select(select_schedule)
        select.select_by_visible_text(schedule)

    # def select_internshipProgram(self, option):
    #     if option.lower() == 'yes':
    #         self.driver.find_element(*self.InternshipYes).click()
    #     elif option.lower() == 'no':
    #         self.driver.find_element(*self.InternshipNo).click()
    #     else:
    #         raise ValueError("Option must be 'Yes' or 'No'")

    def enter_query(self, query):
        self.driver.find_element(*self.Queries_textbox).send_keys(query)
