"""
PIM (Personnel Information Management) Tests
"""

import pytest
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from utils.driver_manager import TestHelpers
from config import Config
import time


class TestPIM:
    """Test cases for PIM functionality"""
    
    @pytest.mark.smoke
    def test_add_employee_without_login(self, login):
        """Test adding employee without creating login credentials"""
        driver = login
        dashboard = DashboardPage(driver)
        pim_page = PIMPage(driver)
        
        # Navigate to PIM
        dashboard.navigate_to_pim()
        time.sleep(1)
        
        # Add employee
        first_name = "Test" + TestHelpers.generate_unique_username()[-6:]
        middle_name = "Middle"
        last_name = "Employee"
        
        pim_page.add_employee(first_name, middle_name, last_name)
        
        # Verify success (usually shows personal details page)
        time.sleep(2)
        assert "personalDetails" in driver.current_url or "viewPersonalDetails" in driver.current_url, \
            "Employee not added successfully"
    
    @pytest.mark.regression
    def test_add_employee_with_login(self, login):
        """Test adding employee with login credentials"""
        driver = login
        dashboard = DashboardPage(driver)
        pim_page = PIMPage(driver)
        
        # Navigate to PIM
        dashboard.navigate_to_pim()
        time.sleep(1)
        
        # Generate unique data
        first_name = "Login" + TestHelpers.generate_unique_username()[-6:]
        middle_name = "Test"
        last_name = "User"
        username = TestHelpers.generate_unique_username()
        password = "Test@1234"
        
        # Add employee with login
        pim_page.add_employee(first_name, middle_name, last_name, 
                            create_login=True, username=username, password=password)
        
        # Verify success
        time.sleep(2)
        assert "personalDetails" in driver.current_url or "viewPersonalDetails" in driver.current_url, \
            "Employee with login not added successfully"
    
    @pytest.mark.regression
    def test_search_employee_list(self, login):
        """Test searching in employee list"""
        driver = login
        dashboard = DashboardPage(driver)
        pim_page = PIMPage(driver)
        
        # Navigate to PIM
        dashboard.navigate_to_pim()
        time.sleep(1)
        
        # Click employee list
        pim_page.click_employee_list()
        time.sleep(1)
        
        # Search for an employee (using a common name that likely exists)
        pim_page.search_employee_by_name("a")
        time.sleep(2)
        pim_page.click_search()
        time.sleep(2)
        
        # Verify results are displayed
        # Note: In demo, there should be some results
    
    @pytest.mark.smoke
    def test_navigate_to_add_employee(self, login):
        """Test navigation to Add Employee page"""
        driver = login
        dashboard = DashboardPage(driver)
        pim_page = PIMPage(driver)
        
        # Navigate to PIM
        dashboard.navigate_to_pim()
        time.sleep(1)
        
        # Click Add Employee
        pim_page.click_add_employee()
        time.sleep(1)
        
        # Verify Add Employee form is displayed
        assert pim_page.is_displayed(pim_page.FIRST_NAME_INPUT), "Add Employee form not displayed"
        assert pim_page.is_displayed(pim_page.LAST_NAME_INPUT), "Last name field not displayed"
    
    @pytest.mark.regression
    def test_employee_list_display(self, login):
        """Test employee list displays correctly"""
        driver = login
        dashboard = DashboardPage(driver)
        pim_page = PIMPage(driver)
        
        # Navigate to PIM
        dashboard.navigate_to_pim()
        time.sleep(1)
        
        # Click employee list
        pim_page.click_employee_list()
        time.sleep(2)
        
        # Click search to load all employees
        pim_page.click_search()
        time.sleep(2)
        
        # Verify table has rows
        rows = pim_page.get_table_rows_count()
        assert rows > 0, "No employees displayed in list"
    
    @pytest.mark.sanity
    def test_pim_page_elements(self, login):
        """Test PIM page elements are displayed"""
        driver = login
        dashboard = DashboardPage(driver)
        pim_page = PIMPage(driver)
        
        # Navigate to PIM
        dashboard.navigate_to_pim()
        time.sleep(1)
        
        # Verify navigation elements
        assert pim_page.is_displayed(pim_page.ADD_EMPLOYEE_BUTTON), "Add Employee button not displayed"
        assert pim_page.is_displayed(pim_page.EMPLOYEE_LIST_BUTTON), "Employee List button not displayed"
