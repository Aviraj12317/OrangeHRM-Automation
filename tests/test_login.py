"""
Login Tests for OrangeHRM
"""

import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from config import Config


class TestLogin:
    """Test cases for Login functionality"""
    
    @pytest.mark.smoke
    def test_valid_login(self, driver):
        """Test login with valid credentials"""
        login_page = LoginPage(driver)
        dashboard = DashboardPage(driver)
        
        # Verify login page elements
        assert login_page.is_logo_displayed(), "Logo not displayed"
        
        # Perform login
        login_page.login(Config.USERNAME, Config.PASSWORD)
        
        # Verify successful login
        assert dashboard.is_dashboard_displayed(), "Dashboard not displayed after login"
        assert "dashboard" in driver.current_url.lower(), "URL doesn't contain dashboard"
    
    @pytest.mark.regression
    def test_invalid_login_wrong_password(self, driver):
        """Test login with invalid password"""
        login_page = LoginPage(driver)
        
        login_page.login(Config.USERNAME, "wrongpassword")
        
        # Verify error message
        assert login_page.is_error_displayed(), "Error message not displayed"
        error_text = login_page.get_error_message()
        assert "Invalid credentials" in error_text, f"Unexpected error message: {error_text}"
    
    @pytest.mark.regression
    def test_invalid_login_wrong_username(self, driver):
        """Test login with invalid username"""
        login_page = LoginPage(driver)
        
        login_page.login("invaliduser", Config.PASSWORD)
        
        # Verify error message
        assert login_page.is_error_displayed(), "Error message not displayed"
    
    @pytest.mark.regression
    def test_invalid_login_empty_credentials(self, driver):
        """Test login with empty credentials"""
        login_page = LoginPage(driver)
        
        login_page.click_login()
        
        # Verify validation messages appear
        # The form should show required field messages
    
    @pytest.mark.smoke
    def test_logout(self, login):
        """Test logout functionality"""
        driver = login
        dashboard = DashboardPage(driver)
        login_page = LoginPage(driver)
        
        # Perform logout
        dashboard.logout()
        
        # Verify redirected to login page
        assert login_page.is_logo_displayed(), "Not redirected to login page"
    
    @pytest.mark.sanity
    def test_login_page_elements(self, driver):
        """Test all elements on login page are displayed"""
        login_page = LoginPage(driver)
        
        assert login_page.is_logo_displayed(), "Logo not displayed"
        assert login_page.is_displayed(login_page.USERNAME_INPUT), "Username input not displayed"
        assert login_page.is_displayed(login_page.PASSWORD_INPUT), "Password input not displayed"
        assert login_page.is_displayed(login_page.LOGIN_BUTTON), "Login button not displayed"
