from datetime import datetime
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def init_driver():
    load_dotenv()

    chrome_path = "/usr/bin/google-chrome-stable"
    chrome_driver_path = "/usr/bin/chromedriver"

    options = webdriver.ChromeOptions()
    options.binary_location = chrome_path
    options.add_argument('--headless')  # ヘッドレスモード（ブラウザを表示しない）
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument("--lang=ja")

    service = ChromeService(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def input_to_field(driver, field_name, value):
    try:
        input_field = driver.find_element(By.NAME, field_name)
        input_field.clear()
        input_field.send_keys(value)
    except Exception as e:
        print(f"Exception while inputting to field: {e}")

def click_button(driver, button_name):
    try:
        button = driver.find_element(By.NAME, button_name)
        button.click()
    except Exception as e:
        print(f"Exception while clicking button: {e}")

def click_button_by_text(driver, button_text):
    try:
        button = driver.find_element(By.XPATH, f"//button[text()='{button_text}']")
        button.click()
    except Exception as e:
        print(f"Exception while clicking button by text: {e}")

def click_button_by_type(driver, button_type):
    try:
        button = driver.find_element(By.XPATH, f"//button[@type='{button_type}']")
        button.click()
    except Exception as e:
        print(f"Exception while clicking button by type: {e}")

def wait_for_element(driver, by, value, timeout=10):
    try:
        element_present = EC.presence_of_element_located((by, value))
        WebDriverWait(driver, timeout).until(element_present)
    except Exception as e:
        print(f"Exception while waiting for element: {e}")

def save_screenshot(driver, directory="screenshots", full_page=False):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        screenshot_path = os.path.join(directory, f"screenshot_{timestamp}.png")

        if full_page:
            total_width = driver.execute_script("return document.body.scrollWidth")
            total_height = driver.execute_script("return document.body.scrollHeight")
            driver.set_window_size(total_width, total_height)

        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")
    except Exception as e:
        print(f"Exception while saving screenshot: {e}")
