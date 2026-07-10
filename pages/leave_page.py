"""
Leave Management Page Object Model
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class LeavePage(BasePage):
    # Locators
    APPLY_LEAVE_BUTTON = (By.XPATH, "//a[text()='Apply']")
    MY_LEAVE_BUTTON = (By.XPATH, "//a[text()='My Leave']")
    LEAVE_LIST_BUTTON = (By.XPATH, "//a[text()='Leave List']")
    ASSIGN_LEAVE_BUTTON = (By.XPATH, "//a[text()='Assign Leave']")
    
    # Apply Leave Form
    LEAVE_TYPE_DROPDOWN = (By.XPATH, "//label[text()='Leave Type']/parent::div/following-sibling::div//div[@class='oxd-select-text-input']")
    FROM_DATE_INPUT = (By.XPATH, "//label[text()='From Date']/parent::div/following-sibling::div//input")
    TO_DATE_INPUT = (By.XPATH, "//label[text()='To Date']/parent::div/following-sibling::div//input")
    COMMENTS_TEXTAREA = (By.XPATH, "//textarea[@placeholder='Type comment here']")
    APPLY_BUTTON = (By.XPATH, "//button[@type='submit']")
    
    # Leave List Search
    FROM_DATE_SEARCH = (By.XPATH, "//label[text()='From Date']/parent::div/following-sibling::div//input")
    TO_DATE_SEARCH = (By.XPATH, "//label[text()='To Date']/parent::div/following-sibling::div//input")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    RESET_BUTTON = (By.XPATH, "//button[text()=' Reset ']")
    
    # Leave Balance
    LEAVE_BALANCE_WIDGET = (By.XPATH, "//p[text()='Leave Balance (Days)']")
    
    # Table
    TABLE_ROWS = (By.XPATH, "//div[@class='oxd-table-body']/div[@class='oxd-table-card']")
    
    # Messages
    SUCCESS_MESSAGE = (By.XPATH, "//p[contains(@class, 'oxd-text--toast-message')]")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_apply_leave(self):
        """Click Apply Leave button"""
        self.click(self.APPLY_LEAVE_BUTTON)
    
    def click_my_leave(self):
        """Click My Leave button"""
        self.click(self.MY_LEAVE_BUTTON)
    
    def click_leave_list(self):
        """Click Leave List button"""
        self.click(self.LEAVE_LIST_BUTTON)
    
    def click_assign_leave(self):
        """Click Assign Leave button"""
        self.click(self.ASSIGN_LEAVE_BUTTON)
    
    def select_leave_type(self, leave_type):
        """Select leave type from dropdown"""
        self.click(self.LEAVE_TYPE_DROPDOWN)
        time.sleep(0.5)
        leave_option = (By.XPATH, f"//span[text()='{leave_type}']")
        self.click(leave_option)
    
    def enter_from_date(self, date):
        """Enter from date"""
        self.send_keys(self.FROM_DATE_INPUT, date)
    
    def enter_to_date(self, date):
        """Enter to date"""
        self.send_keys(self.TO_DATE_INPUT, date)
    
    def enter_comments(self, comments):
        """Enter comments"""
        self.send_keys(self.COMMENTS_TEXTAREA, comments)
    
    def click_apply(self):
        """Click apply button"""
        self.click(self.APPLY_BUTTON)
        time.sleep(2)
    
    def apply_leave(self, leave_type, from_date, to_date, comments=""):
        """Complete flow to apply leave"""
        self.click_apply_leave()
        time.sleep(1)
        self.select_leave_type(leave_type)
        self.enter_from_date(from_date)
        self.enter_to_date(to_date)
        if comments:
            self.enter_comments(comments)
        self.click_apply()
    
    def search_leave(self, from_date, to_date):
        """Search leave by date range"""
        self.enter_from_date(from_date)
        self.enter_to_date(to_date)
        self.click(self.SEARCH_BUTTON)
        time.sleep(1)
    
    def get_table_rows_count(self):
        """Get number of rows in table"""
        return len(self.find_elements(self.TABLE_ROWS))
    
    def get_success_message(self):
        """Get success message text"""
        return self.get_text(self.SUCCESS_MESSAGE)
