# Requestsモジュールを取り込む
import requests

# 現在時刻を提供しているサーバーにアクセス
url = "https://api.aoikujira.com/time/get/php"
result = requests.get(url)
# アクセス結果を表示
print(f"ok={result.ok}")
# アクセスに成功すれば取得したテキストを表示
if result.ok:
    print(f"text={result.text}")
# ステータスコードを表示
print(f"status_code={result.status_code}")
