import os
import uuid
import random
import pytest
import pykakasi
from faker import Faker
from selenium import webdriver
from pages.student_registration import RegistrationPage
from pages.admin_loginpage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

fake_en = Faker('en_US')
fake = Faker('ja_JP')

def convert_to_katakana(name):
    kakasi = pykakasi.kakasi()
    kakasi.setMode("H", "K")
    kakasi.setMode("a", "K")
    kakasi.setMode("r", "Hepburn")
    conv = kakasi.getConverter()
    return conv.do(name)

def generate_unique_email():
    return f"user_{uuid.uuid4().hex}@test.com"

def get_random_image_path(folder_path="test/images"):
    images = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    return os.path.abspath(os.path.join(folder_path, random.choice(images)))

def get_random_gender():
    return random.choice(["Male", "Female", "Other"])

def test_registration_form(driver):
    driver.get("https://ai-samurai.tai.com.np/admin/login")
    login = LoginPage(driver)
    login.enter_email("admin@tai.com.np")
    login.enter_password("admin123")
    login.click_login()

    try:
        WebDriverWait(driver, 10).until(EC.url_contains("/admin/students"))
    except TimeoutException:
        assert False, "Login failed — Student URL did not load"

    try:
        create_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div/div[1]/button"))
        )
        create_btn.click()
    except TimeoutException:
        assert False, "'Create Student' button not found or not clickable"

    WebDriverWait(driver, 50).until(EC.url_contains("/add-student"))

    driver.get("https://ai-samurai.tai.com.np/admin/add-student")
    reg_page = RegistrationPage(driver)

    test_data = {
        "last-name": fake_en.last_name(),
        "firstName": fake_en.first_name(),
        "lastNameKatakana": "タナカ",
        "firstNameKatakana": "タロウ",
        "phone": fake.msisdn()[:11],
        "email": generate_unique_email(),
        "gender": get_random_gender(),
        "dob": fake.date_of_birth(minimum_age=18, maximum_age=30).strftime("%Y-%m-%d"),
        "image_path": get_random_image_path(),
        "postal_code": fake.postcode(),
        "address": fake.address(),
        "nationality": random.choice(["Japanese", "Nepalese", "Filipino"]),
        "background": fake.text(max_nb_chars=100),
        "future_plans": "I want to contribute to global tech.",
        "motivation": fake.paragraph(nb_sentences=2),
        "hobby": random.choice(["Reading", "Gaming", "Photography"]),
    }

    reg_page.fill_registration_form(test_data)
    reg_page.Register_Now()

    # Check for success toast
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Toastify__toast--success"))
        )
    except TimeoutException:
        # Check for error toast if success not found
        try:
            error_toast = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "Toastify__toast--error"))
            )
            print("Registration error: ", error_toast.text)
        except:
            print("No success or error toast appeared.")
        finally:
            driver.save_screenshot("student_registration_failure.png")
        assert False, "Registration failed — toast message not found"

    driver.get("https://ai-samurai.tai.com.np/admin/students")
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//td[contains(text(), '{test_data['email']}')]"))
        )
    except TimeoutException:
        driver.save_screenshot("student_not_found.png")
        assert False, "Registered student not found in the student list"

    print("Test data used:", test_data)
