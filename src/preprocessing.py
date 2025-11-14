#======================== TwitterのIDから投稿日時を取得する関数 =================
from datetime import datetime, timedelta
# https://qiita.com/haruka_kotani/items/0e2096cbd527015a2d96
twitter_epoch = 1288834974657
unix_epoch = 62135596800000
timestamp_bits = 41
timestamp_shift = 22
timestamp_mask = (1 << timestamp_bits) - 1

def tweetID_2_datetime(tweet_id):
    timestamp = ((tweet_id >> timestamp_shift) & timestamp_mask) + twitter_epoch + unix_epoch
    tweet_datetime = datetime(1, 1, 1) + timedelta(milliseconds=timestamp)
    return tweet_datetime


#======================== テキストから言語を検出する関数 =================
import pandas as pd
from langdetect import detect, DetectorFactory

# 安定した言語検出のためにランダムシードを設定
DetectorFactory.seed = 0
def detect_language(text):
    try:
        return detect(text)
    except:
        return 'unknown'  # 言語検出ができない場合は 'unknown' を返す