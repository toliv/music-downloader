from __future__ import unicode_literals
from datetime import datetime
from typing import Optional
from utils import string_of_date
import youtube_dl
from youtubesearchpython import VideosSearch


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d["status"] == "finished":
        print("Done downloading, now converting ...")


defaul_ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        }
    ],
    "logger": MyLogger(),
    "progress_hooks": [my_hook],
}


def download_mp3(url: str, filename: Optional[str]=None) -> None:
    print(f"{string_of_date(datetime.now())} : Beginning download for {url} : {filename}....")
    opts = defaul_ydl_opts.copy()
    if filename:
        opts["outtmpl"] = filename + "."
    with youtube_dl.YoutubeDL(opts) as ydl:
        ydl.download([url])
    print(f"{string_of_date(datetime.now())}: Completed download for {url} : {filename}")

async def async_download_mp3(url: str, filename: Optional[str]=None) -> None:
    download_mp3(url, filename)


def get_video_url(title_name: str, limit: int=1) -> str:
    videoSearch = VideosSearch(title_name, limit=limit)
    videosResult = videoSearch.result()
    return videosResult['result'][0]['link']
