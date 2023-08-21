import requests
import os, time

# 保存先のフォルダを指定
save_dir = "./image"
# 画像の基本URLを指定
base_url = "https://uta.pw/shodou/img/{0}/{1}.png"


# 一気に画像をダウンロード
def download_all():
    # 画像の保存フォルダを作成
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    # 連続ダウンロード
    for id in range(1, 11):
        download_file(id)
        time.sleep(1)  # サーバに負荷をかけないよう1秒間処理を待機


# idの画像を一枚だけダウンロードする
def download_file(id):
    # 画像のURLと保存先を動的に決定
    url = base_url.format(id % 31, id)
    save_file = save_dir + "/" + str(id) + ".png"
    # URLのリソースを取得
    res = requests.get(url)
    # 戻り値をチェック
    if not res.ok:
        print("失敗:", res.status_code)
        return
    # ファイルに保存
    with open(save_file, "wb") as fp:
        fp.write(res.content)
    print("save:", save_file)


if __name__ == "__main__":
    download_all()
