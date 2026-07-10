"""
Admin Module Tests
"""

import pytest
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from utils.driver_manager import TestHelpers
import time


class TestAdmin:
    """Test cases for Admin functionality"""
    
    @pytest.mark.regression
    def test_navigate_to_user_management(self, login):
        """Test navigation to User Management"""
        driver = login
        dashboard = DashboardPage(driver)
        admin_page = AdminPage(driver)
        
        # Navigate to Admin
        dashboard.navigate_to_admin()
        time.sleep(2)
        
        # Verify admin page elements
        assert "admin" in driver.current_url.lower(), "Not on Admin page"
    
    @pytest.mark.smoke
    def test_search_users(self, login):
        """Test searching users in admin"""
        driver = login
        dashboard = DashboardPage(driver)
        admin_page = AdminPage(driver)
        
        # Navigate to Admin
        dashboard.navigate_to_admin()
        time.sleep(2)
        
        # Search for admin user
        admin_page.search_user_by_username("Admin")
        time.sleep(2)
        
        # Verify results
        rows = admin_page.get_table_rows_count()
        assert rows > 0, "No search results found"
    
    @pytest.mark.regression
    def test_reset_search(self, login):
        """Test reset button in user search"""
        driver = login
        dashboard = DashboardPage(driver)
        admin_page = AdminPage(driver)
        
        # Navigate to Admin
        dashboard.navigate_to_admin()
        time.sleep(2)
        
        # Search for a user
        admin_page.search_user_by_username("Admin")
        time.sleep(1)
        
        # Click reset
        admin_page.click_reset()
        time.sleep(1)
        
        # Verify search field is cleared
        # The form should be reset
    
    @pytest.mark.regression
    def test_navigate_to_job_titles(self, login):
        """Test navigation to Job Titles"""
        driver = login
        dashboard = DashboardPage(driver)
        admin_page = AdminPage(driver)
        
        # Navigate to Admin
        dashboard.navigate_to_admin()
        time.sleep(2)
        
        # Click Job tab
        admin_page.click_job_tab()
        time.sleep(1)
        
        # Click Job Titles
        admin_page.click_job_titles()
        time.sleep(2)
        
        # Verify navigation
        assert "jobTitle" in driver.current_url or "job" in driver.current_url.lower(), \
            "Not navigated to Job Titles"
    
    @pytest.mark.regression
    def test_navigate_to_locations(self, login):
        """Test navigation to Locations"""
        driver = login
        dashboard = DashboardPage(driver)
        admin_page = AdminPage(driver)
        
        # Navigate to Admin
        dashboard.navigate_to_admin()
        time.sleep(2)
        
        # Click Organization tab
        admin_page.click_organization_tab()
        time.sleep(1)
        
        # Click Locations
        admin_page.click_locations()
        time.sleep(2)
        
        # Verify navigation
        assert "location" in driver.current_url.lower(), "Not navigated to Locations"
    
    @pytest.mark.sanity
    def test_admin_page_elements(self, login):
        """Test Admin page elements are displayed"""
        driver = login
        dashboard = DashboardPage(driver)
        admin_page = AdminPage(driver)
        
        # Navigate to Admin
        dashboard.navigate_to_admin()
        time.sleep(2)
        
        # Verify search elements
        assert admin_page.is_displayed(admin_page.SEARCH_BUTTON), "Search button not displayed"
        assert admin_page.is_displayed(admin_page.RESET_BUTTON), "Reset button not displayed"
        assert admin_page.is_displayed(admin_page.ADD_USER_BUTTON), "Add User button not displayed"
    
    @pytest.mark.regression
    def test_user_list_display(self, login):
        """Test user list displays correctly"""
        driver = login
        dashboard = DashboardPage(driver)
        admin_page = AdminPage(driver)
        
        # Navigate to Admin
        dashboard.navigate_to_admin()
        time.sleep(2)
        
        # Click search to display all users
        admin_page.click_search()
        time.sleep(2)
        
        # Verify users are displayed
        rows = admin_page.get_table_rows_count()
        assert rows > 0, "No users displayed"
