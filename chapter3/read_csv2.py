import csv, pprint

# ファイルを開いてreaderを得る
with open("items2.csv", encoding="sjis") as f:
    reader = csv.reader(f)
    # ヘッダ行をスキップ
    head = next(reader)
    # 1行ずつ調べる
    total = 0
    for row in reader:
        # CSVの1行を変数に分ける
        name, price, cnt, subtotal = row
        print(name, price, cnt, subtotal)
        total += int(subtotal)
    # 合計を表示
    print("合計:", total, "円")
