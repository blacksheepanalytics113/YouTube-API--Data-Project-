from googleapiclient.discovery import build
import pandas as pd
import matplotlib 
import googleapiclient.errors
from pprint import pprint

api_key = 'AIzaSyAdr7OwNPGBHWZG3poiCtAEonA-maJ1s1A'
channel_id = 'UCcbjsobn9lYHUM5S7qQgU5A'



youtube = build('youtube','v3',developerKey=api_key)

def get_channel_stats(youtube,channel_id):
    All_Data = []
    request = youtube.channels().list(
        part = 'snippet,contentDetails,statistics',id = channel_id
    )
    response = request.execute()
    Data = dict(Channel_Name= response['items'][0]['snippet']['title'],
                Published_Data= response['items'][0]['snippet']['publishedAt'],
                Subscribers = response['items'][0]['statistics']['subscriberCount'],
                Views = response['items'][0]['statistics']['viewCount'])
    return Data
channel_Statistics = get_channel_stats(youtube,channel_id)
print(channel_Statistics)


