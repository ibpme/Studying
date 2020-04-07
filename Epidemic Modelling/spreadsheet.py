import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint



scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/ibpra/Documents/API/client_secret.json', scope)
client = gspread.authorize(creds)
sheet_url="https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/edit"
statisitik_harian = client.open_by_url(sheet_url).worksheet("Statistik Harian")
