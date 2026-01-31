import sys
import os
import random
import time
from datetime import datetime
from threading import Thread

# Python 3.13でimghdrが削除されたため、互換性を保つ
if sys.version_info >= (3, 13):
    from unittest.mock import MagicMock
    sys.modules['imghdr'] = MagicMock()

import tweepy
import schedule
from flask import Flask

app = Flask(__name__)

api_key = os.environ.get('TWITTER_API_KEY')
api_secret = os.environ.get('TWITTER_API_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

characters = ['御', '奈', '新', 'ヶ', '万', '出', '機', '内']

@app.route('/')
def home():
    return 'Bot is running'

def tweet_random_characters():
    shuffled = characters.copy()
    random.shuffle(shuffled)
    tweet_text = ''.join(shuffled)
    
    try:
        response = client.create_tweet(text=tweet_text)
        print(f"Tweet success: {tweet_text}")
        print(f"Time: {datetime.now()}")
    except Exception as e:
        print(f"Error: {e}")

def run_scheduler():
    schedule.every().day.at("11:00").do(tweet_random_characters)
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    scheduler_thread = Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()
    
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
