import pytest
from pages.admin_loginpage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.mark.parametrize("email,password,error_message", [
    ("", "admin123", "Email is required"),                   # empty email
    ("admin@tai.com.np", "", "Password is required"),        # empty password
    ("invalidemail", "admin123", "Invalid email format"),    # invalid email format
    ("admin@tai.com.np", "wrongpass", "Invalid credentials"),# wrong password
    ("notexist@tai.com.np", "admin123", "Invalid credentials"), # non-existing user
    ("a"*256 + "@tai.com.np", "admin123", "Invalid email"),  # very long email
    ("admin@tai.com.np", "a"*256, "Password too long"),      # very long password
   ("  admin@tai.com.np  ", "admin123", "Invalid credentials"), # email with spaces
])
def test_invalid_login(setup, email, password, error_message):
    driver = setup
    driver.get("https://ai-samurai.tai.com.np/admin/login")

    login = LoginPage(driver)
    login.enter_email(email)
    login.enter_password(password)
    login.click_login()

    # Wait for error message element to appear, replace selector as per your app
    error_locator = login.get_error_message_locator()  # Implement this in LoginPage
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(error_locator))
    except TimeoutException:
        assert False, "Expected error message did not appear"

    # Verify error message text matches expected (simplified example)
    actual_error = login.get_error_message_text()
    assert error_message.lower() in actual_error.lower(), f"Expected error containing '{error_message}', but got '{actual_error}'"

   