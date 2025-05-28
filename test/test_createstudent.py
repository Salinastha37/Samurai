import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.students_page import StudentsPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_create_student(driver):
    login_page = LoginPage(driver)
    students_page = StudentsPage(driver)

    login_page.load("http://your-app-url.com/login")
    login_page.login("admin@example.com", "yourpassword")

    # Wait for redirect to /admin/students
    assert "/admin/students" in driver.current_url

    students_page.click_create_student()
    students_page.fill_student_form("John Doe", "john.doe@example.com", "Math 101")
    students_page.submit_form()

    success_message = students_page.get_success_message()
    assert "Student created successfully" in success_message

    assert students_page.student_exists_in_table("John Doe")
