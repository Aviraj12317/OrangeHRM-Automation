"""
Base Page Object Model class with common methods
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
    
    def find_element(self, locator):
        """Find a single element"""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Element not found: {locator}")
    
    def find_elements(self, locator):
        """Find multiple elements"""
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return []
    
    def click(self, locator):
        """Click on an element"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def send_keys(self, locator, text):
        """Send keys to an element"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Get text from an element"""
        element = self.find_element(locator)
        return element.text
    
    def is_displayed(self, locator):
        """Check if element is displayed"""
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except:
            return False
    
    def is_enabled(self, locator):
        """Check if element is enabled"""
        element = self.find_element(locator)
        return element.is_enabled()
    
    def wait_for_element(self, locator, timeout=20):
        """Wait for element to be visible"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_element_to_disappear(self, locator, timeout=20):
        """Wait for element to disappear"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.invisibility_of_element_located(locator))
    
    def scroll_to_element(self, locator):
        """Scroll to element"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
    
    def hover_over_element(self, locator):
        """Hover over an element"""
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
    
    def select_dropdown_by_text(self, locator, text):
        """Select dropdown option by visible text"""
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)
    
    def select_dropdown_by_value(self, locator, value):
        """Select dropdown option by value"""
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_value(value)
    
    def get_current_url(self):
        """Get current page URL"""
        return self.driver.current_url
    
    def get_page_title(self):
        """Get page title"""
        return self.driver.title
    
    def take_screenshot(self, filename):
        """Take a screenshot"""
        self.driver.save_screenshot(filename)
    
    def switch_to_frame(self, locator):
        """Switch to iframe"""
        frame = self.find_element(locator)
        self.driver.switch_to.frame(frame)
    
    def switch_to_default_content(self):
        """Switch back to default content"""
        self.driver.switch_to.default_content()
    
    def execute_script(self, script, *args):
        """Execute JavaScript"""
        return self.driver.execute_script(script, *args)
    
    def wait_for_page_load(self):
        """Wait for page to load completely"""
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
