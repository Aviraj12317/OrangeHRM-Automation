"""
Pytest Configuration and Fixtures
"""

import pytest
from utils.driver_manager import DriverManager, TestHelpers
from config import Config
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.fixture(scope="function")
def driver():
    """Setup and teardown WebDriver"""
    # Setup
    TestHelpers.create_report_directory()
    driver = DriverManager.get_driver()
    driver.get(Config.BASE_URL)
    
    yield driver
    
    # Teardown
    driver.quit()


@pytest.fixture(scope="function")
def login(driver):
    """Login fixture to use in tests that require authentication"""
    login_page = LoginPage(driver)
    login_page.login(Config.USERNAME, Config.PASSWORD)
    dashboard = DashboardPage(driver)
    assert dashboard.is_dashboard_displayed(), "Login failed - Dashboard not displayed"
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot on test failure"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get('driver')
        if driver:
            TestHelpers.take_screenshot(driver, item.name)


def pytest_configure(config):
    """Configure pytest"""
    config.addinivalue_line(
        "markers", "smoke: mark test as smoke test"
    )
    config.addinivalue_line(
        "markers", "regression: mark test as regression test"
    )
    config.addinivalue_line(
        "markers", "sanity: mark test as sanity test"
    )
