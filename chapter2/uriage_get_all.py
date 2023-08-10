import openpyxl as excel

book = excel.load_workbook("uriage.xlsx", data_only=True)  # data_onlyで計算済の値を持ってくる
sheet = book.active

# A3からF9のセルを取り出す
rows = sheet["A3":"F9"]
for row in rows:
    # セルの値をリストとして得る
    values = [cell.value for cell in row]
    # リストを表示する
    print(values)
