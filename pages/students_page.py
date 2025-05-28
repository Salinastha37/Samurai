from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebdriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class StudentsPage:
    def _init_(self, driver):
        self.driver = driver
        self.create_input = (By.ID, "create-student")
        self.name_input = (By.NAME, "name")
        self.email_input = (By.NAME, "email")
        self.course_select = (By.NAME, "course")
        self.submit_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.success_alert = (By.CLASS_NAME, "alert-success")
        self.students_table = (By.ID, "students-table")

    def click_create_student(self):
       WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.create_button)
        ).click()

    def fill_student_form(self, name, email, course_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.name_input)
        ).send_keys(name)
        self.driver.find_element(*self.email_input).send_keys(email)
        Select(self.driver.find_element(*self.course_select)).select_by_visible_text(course_name)

    def submit_form(self):
        self.driver.find_element(*self.submit_button).click()

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.success_alert)
        ).text

    def student_exists_in_table(self, name):
        table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.students_table)
        )
        return name in table.text