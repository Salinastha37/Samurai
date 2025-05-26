from pages.superadmin_loginpage import LoginPage

def test_valid_login(setup):
    driver = setup
    driver.get("https://samurai.tai.com.np/super-admin/login")
    login = LoginPage(driver)
    login.enter_email("super-admin@tai.com.np")
    login.enter_password("admin123")
    login.click_login()
    assert "Dashboard" in driver.title
