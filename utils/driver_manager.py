"""
Test Utilities - Driver Management and Helpers
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

try:
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
except ModuleNotFoundError as exc:
    raise ModuleNotFoundError(
        "webdriver_manager is required. Install it with: pip install webdriver-manager"
    ) from exc

from config import Config
import os
from datetime import datetime


class DriverManager:
    """Manage WebDriver instances"""
    
    @staticmethod
    def get_driver(browser=None):
        """Initialize and return WebDriver based on configuration"""
        browser = browser or Config.BROWSER
        
        if browser.lower() == "chrome":
            options = webdriver.ChromeOptions()
            if Config.HEADLESS:
                options.add_argument("--headless")
            options.add_argument(f"--window-size={Config.WINDOW_SIZE}")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-infobars")
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            
        elif browser.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            if Config.HEADLESS:
                options.add_argument("--headless")
            
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
            
        elif browser.lower() == "edge":
            options = webdriver.EdgeOptions()
            if Config.HEADLESS:
                options.add_argument("--headless")
            options.add_argument(f"--window-size={Config.WINDOW_SIZE}")
            
            service = EdgeService(EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service, options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
        driver.maximize_window()
        
        return driver


class TestHelpers:
    """Helper functions for tests"""
    
    @staticmethod
    def take_screenshot(driver, test_name):
        """Take screenshot on test failure"""
        if Config.SCREENSHOT_ON_FAILURE:
            screenshot_dir = Config.SCREENSHOT_PATH
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"{screenshot_dir}{test_name}_{timestamp}.png"
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")
            return screenshot_path
        return None
    
    @staticmethod
    def generate_unique_username():
        """Generate unique username with timestamp"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"user_{timestamp}"
    
    @staticmethod
    def generate_unique_employee_id():
        """Generate unique employee ID"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"EMP{timestamp}"
    
    @staticmethod
    def get_current_date():
        """Get current date in YYYY-MM-DD format"""
        return datetime.now().strftime("%Y-%m-%d")
    
    @staticmethod
    def create_report_directory():
        """Create report directory if it doesn't exist"""
        if not os.path.exists(Config.REPORT_PATH):
            os.makedirs(Config.REPORT_PATH)
        if not os.path.exists(Config.SCREENSHOT_PATH):
            os.makedirs(Config.SCREENSHOT_PATH)
