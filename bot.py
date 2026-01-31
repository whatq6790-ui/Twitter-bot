import sys

if sys.version_info >= (3, 13):
    from unittest.mock import MagicMock
    sys.modules['imghdr'] = MagicMock()

import os
import random
from datetime import datetime

import dotenv
import tweepy
from flask import Flask

app = Flask(__name__)

dotenv.load_dotenv('/etc/secrets/.env')

api_key = os.environ.get('TWITTER_API_KEY')
api_secret = os.environ.get('TWITTER_API_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

print(f"API Key: {api_key[:10] if api_key else 'NOT SET'}...")
print(f"API Secret: {api_secret[:10] if api_secret else 'NOT SET'}...")
print(f"Access Token: {access_token[:10] if access_token else 'NOT SET'}...")

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

@app.route('/tweet')
def tweet_test():
    shuffled = characters.copy()
    random.shuffle(shuffled)
    tweet_text = ''.join(shuffled)
    
    try:
        response = client.create_tweet(text=tweet_text)
        return f"Tweet posted: {tweet_text}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
```

修正後、「Manual Deploy」をして、Renderが起動したら、ブラウザで以下にアクセスしてください：
```
https://twitter-bot-rynf.onrender.com/tweet
