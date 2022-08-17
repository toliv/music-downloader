# music-downloader
A simple script to find and download music from a Spotify playlist by searching on Youtube and converting to audio.

# Setup

1. Install dependencies via `pipenv sync --dev`
2. Set up your `.env` file. You need to set up your [developer access](https://developer.spotify.com/dashboard/) to Spotify. Then set up two variables in your `.env` file : `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET`

# Usage
Replace your playlist link in the value of the `spotify_playlist` variable in `main.py` and run. 
