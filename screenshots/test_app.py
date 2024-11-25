import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

# Función para configurar el WebDriver
@pytest.fixture(scope="module")
def setup():
    # Cambia la ruta de chromedriver si es necesario
    service = Service(r"C:\Seleniumdriver\chromedriver.exe")
    chrome_options = Options()

    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

# Función para capturar la pantalla
def capture_screenshot(driver, test_name):
    screenshot_dir = "screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    
    screenshot_path = os.path.join(screenshot_dir, f"{test_name}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Captura de pantalla guardada en {screenshot_path}")

# Prueba de ejemplo con captura de pantalla
def test_search(setup):
    driver = setup
    try:
        driver.get('https://www.google.com')
        time.sleep(2)
        search_box = driver.find_element(By.NAME, 'q')
        search_box.send_keys('ChromeDriver')
        search_box.submit()
        time.sleep(2)
    except Exception as e:
        capture_screenshot(driver, "test_search_fail")
        raise e

# Prueba de ejemplo sin error
def test_login(setup):
    driver = setup
    driver.get('https://www.google.com')
    time.sleep(2)
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('Selenium')
    search_box.submit()
    time.sleep(2)
