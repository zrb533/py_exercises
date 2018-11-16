from common.common import *

excel_path = '/Users/zhanglinquan/PycharmProjects/py_exercises/data/excel_api/login.xlsx'
pe = ParseExcel(excel_path)
sheet1 = pe.set_sheet_by_name("goods_select")
sheet2 = pe.set_sheet_by_name("goods_detail")
print(sheet1)
print(sheet2)

print(sheet1.max_row)
print(sheet2.max_row)
print(sheet1.max_row)
print(sheet2.max_row)
print(sheet1.max_column)
print(sheet2.max_column)
print(sheet1.max_column)
print(sheet2.max_column)