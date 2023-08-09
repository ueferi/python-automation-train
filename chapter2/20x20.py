import openpyxl as excel

# 新規ワークブックを作る
book = excel.Workbook()
# アクティブなワークシートを得る
sheet = book.active

# 連続でセルに値を設定する
for y in range(1, 21):
    for x in range(1, 21):
        # セルを取得
        cell = sheet.cell(row=y, column=x)
        # 九九の値を設定
        cell.value = x * y

# ファイルを保存
book.save("20x20.xlsx")
