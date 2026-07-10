"""
Login Page Object Model
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'alert-content-text')]")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//p[contains(text(), 'Forgot your password')]")
    LOGO = (By.XPATH, "//img[@alt='company-branding']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def enter_username(self, username):
        """Enter username"""
        self.send_keys(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        """Enter password"""
        self.send_keys(self.PASSWORD_INPUT, password)
    
    def click_login(self):
        """Click login button"""
        self.click(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        """Complete login flow"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    def get_error_message(self):
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self):
        """Check if error message is displayed"""
        return self.is_displayed(self.ERROR_MESSAGE)
    
    def is_logo_displayed(self):
        """Check if logo is displayed"""
        return self.is_displayed(self.LOGO)
    
    def click_forgot_password(self):
        """Click forgot password link"""
        self.click(self.FORGOT_PASSWORD_LINK)
