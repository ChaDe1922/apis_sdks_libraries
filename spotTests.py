import requests
import spotipy
import pandas as pd
import json
from pandas.io.json import json_normalize
from spotipy.oauth2 import SpotifyClientCredentials

#GET AUTHENTICATION SET UP FOR SPOTIFY
#define my client id & client secret key
CLIENT_ID = '744aee4ee39a4b6787e645452d1d36b4'
CLIENT_SECRET = '7b72ec76041d4818b061e91ce613d780'

#authenticate myself to use Spotify API through an authorization URL
AUTH_URL = 'https://accounts.spotify.com/api/token'

client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
##SEND A POST REQUEST TO TEST API
#POST request authentication with my credentials
auth_response = requests.post(AUTH_URL, {'grant_type': 'client_credentials',
                                        'client_id': CLIENT_ID,
                                         'client_secret': CLIENT_SECRET,
                                        })

#Convert response to JSON
auth_response_data = auth_response.json()

#Pull access token from response
access_token = auth_response_data['access_token']

#print the response & status code of my POST authentication request
print(auth_response_data)
print("Auth Request Status Code: " + str(auth_response.status_code))

#_____________________________________________________________________#
##ADD A GET REQUEST
#Create authorization headers
headers = {
    'Authorization':'Bearer {token}'.format(token = access_token)
}

#variables
# BASE_URL = 'https://api.spotify.com/v1/'
playlist_id = '37i9dQZF1DX9oh43oAzkyx'
results = sp.playlist(playlist_id)

#print(results)

#_____________________________________________________________________#
##PARSE THE JSON SO THE PROGRAM PRINTS SOMETHING USEFUL
ids=[]

for item in results['tracks']['items']:
        track = item['track']['id']
        ids.append(track)
        
song_meta={'id':[],'album':[], 'name':[], 
           'artist':[],'explicit':[],'popularity':[]}

for song_id in ids:
    # get song's meta data
    meta = sp.track(song_id)
    
    # song id
    song_meta['id'].append(song_id)

    # album name
    album=meta['album']['name']
    song_meta['album']+=[album]

    # song name
    song=meta['name']
    song_meta['name']+=[song]
    
    # artists name
    s = ', '
    artist=s.join([singer_name['name'] for singer_name in meta['artists']])
    song_meta['artist']+=[artist]
    
    # explicit: lyrics could be considered offensive or unsuitable for children
    explicit=meta['explicit']
    song_meta['explicit'].append(explicit)
    
    # song popularity
    popularity=meta['popularity']
    song_meta['popularity'].append(popularity)

song_meta_df=pd.DataFrame.from_dict(song_meta)

# check the song feature
features = sp.audio_features(song_meta['id'])
# change dictionary to dataframe
features_df=pd.DataFrame.from_dict(features)

# convert milliseconds to mins
# duration_ms: The duration of the track in milliseconds.
# 1 minute = 60 seconds = 60 × 1000 milliseconds = 60,000 ms
features_df['duration_ms']=features_df['duration_ms']/60000

# combine two dataframe
final_df=song_meta_df.merge(features_df)

print(final_df)

