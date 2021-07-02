import requests
import spotipy
import pandas as pd
import json
from pandas.io.json import json_normalize

#GET AUTHENTICATION SET UP FOR SPOTIFY
#define my client id & client secret key
CLIENT_ID = '744aee4ee39a4b6787e645452d1d36b4'
CLIENT_SECRET = '7b72ec76041d4818b061e91ce613d780'

#authenticate myself to use Spotify API through an authorization URL
AUTH_URL = 'https://accounts.spotify.com/api/token'


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
print("Request Status Code: " + str(auth_response.status_code))

