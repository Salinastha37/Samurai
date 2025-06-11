from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_registration_form(self, data):
     WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='last-name']"))
    ).send_keys(data['last-name'])

     self.driver.find_element(By.XPATH, "//*[@id='firstName']").send_keys(data['firstName'])
     self.driver.find_element(By.XPATH, "//*[@id='lastNameKatakana']").send_keys(data['lastNameKatakana'])
     self.driver.find_element(By.XPATH, "//*[@id='firstNameKatakana']").send_keys(data['firstNameKatakana'])
     self.driver.find_element(By.XPATH, "//*[@id='phone']").send_keys(data['phone'])
     self.driver.find_element(By.XPATH, "//*[@id='email']").send_keys(data['email'])

     #gender_element = self.driver.find_element(By.XPATH, "label[@for='gender']")
     #Select(gender_element).select_by_visible_text(data['gender'])

    # More reliable selectors for dynamic IDs
     self.driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/div[2]/form/div[6]/div/div/input').send_keys(data['dob'])
     self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(data['image_path'])

     self.driver.find_element(By.XPATH, "//*[@id='postal_code']").send_keys(data['postal_code'])
     self.driver.find_element(By.XPATH, "//*[@id='address']").send_keys(data['address'])
     self.driver.find_element(By.XPATH, "//*[@id='nationality']").send_keys(data['nationality'])
     self.driver.find_element(By.XPATH, "//*[@id='background']").send_keys(data['background'])
     self.driver.find_element(By.XPATH, "//*[@id='future_plans']").send_keys(data['future_plans'])
     self.driver.find_element(By.XPATH, "//*[@id='motivation_for_application']").send_keys(data['motivation'])
     self.driver.find_element(By.XPATH, "//*[@id='hobby']").send_keys(data['hobby'])

    def Register_Now(self):
    # Prefer clicking the button based on visible text or class
     self.driver.find_element(By.XPATH, '//button[text()="Register Now"]').click()

