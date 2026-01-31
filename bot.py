import tweepy
import schedule
import time
import random
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# Twitter APIの認証情報
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Tweepyで認証
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# ランダムに並び替える8文字
characters = ['御', '奈', '新', 'ヶ', '万', '出', '機', '内']

def post_tweet():
    """ツイートを投稿する関数"""
    # 8文字をランダムに並び替える
    random.shuffle(characters)
    tweet_text = ''.join(characters)
    
    try:
        api.update_status(tweet_text)
        print(f"ツイート投稿成功: {tweet_text}")
    except Exception as e:
        print(f"エラー: {e}")

# 毎日20時（夜8時）に投稿するようスケジュール設定
schedule.every().day.at("11:00").do(post_tweet)

print("ボットが起動しました。毎日20時にツイートします。")

# スケジュールを常時実行
while True:
    schedule.run_pending()
    time.sleep(60)  # 1分ごとにチェック
