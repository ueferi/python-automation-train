import openpyxl as xl

book = xl.Workbook()
sheet = book.active


# セルに値とフォーマットを与える関数を定義
def set_cell(cname, value, fmt):
    c = sheet[cname]
    c.value = value
    c.number_format = fmt


# 3桁ごとにカンマ区切りを指定
digit3_fmt = "#,##0"
sheet["A1"] = digit3_fmt
set_cell("B1", 12345, digit3_fmt)
set_cell("C1", 123456789, digit3_fmt)

# 通貨形式を指定
currency_fmt = '"¥"#,##0;"¥"\\-#,##0'
sheet["A2"] = currency_fmt
# 正数(0以上の数)を指定
set_cell("B2", 12345, currency_fmt)
# 負数(0以下の数)を指定
set_cell("C2", -12345, currency_fmt)

# 数値のマイナス値を△で表し、赤色にする
num_fmt = '#,##0;[red]"△ "#,##0'
sheet["A3"] = num_fmt
set_cell("B3", 12345, num_fmt)
set_cell("C3", -12345, num_fmt)

# 保存
book.save("number_format2.xlsx")
