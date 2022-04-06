from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.enums import TakeScreenshotConditionType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: VLFsports
    Package: TestProject.Generated.Tests.VLFsports
    Test: CP-02A
    Generated by: Carlos Leonardo (thorin.1620@gmail.com)
    Generated on 04/04/2022, 03:52:25
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="w0FakVRmj9dNXYcKJPUnZ09uKCtFIu24ziWZm9gCuAE",
                              project_name="VLFsports",
                              job_name="CP-02A")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """ENCONTRAR PRODUCTO."""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://vlfsports.odoo.com"
    Keyword = "Lazo"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Click 'Tienda'
    tienda = driver.find_element(By.XPATH,
                                 "//span[. = 'Tienda']")
    tienda.click()

    # 3. Click 'search'
    search = driver.find_element(By.CSS_SELECTOR,
                                 "[name='search']")
    search.click()

    # 4. Type '{Keyword}' in 'search'
    search = driver.find_element(By.CSS_SELECTOR,
                                 "[name='search']")
    search.send_keys(f'{Keyword}')

    # 5. Click 'I'
    i = driver.find_element(By.XPATH,
                            "//button/i")
    i.click()

    # 6. Click 'IMG'
    step_settings = StepSettings(
        screenshot_condition=TakeScreenshotConditionType.Always)
    with DriverStepSettings(driver, step_settings):
        img = driver.find_element(By.XPATH,
                                  "//td[1]//img")
        img.click()
