from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 10 seconds wait

        # Define locators
        self.email_input = (By.NAME, "email")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def enter_email(self, email):
        email_field = self.wait.until(EC.visibility_of_element_located(self.email_input))
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.wait.until(EC.visibility_of_element_located(self.password_input))
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_btn = self.wait.until(EC.element_to_be_clickable(self.login_button))
        login_btn.click()