import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import pandas as pd

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/ibpra/Documents/API/client_secret.json', scope)
client = gspread.authorize(creds)
sheet_url="https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/edit"

statistik_harian = client.open_by_url(sheet_url).worksheet("Statistik Harian")

date = statistik_harian.col_values(1)
new_cases = statistik_harian.col_values(2)
total_cases = statistik_harian.col_values(5)
quarantined = statistik_harian.col_values(6)
new_recovered = statistik_harian.col_values(7)
total_recovered = statistik_harian.col_values(8)
new_deaths = statistik_harian.col_values(9)
total_deaths = statistik_harian.col_values(10)
total_tests = statistik_harian.col_values(12)

data = [date[1:],total_cases[1:],total_recovered[1:],total_deaths[1:],quarantined[1:],new_cases[1:],new_recovered[1:],new_deaths[1:]]
tests = total_tests[1:]
time = date[1:len(data[1])+1]

import xlwt
from xlwt import Workbook
import os

os.remove("C://Users/ibpra/Documents/COVID 19/INDONESIA MODELING/data_indo.xls")
wb = Workbook()

sheet1 = wb.add_sheet('Sheet1')

for i in range(1,8):
    for j in range(len(data[i])):
        sheet1.write(j,i, data[i][j])

wb.save(r'/Users/ibpra/Documents/COVID 19/INDONESIA MODELING/%s.xls' % 'data_indo')
