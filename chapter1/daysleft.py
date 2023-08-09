from datetime import datetime

# 予定日を指定
yoteibi = datetime(2025, 4, 13)  # 大阪万博の開催日
# 基準となる日付(今日)を指定
now = datetime.now()
# 日付計算
delta = yoteibi - now
# 結果を表示
print(f"あと{delta.days+1}日です")
