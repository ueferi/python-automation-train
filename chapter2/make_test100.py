import openpyxl as excel

# 新規ワークブックを作る
book = excel.Workbook()
# アクティブなワークシートを得る
sheet = book.active

# 連続でセルに値を設定する
for y in range(1, 101):
    for x in range(1, 101):
        # セルを取得
        cell = sheet.cell(row=y, column=x)
        cell.value = cell.coordinate  # coordinateプロパティでセル名を取得

# ファイルを保存
book.save("test100.xlsx")
