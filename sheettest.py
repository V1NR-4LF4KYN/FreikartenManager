import gspread
from oauth2client.service_account import ServiceAccountCredentials





scope = ['https://www.googleapis.com/auth/documents.readonly', "https://www.spreadsheets.google.com/feeds", "https://www.googleapsis.com/auth/spreadsheets", "https://www.googleapsis.com/auth/drive.file", "https://www.googleapsis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

'''
sheet = client.open("FreikartenManager").sheet1
data = sheet.get_all_records()

print(data)
'''