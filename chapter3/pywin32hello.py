# pywin32(win32com)のライブラリを読み込み
import win32com.client as com

# Excelを起動する
app = com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

# Excelに新規ワークブックを追加
book = app.Workbooks.Add()
# アクティブなシートを得る
sheet = book.ActiveSheet

# シートに値を書き込む
sheet.Range("B2").Value = "こんにちは"
