from pages.admin_loginpage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_valid_login(setup):
    driver = setup
    driver.get("https://ai-samurai.tai.com.np/admin/login")
    login = LoginPage(driver)
    login.enter_email("admin@tai.com.np")
    login.enter_password("admin123")
    login.click_login()
    expected_url = "https://ai-samurai.tai.com.np/admin/students"
    WebDriverWait(driver, 100).until(EC.url_to_be(expected_url))

    assert driver.current_url == expected_url
   