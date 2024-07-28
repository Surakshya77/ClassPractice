from selenium.webdriver.common.by import By


class AboutYourselfPage:

    def __init__(self, driver):
        self.driver = driver
        self.FullName_textbox = (By.XPATH, "//input[@id='fullname']")
        self.Phone_Textbox = (By.XPATH, "//input[@id='phone']")
        self.Email_Textbox = (By.XPATH, "//input[@id='email']")
        self.Hobby_Textbox = (By.XPATH, "//input[@id='hobby']")
        self.Submit_Button = (By.XPATH, "//button[normalize-space()='Submit']")

    def open_page(self, url):
        self.driver.get(url)

    def enter_fullname(self, Name):
        self.driver.find_element(*self.FullName_textbox).send_keys(Name)

    def enter_phone(self, Phone):
        self.driver.find_element(*self.Phone_Textbox).send_keys(Phone)

    def enter_email(self, Email):
        self.driver.find_element(*self.Email_Textbox).send_keys(Email)

    def enter_hobby(self, Hobby):
        self.driver.find_element(*self.Hobby_Textbox).send_keys(Hobby)

    def click_submit_button(self):
        self.driver.find_element(*self.Submit_Button).click()
