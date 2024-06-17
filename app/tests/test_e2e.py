import pytest
from src.selenium_helpers import click_button_by_type, init_driver, input_to_field, save_screenshot, wait_for_element
from getpass import getpass
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def driver():
    driver = init_driver()
    yield driver
    driver.quit()

def test_login_and_verify_title(driver):
    url = input("Enter the URL of the page you want to scrape: ")
    driver.get(url)

    # ユーザー名を入力
    value = input("Enter your email: ")
    input_to_field(driver, "email", value)

    # パスワードを入力
    value = getpass("Enter your password: ")
    input_to_field(driver, "password", value)

    # ログインボタンをクリック（ボタンのタイプを指定）
    click_button_by_type(driver, "submit")

    # 例：ログイン後のページが読み込まれるのを待機（特定の要素を待機）
    wait_id = input("Enter the ID of the element you want to wait for: ")
    wait_for_element(driver, By.ID, wait_id)

    # タイトルを検証
    expected_title = input("Enter the expected title: ")
    actual_title = driver.title
    assert actual_title == expected_title, f"Title does not match. Expected: {expected_title}, Got: {actual_title}"

    # 全体のスクリーンショットを撮影
    save_screenshot(driver, full_page=True)
