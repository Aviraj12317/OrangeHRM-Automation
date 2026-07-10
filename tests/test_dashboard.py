"""
Dashboard Tests for OrangeHRM
"""

import pytest
from pages.dashboard_page import DashboardPage
from config import Config


class TestDashboard:
    """Test cases for Dashboard functionality"""
    
    @pytest.mark.smoke
    def test_dashboard_display(self, login):
        """Test dashboard is displayed after login"""
        driver = login
        dashboard = DashboardPage(driver)
        
        assert dashboard.is_dashboard_displayed(), "Dashboard header not displayed"
    
    @pytest.mark.sanity
    def test_all_menu_items_displayed(self, login):
        """Test all main menu items are displayed"""
        driver = login
        dashboard = DashboardPage(driver)
        
        # Verify all menu items are displayed
        assert dashboard.is_displayed(dashboard.ADMIN_MENU), "Admin menu not displayed"
        assert dashboard.is_displayed(dashboard.PIM_MENU), "PIM menu not displayed"
        assert dashboard.is_displayed(dashboard.LEAVE_MENU), "Leave menu not displayed"
        assert dashboard.is_displayed(dashboard.TIME_MENU), "Time menu not displayed"
        assert dashboard.is_displayed(dashboard.RECRUITMENT_MENU), "Recruitment menu not displayed"
        assert dashboard.is_displayed(dashboard.MY_INFO_MENU), "My Info menu not displayed"
        assert dashboard.is_displayed(dashboard.PERFORMANCE_MENU), "Performance menu not displayed"
    
    @pytest.mark.regression
    def test_navigate_to_admin(self, login):
        """Test navigation to Admin module"""
        driver = login
        dashboard = DashboardPage(driver)
        
        dashboard.navigate_to_admin()
        
        assert "admin" in driver.current_url.lower(), "Not navigated to Admin page"
    
    @pytest.mark.regression
    def test_navigate_to_pim(self, login):
        """Test navigation to PIM module"""
        driver = login
        dashboard = DashboardPage(driver)
        
        dashboard.navigate_to_pim()
        
        assert "pim" in driver.current_url.lower(), "Not navigated to PIM page"
    
    @pytest.mark.regression
    def test_navigate_to_leave(self, login):
        """Test navigation to Leave module"""
        driver = login
        dashboard = DashboardPage(driver)
        
        dashboard.navigate_to_leave()
        
        assert "leave" in driver.current_url.lower(), "Not navigated to Leave page"
    
    @pytest.mark.regression
    def test_navigate_to_recruitment(self, login):
        """Test navigation to Recruitment module"""
        driver = login
        dashboard = DashboardPage(driver)
        
        dashboard.navigate_to_recruitment()
        
        assert "recruitment" in driver.current_url.lower(), "Not navigated to Recruitment page"
    
    @pytest.mark.regression
    def test_navigate_to_my_info(self, login):
        """Test navigation to My Info module"""
        driver = login
        dashboard = DashboardPage(driver)
        
        dashboard.navigate_to_my_info()
        
        assert "pim" in driver.current_url.lower(), "Not navigated to My Info page"
    
    @pytest.mark.smoke
    def test_user_dropdown_functionality(self, login):
        """Test user dropdown menu"""
        driver = login
        dashboard = DashboardPage(driver)
        
        # Click user dropdown
        dashboard.click_user_dropdown()
        
        # Verify logout option is displayed
        assert dashboard.is_displayed(dashboard.LOGOUT_LINK), "Logout link not displayed"
