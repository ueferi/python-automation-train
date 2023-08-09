# 日時関連の命令を使う時に宣言
from datetime import datetime

# 現在時刻を取得
t = datetime.now()
fmt = t.strftime("%Y年%m月%d日 %H時%M分%S秒")  # strftimeメソッドで書式を指定
print(fmt)
