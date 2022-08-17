from typing import Any, List
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))

def songs_in_playlist(playlist_url: str, limit:int = 50) -> List[Any]:
    tracks = spotify.playlist_items(playlist_url,limit=limit,)
    tracks_and_artists = []
    items = tracks["items"]

    for item in items:
        track = item['track']
        track_name = track['name']
        artist_names = [artist['name'] for artist in track['artists']]
        tracks_and_artists.append(f"{track_name} - {' '.join(artist_names)}")
    
    return tracks_and_artists

    