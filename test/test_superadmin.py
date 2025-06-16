from pages.superadmin_loginpage import LoginPage
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


# def test_valid_login(setup):
#     driver = setup
#     driver.get("https://samurai.tai.com.np/super-admin/login")
#     login = LoginPage(driver)
#     login.enter_email("super-admin@tai.com.np")
#     login.enter_password("admin123")
#     login.click_login()
#     assert "Dashboard" in driver.title
def test_valid_login(driver):
    driver.get("https://ai-samurai.tai.com.np/sa/login")

    login = LoginPage(driver)
    login.enter_email("super-admin@tai.com.np")   
    login.enter_password("admin123")
    login.click_login()

    try:
        WebDriverWait(driver, 10).until(EC.url_contains("/sa"))
    except TimeoutException:
        assert False, "Login failed — student page did not load"
        #  Pause for 3 seconds to hold on dashboard
        time.sleep(10)

    assert "/sa" in driver.current_url


#  INVALID LOGIN TESTS 

@pytest.mark.parametrize("email,password,error_message", [
    ("", "admin123", ""),
    ("super-admin@tai.com.np", "", ""),
    ("invalidemail", "admin123", " "),
    ("super-admin@tai.com.np", "wrongpass", "Unauthorized"),
    ("notexist@tai.com.np", "admin123", "Unauthorized"),
    ("sa"*256 + "@tai.com.np", "admin123", "Unauthorized"),
    ("super-admin@tai.com.np", "a"*256, "Unauthorized"),
    ("  super-admin@tai.com.np  ", "admin123", "Unauthorized"),
    ("super-admin@tai.com.np  ", "   admin123", "Unauthorized"),
  ])
def test_invalid_login(driver, email, password, error_message):
    driver.get("https://ai-samurai.tai.com.np/admin/login")

    login = LoginPage(driver)
    login.enter_email(email)
    login.enter_password(password)
    login.click_login()
