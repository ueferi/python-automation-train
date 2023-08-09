from datetime import datetime

# 22時就寝、翌朝8時半起床として、あと何時間寝られるか？
# 就寝時間と起床時刻を指定
sleep_t = datetime(2023, 1, 1, 22, 0, 0)
wakeup_t = datetime(2023, 1, 2, 8, 30, 0)
# 時間計算
delta = wakeup_t - sleep_t
print(type(delta))
sec = delta.seconds  # あと何秒か？
hours = sec / (60 * 60)  # 秒数を1時間の秒数で割る(60*60=3600sec)
# 結果を表示
print(f"あと{hours}時間です")
