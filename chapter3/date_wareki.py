import openpyxl as excel
import datetime

in_file = "date-sample.xlsx"
out_file = "date-wareki.xlsx"
cell_format = '[$-ja-JP]ggge"年"m"月"d"日"'


# メイン処理
def date_wareki(in_file, out_file):
    # Excelブックを開く
    book = excel.load_workbook(in_file)
    # 全シートを確認する
    for sheet in book.worksheets:
        # 全行を確認する
        for row in sheet.iter_rows():
            # 全セルを確認する
            for cell in row:
                check_cell(cell)
    # 保存
    book.save(out_file)


# セルをチェックする
def check_cell(cell):
    # セルが日付型か確認
    if type(cell.value) is datetime.datetime:
        cell.number_format = cell_format


if __name__ == "__main__":
    date_wareki(in_file, out_file)
