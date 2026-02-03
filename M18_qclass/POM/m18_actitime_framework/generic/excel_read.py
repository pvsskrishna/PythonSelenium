from xlrd import *

def read_data():
    d = {}
    wb = open_workbook("C:\\Users\\Hp\\PycharmProjects\\m18_actitime_framework\\excel_files\\data.xlsx")
    sh = wb.sheet_by_name("Sheet1")
    key = sh.row_values(0)
    values = sh.row_values(1)
    for header, values in zip(key,values):
        d[header] = values
    return d




