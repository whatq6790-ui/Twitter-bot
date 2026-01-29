import sys
import os
import random
import time
from datetime import datetime

# Python 3.13でimghdrが削除されたため、互換性を保つ
if sys.version_info >= (3, 13):
    from unittest.mock import MagicMock
    sys.modules['imghdr'] = MagicMock()

import tweepy
import schedule

# 環境変数からAPIキーを読み込む
api_key = os.environ.get('TWITTER_API_KEY')
api_secret = os.environ.get('TWITTER_API_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

# Tweepyのクライアントを初期化
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# 8文字の定義
characters = ['御', '奈', '新', 'ヶ', '万', '出', '機', '内']

def tweet_random_characters():
    """ランダムに並び替えた8文字をツイートする"""
    # 文字をランダムに並び替える
    shuffled = characters.copy()
    random.shuffle(shuffled)
    tweet_text = ''.join(shuffled)
    
    try:
        # ツイートを投稿
        response = client.create_tweet(text=tweet_text)
        print(f"ツイート成功: {tweet_text}")
        print(f"時刻: {datetime.now()}")
    except Exception as e:
        print(f"エラー: {e}")

# 毎日夜8時(20時)に実行するようスケジュール設定
schedule.every().day.at("20:00").do(tweet_random_characters)

# スケジューラーを実行
if __name__ == "__main__":
    print("ボットが起動しました...")
    while True:
        schedule.run_pending()
        time.sleep(60)  # 1分ごとにチェック
