import asyncio
import datetime
from utils import string_of_date
from youtube_util import async_download_mp3, download_mp3, get_video_url
from spotify_util import songs_in_playlist

spotify_playlist = 'https://open.spotify.com/playlist/60eRAVl8vaaKm9cZzsoZfx'

async def main(spotify_playlist: str) -> None:
    start_time = datetime.datetime.now()
    print(f"Starting at : {string_of_date(start_time)}")

    songs_and_artists = songs_in_playlist(spotify_playlist, limit=75)
    url_and_filenames = []
    for song_and_artist in songs_and_artists:
        url = get_video_url(song_and_artist)
        url_and_filenames.append((url, song_and_artist))

    print(f"Identified {len(url_and_filenames)} songs to download")
    
    await asyncio.gather(
        *[async_download_mp3(url, filename) for (url, filename) in url_and_filenames]
    )

    print("Downloaded all songs")
    
    end_time = datetime.datetime.now()
    print(f"Ending at : {string_of_date(end_time)}")
    print("--- %s seconds elapsed ---" % (end_time - start_time))
    




asyncio.run(main(spotify_playlist))

