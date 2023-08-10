import openpyxl as excel

book = excel.load_workbook("uriage.xlsx", data_only=True)  # data_onlyで計算済の値を持ってくる
sheet = book.active

# A3からF999(データの適当な範囲)のセルを取り出す
rows = sheet["A3":"F999"]
for row in rows:
    # セルの値をリストとして得る
    values = [cell.value for cell in row]
    # 空白セルであれば読み取りを終わる
    if values[0] is None:
        break
    # リストを表示する
    print(values)
