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
    Test: CP-06A
    Generated by: Carlos Leonardo (thorin.1620@gmail.com)
    Generated on 04/07/2022, 23:57:47
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="w0FakVRmj9dNXYcKJPUnZ09uKCtFIu24ziWZm9gCuAE",
                              project_name="VLFsports",
                              job_name="CP-06A")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """Agregar producto."""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://vlfsports.odoo.com"
    correo = ""
    contrasena = ""
    producto = ""

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Click 'Identificarse'
    identificarse = driver.find_element(By.XPATH,
                                        "//a[. = 'Identificarse']")
    identificarse.click()

    # 3. Click 'login'
    login = driver.find_element(By.CSS_SELECTOR,
                                "#login")
    login.click()

    # 4. Type '{correo}' in 'login'
    login = driver.find_element(By.CSS_SELECTOR,
                                "#login")
    login.send_keys(f'{correo}')

    # 5. Click 'password'
    password = driver.find_element(By.CSS_SELECTOR,
                                   "#password")
    password.click()

    # 6. Type '{contrasena}' in 'password'
    password = driver.find_element(By.CSS_SELECTOR,
                                   "#password")
    password.send_keys(f'{contrasena}')

    # 7. Click 'Iniciar sesión'
    iniciar_sesi_n = driver.find_element(By.XPATH,
                                         "//button[. = 'Iniciar sesión']")
    iniciar_sesi_n.click()

    # 8. Click 'DIV6'
    div6 = driver.find_element(By.XPATH,
                               "//a[7]/div[1]")
    div6.click()

    # 9. Click 'IR AL SITIO WEB'
    ir_al_sitio_web = driver.find_element(By.XPATH,
                                          "//a[. = ' Ir al sitio web ']")
    ir_al_sitio_web.click()

    # 10. Click 'Tienda'
    tienda = driver.find_element(By.XPATH,
                                 "//span[. = 'Tienda']")
    tienda.click()

    # 11. Click 'Nuevo1'
    nuevo1 = driver.find_element(By.XPATH,
                                 "//a[. = 'Nuevo']")
    nuevo1.click()

    # 12. Click 'I10'
    i10 = driver.find_element(By.XPATH,
                              "//div[3]/div[2]/div/div/div/div[2]//i")
    i10.click()

    # 13. Type '{producto}' in 'INPUT1'
    input1 = driver.find_element(By.XPATH,
                                 "//form/div/div/input")
    input1.send_keys(f'{producto}')

    # 14. Click 'Crear'
    crear = driver.find_element(By.XPATH,
                                "//button[. = 'Crear']")
    crear.click()

    # 15. Click '1,00'
    _1_00 = driver.find_element(By.XPATH,
                                "//h3[2]//span[. = '1,00']")
    _1_00.click()

    # 16. Click '75'
    _75 = driver.find_element(By.XPATH,
                              "//span[. = '75']")
    _75.click()

    # 17. Click 'Guardar'
    step_settings = StepSettings(
        screenshot_condition=TakeScreenshotConditionType.Always)
    with DriverStepSettings(driver, step_settings):
        guardar = driver.find_element(By.XPATH,
                                      "//button[. = 'Guardar']")
        guardar.click()

    # 18. Click 'SPAN3'
    span3 = driver.find_element(By.XPATH,
                                "//div[1]/label/span[1]")
    span3.click()

    # 19. Click 'Leonardo adames1'
    leonardo_adames1 = driver.find_element(By.XPATH,
                                           "//span[. = 'Leonardo adames']")
    leonardo_adames1.click()

    # 20. Click 'Cerrar sesión'
    cerrar_sesi_n = driver.find_element(By.CSS_SELECTOR,
                                        "#o_logout")
    cerrar_sesi_n.click()
