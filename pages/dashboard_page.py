"""
Dashboard Page Object Model
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    # Locators
    DASHBOARD_HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    USER_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown-tab")
    LOGOUT_LINK = (By.XPATH, "//a[text()='Logout']")
    
    # Menu items
    ADMIN_MENU = (By.XPATH, "//span[text()='Admin']")
    PIM_MENU = (By.XPATH, "//span[text()='PIM']")
    LEAVE_MENU = (By.XPATH, "//span[text()='Leave']")
    TIME_MENU = (By.XPATH, "//span[text()='Time']")
    RECRUITMENT_MENU = (By.XPATH, "//span[text()='Recruitment']")
    MY_INFO_MENU = (By.XPATH, "//span[text()='My Info']")
    PERFORMANCE_MENU = (By.XPATH, "//span[text()='Performance']")
    DASHBOARD_MENU = (By.XPATH, "//span[text()='Dashboard']")
    DIRECTORY_MENU = (By.XPATH, "//span[text()='Directory']")
    MAINTENANCE_MENU = (By.XPATH, "//span[text()='Maintenance']")
    BUZZ_MENU = (By.XPATH, "//span[text()='Buzz']")
    
    # Dashboard widgets
    TIME_AT_WORK_WIDGET = (By.XPATH, "//p[text()='Time at Work']")
    MY_ACTIONS_WIDGET = (By.XPATH, "//p[text()='My Actions']")
    QUICK_LAUNCH_WIDGET = (By.XPATH, "//p[text()='Quick Launch']")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def is_dashboard_displayed(self):
        """Check if dashboard is displayed"""
        return self.is_displayed(self.DASHBOARD_HEADER)
    
    def click_user_dropdown(self):
        """Click on user dropdown"""
        self.click(self.USER_DROPDOWN)
    
    def logout(self):
        """Logout from application"""
        self.click_user_dropdown()
        self.click(self.LOGOUT_LINK)
    
    def navigate_to_admin(self):
        """Navigate to Admin menu"""
        self.click(self.ADMIN_MENU)
    
    def navigate_to_pim(self):
        """Navigate to PIM menu"""
        self.click(self.PIM_MENU)
    
    def navigate_to_leave(self):
        """Navigate to Leave menu"""
        self.click(self.LEAVE_MENU)
    
    def navigate_to_time(self):
        """Navigate to Time menu"""
        self.click(self.TIME_MENU)
    
    def navigate_to_recruitment(self):
        """Navigate to Recruitment menu"""
        self.click(self.RECRUITMENT_MENU)
    
    def navigate_to_my_info(self):
        """Navigate to My Info menu"""
        self.click(self.MY_INFO_MENU)
    
    def navigate_to_performance(self):
        """Navigate to Performance menu"""
        self.click(self.PERFORMANCE_MENU)
    
    def navigate_to_directory(self):
        """Navigate to Directory menu"""
        self.click(self.DIRECTORY_MENU)
    
    def navigate_to_buzz(self):
        """Navigate to Buzz menu"""
        self.click(self.BUZZ_MENU)
    
    def is_time_at_work_widget_displayed(self):
        """Check if Time at Work widget is displayed"""
        return self.is_displayed(self.TIME_AT_WORK_WIDGET)
