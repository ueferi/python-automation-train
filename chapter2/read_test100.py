import openpyxl as excel

book = excel.load_workbook("test100.xlsx")
sheet = book.active

# H2セルを直接指定する場合
print(sheet["H2"].value)
# 行番号と列番号を指定する場合
cell = sheet.cell(row=2, column=8)

print(cell.value)
