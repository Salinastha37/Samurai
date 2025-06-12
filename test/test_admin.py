import pytest
from pages.admin_loginpage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

# VALID LOGIN TES
def test_valid_login(driver):
    driver.get("https://ai-samurai.tai.com.np/admin/login")

    login = LoginPage(driver)
    login.enter_email("admin@tai.com.np")   
    login.enter_password("admin123")
    login.click_login()

    try:
        WebDriverWait(driver, 10).until(EC.url_contains("/admin/students"))
    except TimeoutException:
        assert False, "Login failed — student page did not load"

    assert "/admin/students" in driver.current_url


#  INVALID LOGIN TESTS 

@pytest.mark.parametrize("email,password,error_message", [
    ("", "admin123", ""),
    ("admin@tai.com.np", "", ""),
    ("invalidemail", "admin123", " "),
    ("admin@tai.com.np", "wrongpass", "Unauthorized"),
    ("notexist@tai.com.np", "admin123", "Unauthorized"),
    ("a"*256 + "@tai.com.np", "admin123", "Unauthorized"),
    ("admin@tai.com.np", "a"*256, "Unauthorized"),
    ("  admin@tai.com.np  ", "admin123", "Unauthorized"),
])
def test_invalid_login(driver, email, password, error_message):
    driver.get("https://ai-samurai.tai.com.np/admin/login")

    login = LoginPage(driver)
    login.enter_email(email)
    login.enter_password(password)
    login.click_login()

    # Directly define the error locator here
"""  error_locator = (By.CSS_SELECTOR, ".Toastify__toast.Toastify__toast-theme--light Toastify__toast--error")  

    try:
        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(error_locator)
        )
    except TimeoutException:
        assert False, "Expected error message did not appear"

    actual_error = error_element.text
    assert error_message.lower() in actual_error.lower(), \
        f"Expected error containing '{error_message}', but got '{actual_error}'"
"""