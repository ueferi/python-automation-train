import openpyxl as excel

book = excel.load_workbook("uriage.xlsx")
sheet = book.active

# A3からf9/列番号を得る
cell = sheet["C2"]
(row, col) = (cell.row, cell.column)
print(f"C2={row},{col}")

# 行番号/列番号からセル名を得る
cell = sheet.cell(row=2, column=3)
cdt = cell.coordinate
print(f"(2,3)={cdt}")
