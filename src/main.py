from utils import click_button_by_type, init_driver, input_to_field, click_button_by_text, save_screenshot, wait_for_element
from getpass import getpass
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    url = input("Enter the URL of the page you want to scrape: ")
    driver = init_driver()
    driver.get(url)

    # ユーザー名を入力
    # value = input("Enter your username: ")
    # input_to_field(driver, "username", value)
    value = input("Enter your email: ")
    input_to_field(driver, "email", value)

    # パスワードを入力
    value = getpass("Enter your password: ")
    input_to_field(driver, "password", value)

    # ログインボタンをクリック（ボタンの表示タイプを指定）
    click_button_by_type(driver, "submit")

    # 例：ログイン後のページが読み込まれるのを待機（特定の要素を待機）
    wait_id = input("Enter the ID of the element you want to wait for: ")
    wait_for_element(driver, By.ID, wait_id)

    # 全体のスクリーンショットを撮影
    save_screenshot(driver, full_page=True)

    # 最後にブラウザを閉じる
    driver.quit()
