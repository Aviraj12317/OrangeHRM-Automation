"""
Leave Module Tests
"""

import pytest
from pages.dashboard_page import DashboardPage
from pages.leave_page import LeavePage
from utils.driver_manager import TestHelpers
import time
from datetime import datetime, timedelta


class TestLeave:
    """Test cases for Leave functionality"""
    
    @pytest.mark.regression
    def test_navigate_to_leave_module(self, login):
        """Test navigation to Leave module"""
        driver = login
        dashboard = DashboardPage(driver)
        
        # Navigate to Leave
        dashboard.navigate_to_leave()
        time.sleep(2)
        
        # Verify navigation
        assert "leave" in driver.current_url.lower(), "Not navigated to Leave page"
    
    @pytest.mark.smoke
    def test_navigate_to_apply_leave(self, login):
        """Test navigation to Apply Leave page"""
        driver = login
        dashboard = DashboardPage(driver)
        leave_page = LeavePage(driver)
        
        # Navigate to Leave
        dashboard.navigate_to_leave()
        time.sleep(2)
        
        # Click Apply Leave
        leave_page.click_apply_leave()
        time.sleep(2)
        
        # Verify Apply Leave form is displayed
        assert leave_page.is_displayed(leave_page.LEAVE_TYPE_DROPDOWN), \
            "Apply Leave form not displayed"
    
    @pytest.mark.regression
    def test_navigate_to_my_leave(self, login):
        """Test navigation to My Leave page"""
        driver = login
        dashboard = DashboardPage(driver)
        leave_page = LeavePage(driver)
        
        # Navigate to Leave
        dashboard.navigate_to_leave()
        time.sleep(2)
        
        # Click My Leave
        leave_page.click_my_leave()
        time.sleep(2)
        
        # Verify My Leave page is displayed
        assert "viewMyLeaveList" in driver.current_url or "leave" in driver.current_url.lower(), \
            "Not on My Leave page"
    
    @pytest.mark.regression
    def test_navigate_to_leave_list(self, login):
        """Test navigation to Leave List page"""
        driver = login
        dashboard = DashboardPage(driver)
        leave_page = LeavePage(driver)
        
        # Navigate to Leave
        dashboard.navigate_to_leave()
        time.sleep(2)
        
        # Click Leave List
        leave_page.click_leave_list()
        time.sleep(2)
        
        # Verify Leave List page is displayed
        assert "viewLeaveList" in driver.current_url or "leave" in driver.current_url.lower(), \
            "Not on Leave List page"
    
    @pytest.mark.regression
    def test_apply_leave_form_elements(self, login):
        """Test Apply Leave form has all required elements"""
        driver = login
        dashboard = DashboardPage(driver)
        leave_page = LeavePage(driver)
        
        # Navigate to Leave
        dashboard.navigate_to_leave()
        time.sleep(2)
        
        # Click Apply Leave
        leave_page.click_apply_leave()
        time.sleep(2)
        
        # Verify form elements
        assert leave_page.is_displayed(leave_page.LEAVE_TYPE_DROPDOWN), "Leave Type dropdown not displayed"
        assert leave_page.is_displayed(leave_page.FROM_DATE_INPUT), "From Date input not displayed"
        assert leave_page.is_displayed(leave_page.TO_DATE_INPUT), "To Date input not displayed"
        assert leave_page.is_displayed(leave_page.APPLY_BUTTON), "Apply button not displayed"
    
    @pytest.mark.sanity
    def test_leave_page_navigation_buttons(self, login):
        """Test Leave page navigation buttons are displayed"""
        driver = login
        dashboard = DashboardPage(driver)
        leave_page = LeavePage(driver)
        
        # Navigate to Leave
        dashboard.navigate_to_leave()
        time.sleep(2)
        
        # Verify navigation buttons
        assert leave_page.is_displayed(leave_page.APPLY_LEAVE_BUTTON), "Apply button not displayed"
        assert leave_page.is_displayed(leave_page.MY_LEAVE_BUTTON), "My Leave button not displayed"
        assert leave_page.is_displayed(leave_page.LEAVE_LIST_BUTTON), "Leave List button not displayed"
    
    @pytest.mark.regression
    def test_search_leave_by_date(self, login):
        """Test searching leave records by date"""
        driver = login
        dashboard = DashboardPage(driver)
        leave_page = LeavePage(driver)
        
        # Navigate to Leave List
        dashboard.navigate_to_leave()
        time.sleep(2)
        leave_page.click_my_leave()
        time.sleep(2)
        
        # Get current date and search
        today = datetime.now().strftime("%Y-%m-%d")
        future_date = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        
        leave_page.search_leave(today, future_date)
        time.sleep(2)
        
        # Verify search completed (page loaded)
