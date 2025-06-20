from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_registration_form(self, data):
        WebDriverWait(self.driver, 50).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='last-name']"))
        ).send_keys(data['last-name'])
        # wait = WebDriverWait(self.driver, 50)
        # wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='last-name']")))
        self.driver.find_element(By.XPATH, "//*[@id='firstName']").send_keys(data['firstName'])
        self.driver.find_element(By.XPATH, "//*[@id='lastNameKatakana']").send_keys(data['lastNameKatakana'])
        self.driver.find_element(By.XPATH, "//*[@id='firstNameKatakana']").send_keys(data['firstNameKatakana'])
        self.driver.find_element(By.XPATH, "//*[@id='phone']").send_keys(data['phone'])
        self.driver.find_element(By.XPATH, "//*[@id='email']").send_keys(data['email'])

        # Select gender
        gender_buttons = self.driver.find_elements(By.XPATH, "//button[contains(@class,'MuiToggleButton-root')]")
        for button in gender_buttons:
            label = button.text.strip().lower()
            if data['gender'].strip().lower() in label:
                button.click()
                break
        
      #  Fill Date of Birth
        dob_value = data["dob"]
        dob_input = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='YYYY/MM/DD']"))
       )
        dob_input.send_keys(dob_value)



        # Upload image
        self.driver.find_element(By.XPATH, "//input[@type='file']").send_keys(data['image_path'])

        self.driver.find_element(By.XPATH, "//*[@id='postal_code']").send_keys(data['postal_code'])
        self.driver.find_element(By.XPATH, "//*[@id='address']").send_keys(data['address'])
        self.driver.find_element(By.XPATH, "//*[@id='nationality']").send_keys(data['nationality'])
        self.driver.find_element(By.XPATH, "//*[@id='background']").send_keys(data['background'])
        self.driver.find_element(By.XPATH, "//*[@id='future_plans']").send_keys(data['future_plans'])
        self.driver.find_element(By.XPATH, "//*[@id='motivation_for_application']").send_keys(data['motivation'])
        self.driver.find_element(By.XPATH, "//*[@id='hobby']").send_keys(data['hobby'])

    def Register_Now(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Register Now"]'))
        ).click()

