from utils import click_button_by_type, init_driver, input_to_field, click_button_by_text, save_screenshot, wait_for_element
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    url = input("Enter the URL of the page you want to scrape: ")
    driver = init_driver()
    driver.get(url)

    # ユーザー名を入力
    value = input("Enter your username: ")
    input_to_field(driver, "username", value)

    # パスワードを入力
    value = input("Enter your password: ")
    input_to_field(driver, "password", value)

    # ログインボタンをクリック（ボタンの表示テキストを指定）
    click_button_by_type(driver, "submit")

    # 例：ログイン後のページが読み込まれるのを待機（特定の要素を待機）
    wait_id = input("Enter the ID of the element you want to wait for: ")
    wait_for_element(driver, By.ID, wait_id)

    # その他の操作...
    save_screenshot(driver)

    # 最後にブラウザを閉じる
    driver.quit()
