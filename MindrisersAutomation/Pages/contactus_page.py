from selenium.webdriver.common.by import By


class ContactPage:
    def __init__(self,driver):
        self.driver = driver
        self.FullName_textbox = (By.XPATH,"//input[@placeholder='Name']")
        self.Email_textbox = (By.XPATH,"//input[@placeholder='Email']")
        self.Phone_textbox = (By.XPATH,"//input[@placeholder='Phone']")
        self.Subject_textbox = (By.XPATH,"//input[@placeholder='Subject']")
        self.Queries_textbox = (By.XPATH,"//textarea[@placeholder='Queries']")

    def open_Page(self, url):
        self.driver.get(url)

    def enter_FullName(self, name):
        self.driver.find_element(*self.FullName_textbox).send_keys(name)

    def enter_Email(self, email):
        self.driver.find_element(*self.Email_textbox).send_keys(email)

    def enter_Phone(self, phone):
        self.driver.find_element(*self.Phone_textbox).send_keys(phone)
    def enter_Subject(self, subject):
        self.driver.find_element(*self.Subject_textbox).send_keys(subject)

    def enter_Query(self, query):
        self.driver.find_element(*self.Queries_textbox).send_keys(query)

