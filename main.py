import base64
import json
from dotenv import load_dotenv
from requests import post, get
import os
import pandas as pd
import numpy as np

load_dotenv()

cliend_id = os.getenv('CLIENT_ID')
cliend_secret = os.getenv('CLIENT_SECRET')

def get_token():
    auth_string = cliend_id + ':' + cliend_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')

    url = "https://accounts.spotify.com/api/token"
    headers = {
    "Authorization": "Basic " + auth_base64,
    "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {'grant_type': 'client_credentials'}
    results = post(url, headers=headers, data = data)
    json_result = json.loads(results.content)
    token = json_result['access_token']
    return token

token = get_token()
# print(token)

def get_auth_header(token):
    return {'Authorization': 'Bearer ' + token}

def search_for_track(token, track):
    url = 'https://api.spotify.com/v1/search'
    headers = get_auth_header(token)
    query = f'?q={track}&type=track&limit=1'

    query_url = url + query
    result = get(query_url, headers=headers)
    # json_results = json.loads(result.content)["tracks"]["items"][0].keys()
    song_id = json.loads(result.content)["tracks"]["items"][0]['id']
    # ["items"][0]['name']
    if(len(song_id) == 0):
        print('No track found')
        return None
    return song_id

song_id = search_for_track(token, "One_Direction_-_Best_Song_Ever")
feature_list = ['acousticness', 'energy', 'instrumentalness', 'key', 'mode', 'tempo', 'time_signature', 'valence']

def extract_features(token, song_id):
    data = []
    url = 'https://api.spotify.com/v1/audio-features'
    headers = get_auth_header(token)
    query = f'/{song_id}'

    query_url = url + query
    result = get(query_url, headers=headers)
    # json_results = json.loads(result.content)["tracks"]["items"][0].keys()
    # features = json.loads(result.content).keys()
    features = json.loads(result.content)
    # ["items"][0]['name']

    if(len(features) == 0):
        print('No track found')
        return None
    for key in feature_list:
        if key in features:
            data.append(features[key])
    return data
# print(extract_features(token, song_id))
final_data = []
def make_datframe():
    folder_path = '/Users/dhruv/Dhruv/ML_KAGGLE/MIXER/music'
    file_list = os.listdir(folder_path)
    mp3_file_names = [file for file in file_list if file.endswith(".mp3")]
    print(len(mp3_file_names))
    # total_duration_seconds = []

    
    for mp3_file in mp3_file_names:
        try:
            song_id = search_for_track(token, mp3_file)
            print(song_id)
            final_data.append(extract_features(token, song_id))
            print()
        except Exception:
            print('NAME NOT IDENTIFIED')
            print()


        print(mp3_file)

make_datframe()
print(final_data)

df = pd.DataFrame(np.array(final_data))
print(df)