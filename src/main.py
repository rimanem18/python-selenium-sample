import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# .env ファイルの内容を読み込む
load_dotenv()

chrome_path = "/usr/bin/google-chrome-stable"
chrome_driver_path = "/usr/bin/chromedriver"

print(f"Chrome path: {chrome_path}")
print(f"ChromeDriver path: {chrome_driver_path}")

options = webdriver.ChromeOptions()
options.binary_location = chrome_path
options.add_argument('--headless')  # ヘッドレスモード（ブラウザを表示しない）
options.add_argument('--no-sandbox') # 制約の多い環境で動作させる
options.add_argument('--disable-dev-shm-usage') # メモリ不足の問題を回避
options.add_argument('--remote-debugging-port=9222')  # デバッグ用のポートを指定

try:
    service = ChromeService(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://example.com")
    print("Title:", driver.title)
    driver.quit()

except Exception as e:
    print(f"Exception: {e}")
