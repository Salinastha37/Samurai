from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_registration_form(self, data):
        self.driver.find_element(By.ID, "last-name").send_keys(data['last-name'])
        self.driver.find_element(By.ID, "firstName").send_keys(data['firstName'])
        self.driver.find_element(By.ID, "lastNameKatakana").send_keys(data['lastNameKatakana'])
        self.driver.find_element(By.ID, "firstNameKatakana").send_keys(data['firstNameKatakana'])
        self.driver.find_element(By.ID, "phone").send_keys(data['phone'])
        self.driver.find_element(By.ID, "email").send_keys(data['email'])
        Select(self.driver.find_element(By.ID, "gender")).select_by_visible_text(data['gender'])
        self.driver.find_element(By.ID, ":r26:").send_keys(data['dob'])
        self.driver.find_element(By.ID, ":r29:").send_keys(data['image_path'])
        self.driver.find_element(By.ID, "postal_code").send_keys(data['postal_code'])
        self.driver.find_element(By.ID, "address").send_keys(data['address'])
        self.driver.find_element(By.ID, "nationality").send_keys(data['nationality'])
        self.driver.find_element(By.ID, "background").send_keys(data['background'])
        self.driver.find_element(By.ID, "future_plans").send_keys(data['future_plans'])
        self.driver.find_element(By.ID, "motivation_for_application").send_keys(data['motivation'])
        self.driver.find_element(By.ID, "hobby").send_keys(data['hobby'])

    def submit_form(self):
        self.driver.find_element(By.ID, ":r2h:").click()
