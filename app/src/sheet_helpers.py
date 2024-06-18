import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 認証情報を読み込む
def authenticate(credentials_file):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    return gspread.authorize(credentials)

# データを追加
def append(client, spreadsheet_id, sheet_name, data):
    sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)
    sheet.append_row(data)
