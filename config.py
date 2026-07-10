"""
Configuration file for OrangeHRM automation testing
"""

class Config:
    # Base URL
    BASE_URL = "https://opensource-demo.orangehrmlive.com/"
    
    # Login Credentials
    USERNAME = "Admin"
    PASSWORD = "admin123"
    
    # Timeouts (in seconds)
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 20
    PAGE_LOAD_TIMEOUT = 30
    
    # Browser settings
    BROWSER = "chrome"  # Options: chrome, firefox, edge
    HEADLESS = False
    WINDOW_SIZE = "1920,1080"
    
    # Test data
    TEST_EMPLOYEE_FIRST_NAME = "John"
    TEST_EMPLOYEE_LAST_NAME = "Doe"
    TEST_EMPLOYEE_MIDDLE_NAME = "Michael"
    
    # Screenshot settings
    SCREENSHOT_ON_FAILURE = True
    SCREENSHOT_PATH = "reports/screenshots/"
    
    # Report settings
    REPORT_PATH = "reports/"
