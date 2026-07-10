"""
Admin Page Object Model
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class AdminPage(BasePage):
    # Locators
    USER_MANAGEMENT_TAB = (By.XPATH, "//span[text()='User Management ']")
    USERS_OPTION = (By.XPATH, "//a[text()='Users']")
    ADD_USER_BUTTON = (By.XPATH, "//button[text()=' Add ']")
    
    # Add/Edit User Form
    USER_ROLE_DROPDOWN = (By.XPATH, "//label[text()='User Role']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//label[text()='Employee Name']/parent::div/following-sibling::div//input")
    STATUS_DROPDOWN = (By.XPATH, "//label[text()='Status']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
    USERNAME_INPUT = (By.XPATH, "//label[text()='Username']/parent::div/following-sibling::div/input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Password']/parent::div/following-sibling::div/input")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//label[text()='Confirm Password']/parent::div/following-sibling::div/input")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    CANCEL_BUTTON = (By.XPATH, "//button[text()=' Cancel ']")
    
    # Search section
    SEARCH_USERNAME_INPUT = (By.XPATH, "//label[text()='Username']/parent::div/following-sibling::div/input")
    SEARCH_USER_ROLE_DROPDOWN = (By.XPATH, "//label[text()='User Role']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
    SEARCH_EMPLOYEE_NAME_INPUT = (By.XPATH, "//label[text()='Employee Name']/parent::div/following-sibling::div//input")
    SEARCH_STATUS_DROPDOWN = (By.XPATH, "//label[text()='Status']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    RESET_BUTTON = (By.XPATH, "//button[text()=' Reset ']")
    
    # Job Menu
    JOB_TAB = (By.XPATH, "//span[text()='Job ']")
    JOB_TITLES_OPTION = (By.XPATH, "//a[text()='Job Titles']")
    PAY_GRADES_OPTION = (By.XPATH, "//a[text()='Pay Grades']")
    EMPLOYMENT_STATUS_OPTION = (By.XPATH, "//a[text()='Employment Status']")
    JOB_CATEGORIES_OPTION = (By.XPATH, "//a[text()='Job Categories']")
    WORK_SHIFTS_OPTION = (By.XPATH, "//a[text()='Work Shifts']")
    
    # Organization Menu
    ORGANIZATION_TAB = (By.XPATH, "//span[text()='Organization ']")
    GENERAL_INFO_OPTION = (By.XPATH, "//a[text()='General Information']")
    LOCATIONS_OPTION = (By.XPATH, "//a[text()='Locations']")
    STRUCTURE_OPTION = (By.XPATH, "//a[text()='Structure']")
    
    # Table
    TABLE_ROWS = (By.XPATH, "//div[@class='oxd-table-body']/div[@class='oxd-table-card']")
    EDIT_BUTTON = (By.XPATH, "//i[contains(@class, 'bi-pencil-fill')]")
    DELETE_BUTTON = (By.XPATH, "//i[contains(@class, 'bi-trash')]")
    CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[contains(@class, 'oxd-button--label-danger')]")
    
    # Success/Error Messages
    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(@class, 'oxd-text--toast-message')]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_user_management(self):
        """Click User Management tab"""
        self.click(self.USER_MANAGEMENT_TAB)
    
    def click_users(self):
        """Click Users option"""
        self.click(self.USERS_OPTION)
    
    def click_add_user(self):
        """Click Add User button"""
        self.click(self.ADD_USER_BUTTON)
    
    def select_user_role(self, role):
        """Select user role from dropdown"""
        self.click(self.USER_ROLE_DROPDOWN)
        time.sleep(0.5)
        role_option = (By.XPATH, f"//span[text()='{role}']")
        self.click(role_option)
    
    def enter_employee_name(self, name):
        """Enter employee name"""
        self.send_keys(self.EMPLOYEE_NAME_INPUT, name)
        time.sleep(2)  # Wait for autocomplete
        # Select first option from autocomplete
        first_option = (By.XPATH, "//div[@role='listbox']//span")
        try:
            self.click(first_option)
        except:
            pass
    
    def select_status(self, status):
        """Select status from dropdown"""
        self.click(self.STATUS_DROPDOWN)
        time.sleep(0.5)
        status_option = (By.XPATH, f"//span[text()='{status}']")
        self.click(status_option)
    
    def enter_username(self, username):
        """Enter username"""
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
        time.sleep(2)
    
    def click_cancel(self):
        """Click cancel button"""
        self.click(self.CANCEL_BUTTON)
    
    def add_user(self, role, employee_name, status, username, password):
        """Complete flow to add a user"""
        self.click_add_user()
        time.sleep(1)
        self.select_user_role(role)
        self.enter_employee_name(employee_name)
        self.select_status(status)
        self.enter_username(username)
        self.enter_password(password)
        self.enter_confirm_password(password)
        self.click_save()
    
    def search_user_by_username(self, username):
        """Search user by username"""
        self.send_keys(self.SEARCH_USERNAME_INPUT, username)
        self.click_search()
    
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
    
    def click_job_tab(self):
        """Click Job tab"""
        self.click(self.JOB_TAB)
    
    def click_job_titles(self):
        """Click Job Titles option"""
        self.click(self.JOB_TITLES_OPTION)
    
    def click_organization_tab(self):
        """Click Organization tab"""
        self.click(self.ORGANIZATION_TAB)
    
    def click_locations(self):
        """Click Locations option"""
        self.click(self.LOCATIONS_OPTION)
    
    def get_success_message(self):
        """Get success message text"""
        return self.get_text(self.SUCCESS_MESSAGE)
