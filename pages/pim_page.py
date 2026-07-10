"""
PIM (Personnel Information Management) Page Object Model
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class PIMPage(BasePage):
    # Locators
    ADD_EMPLOYEE_BUTTON = (By.XPATH, "//a[text()='Add Employee']")
    EMPLOYEE_LIST_BUTTON = (By.XPATH, "//a[text()='Employee List']")
    
    # Add Employee form
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    MIDDLE_NAME_INPUT = (By.NAME, "middleName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    EMPLOYEE_ID_INPUT = (By.XPATH, "//label[text()='Employee Id']/parent::div/following-sibling::div/input")
    CREATE_LOGIN_CHECKBOX = (By.XPATH, "//span[@class='oxd-switch-input']")
    USERNAME_INPUT = (By.XPATH, "//label[text()='Username']/parent::div/following-sibling::div/input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Password']/parent::div/following-sibling::div/input")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//label[text()='Confirm Password']/parent::div/following-sibling::div/input")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    
    # Employee List
    SEARCH_EMPLOYEE_NAME = (By.XPATH, "//label[text()='Employee Name']/parent::div/following-sibling::div//input")
    SEARCH_EMPLOYEE_ID = (By.XPATH, "//label[text()='Employee Id']/parent::div/following-sibling::div/input")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    RESET_BUTTON = (By.XPATH, "//button[text()=' Reset ']")
    
    # Table
    TABLE_ROWS = (By.XPATH, "//div[@class='oxd-table-body']/div[@class='oxd-table-card']")
    DELETE_BUTTON = (By.XPATH, "//i[contains(@class, 'bi-trash')]")
    EDIT_BUTTON = (By.XPATH, "//i[contains(@class, 'bi-pencil-fill')]")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[contains(@class, 'oxd-button--label-danger')]")
    
    # Success message
    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(@class, 'oxd-text--toast-message')]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_add_employee(self):
        """Click Add Employee button"""
        self.click(self.ADD_EMPLOYEE_BUTTON)
    
    def click_employee_list(self):
        """Click Employee List button"""
        self.click(self.EMPLOYEE_LIST_BUTTON)
    
    def enter_first_name(self, first_name):
        """Enter first name"""
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
    
    def enter_middle_name(self, middle_name):
        """Enter middle name"""
        self.send_keys(self.MIDDLE_NAME_INPUT, middle_name)
    
    def enter_last_name(self, last_name):
        """Enter last name"""
        self.send_keys(self.LAST_NAME_INPUT, last_name)
    
    def get_employee_id(self):
        """Get auto-generated employee ID"""
        element = self.find_element(self.EMPLOYEE_ID_INPUT)
        return element.get_attribute("value")
    
    def toggle_create_login(self):
        """Toggle create login details checkbox"""
        self.click(self.CREATE_LOGIN_CHECKBOX)
    
    def enter_username(self, username):
        """Enter username for employee login"""
        self.send_keys(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        """Enter password"""
        self.send_keys(self.PASSWORD_INPUT, password)
    
    def enter_confirm_password(self, password):
        """Enter confirm password"""
        self.send_keys(self.CONFIRM_PASSWORD_INPUT, password)
    
    def click_save(self):
        """Click save button"""
        self.click(self.SAVE_BUTTON)
    
    def add_employee(self, first_name, middle_name, last_name, create_login=False, username=None, password=None):
        """Complete flow to add an employee"""
        self.click_add_employee()
        time.sleep(1)
        self.enter_first_name(first_name)
        self.enter_middle_name(middle_name)
        self.enter_last_name(last_name)
        
        if create_login:
            self.toggle_create_login()
            time.sleep(1)
            self.enter_username(username)
            self.enter_password(password)
            self.enter_confirm_password(password)
        
        self.click_save()
        time.sleep(2)
    
    def search_employee_by_name(self, name):
        """Search employee by name"""
        self.send_keys(self.SEARCH_EMPLOYEE_NAME, name)
        time.sleep(2)  # Wait for autocomplete
    
    def search_employee_by_id(self, employee_id):
        """Search employee by ID"""
        self.send_keys(self.SEARCH_EMPLOYEE_ID, employee_id)
    
    def click_search(self):
        """Click search button"""
        self.click(self.SEARCH_BUTTON)
        time.sleep(1)
    
    def click_reset(self):
        """Click reset button"""
        self.click(self.RESET_BUTTON)
    
    def get_table_rows_count(self):
        """Get number of rows in table"""
        return len(self.find_elements(self.TABLE_ROWS))
    
    def click_delete_first_employee(self):
        """Click delete button for first employee"""
        self.click(self.DELETE_BUTTON)
        time.sleep(1)
        self.click(self.CONFIRM_DELETE_BUTTON)
        time.sleep(2)
    
    def get_success_message(self):
        """Get success message text"""
        return self.get_text(self.SUCCESS_MESSAGE)
