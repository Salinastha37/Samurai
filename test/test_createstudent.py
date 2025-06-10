import os
import uuid
import random
import pytest
from faker import Faker
from selenium import webdriver
from pages.student_registration import RegistrationPage
from pages.admin_loginpage import LoginPage
from selenium.webdriver.support import expected_conditions as EC


fake = Faker('ja_JP')

def generate_unique_email():
    return f"user_{uuid.uuid4().hex}@test.com"

def get_random_image_path(folder_path="test/images"):
    images = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    return os.path.abspath(os.path.join(folder_path, random.choice(images)))

def get_random_gender():
    return random.choice(["Male", "Female", "Other"])

# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://ai-samurai.tai.com.np/admin/add-student")  # 🔁 Replace this with actual URL
#     yield driver
#     driver.quit()

def test_registration_form(driver):
    
    
    driver.get("https://ai-samurai.tai.com.np/admin/login")
    login = LoginPage(driver)
    login.enter_email("admin@tai.com.np")
    login.enter_password("admin123")
    login.click_login()
    
    driver.get("https://ai-samurai.tai.com.np/admin/add-student")
    reg_page = RegistrationPage(driver)

    test_data = {
        "last-name": fake.last_name(),
        "firstName": fake.first_name(),
        "lastNameKatakana'": "タナカ",
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
    reg_page.submit_form()

    # Basic success check (customize this for your app)
    assert "Registration successful" in driver.page_source

