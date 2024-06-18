import os
from sheet_helpers import authenticate, append
from selenium_helpers import init_driver, save_screenshot
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    url = input("Enter the URL of the page you want to scrape: ")
    driver = init_driver()
    driver.get(url)

    # 全体のスクリーンショットを撮影
    img_file = save_screenshot(driver, full_page=True)

    # タイトル取得
    page_title = driver.title
    print(page_title)

    # スプレッドシート認証
    credentials_file = os.getenv("CREDENTIALS_FILE")
    client = authenticate(credentials_file)

    # スプレッドシートにデータを追加
    spreadsheet_id = os.getenv("SPREADSHEET_ID")
    sheet_name = input("Enter the name of the sheet you want to append to: ")

    # メッセージを入力
    message = input("Enter a message to append to the sheet: ")
    append(client, spreadsheet_id, sheet_name, [page_title, url, message, img_file])

    # 最後にブラウザを閉じる
    driver.quit()
