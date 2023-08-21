# pywin32(win32com)のライブラリを読み込み
import win32com.client as com
import os

# 保存先は絶対パスで指定する必要がある
scr_file = os.path.abspath(__file__)
scr_dir = os.path.dirname(scr_file)
in_file = f"{scr_dir}/date-sample.xlsx"
pdf_file = f"{scr_dir}/date-sample.pdf"

# Excelを起動する
app = com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

# Excelでブックを読み込む
book = app.Workbooks.Open(in_file)

# ブックをPDFでエクスポート
xlTypePDF = 0  # PDFを表す変数
book.ExportAsFixedFormat(xlTypePDF, pdf_file)

# Excelを終了させる
app.Quit()
