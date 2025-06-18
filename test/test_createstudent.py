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
import re



fake_en = Faker('en_US')
fake = Faker('ja_JP')
# Convert to Katakana
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
    valid_images = []
    for img in images:
        path = os.path.join(folder_path, img)
        if os.path.getsize(path) <= 2 * 1024 * 1024:  # 2MB in bytes
            valid_images.append(img)
    if not valid_images:
        print(" No valid image found under 2MB with supported formats (JPG, PNG, WEBP, GIF)")
        raise FileNotFoundError("No valid image found under 2MB with supported formats (JPG, PNG, WEBP, GIF)")
    return os.path.abspath(os.path.join(folder_path, random.choice(images)))

def valid_phone(number):
    #returns true if phone mumber is exactly 10/11 digits.
    return re.fullmatch(r"\d{10,11}", number) is not None

def get_random_gender():
    return random.choice(["Male", "Female", "Other"])



def test_registration_form(driver):
    
    
    driver.get("https://ai-samurai.tai.com.np/admin/login")
    login = LoginPage(driver)
    login.enter_email("admin@tai.com.np")
    login.enter_password("admin123")
    login.click_login()
    
    #  Wait for URL to confirm successful login (update if the URL differs)
    try:
        WebDriverWait(driver, 10).until(
            EC.url_contains("/admin/students")  # Adjust this path if needed
        )
    except TimeoutException:
        assert False, "Login failed — Student URL did not load"

     #  Click "Create Student" button
    try:
        create_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div/div[1]/button"))
    )
        create_btn.click()
    except TimeoutException:
        assert False, "'Create Student' button not found or not clickable"

     
    wait = WebDriverWait(driver, 50)  # wait up to 10 seconds
    wait.until(EC.url_contains("/add-student"))
    
    driver.get("https://ai-samurai.tai.com.np/admin/add-student")
    reg_page = RegistrationPage(driver)
    
    #Generate and validate phone number
    raw_phone = fake.msisdn()
    phone = ''.join(filter(str.isdigit, raw_phone))[:11]
    assert valid_phone(phone), f"Generated phone number is invalid: {phone}"

    test_data = {
        "last-name": fake_en.last_name(),
        "firstName": fake_en.first_name(),
        "lastNameKatakana": "タナカ",
        "firstNameKatakana": "タロウ",
        "phone": phone,
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
    
    # Optional: take a screenshot
    driver.save_screenshot("after_submission.png")
    
# Optional: print page source or visible toast
    print("Page source snippet:", driver.page_source[:1000])


    
#     # Wait for redirect to student list page
#     WebDriverWait(driver, 10).until(
#      EC.url_contains("/admin/students")
#     )

# # Confirm redirect occurred
#     assert "/admin/students" in driver.current_url
#navigate to the list to verify 
    # driver.get("https://ai-samurai.tai.com.np/admin/students")
    # try:
    #     WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located(
    #             (By.XPATH, f"//td[contains(text(), '{test_data['email']}')]")
    #         )
    #     )
    # except TimeoutException:
    #     assert False, "Registered student not found in the student list"

