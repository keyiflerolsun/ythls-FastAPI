# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI      import konsol
from yt_dlp   import YoutubeDL
from Core     import kekik_cache
from Settings import CACHE_TIME

class YouTube:
    def __init__(self):
        self.ydl_opts = {
            "quiet"       : True,
            "no_warnings" : True,
            "format"      : "best",
            "cookiefile"  : "cookies.txt"
        }

    @kekik_cache(ttl=CACHE_TIME)
    async def __data(self, video_id: str) -> dict:
        with YoutubeDL(self.ydl_opts) as ydl:
            try:
                info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
            except Exception:
                return {}

        baslik      = info.get("title", "").rstrip("- YouTube").strip()
        author_name = info.get("uploader", None)
        m3u8_url    = info.get("url", None)

        konsol.print(f"\n[yellow]{author_name} | {baslik}")

        return {
            "authorName"  : author_name,
            "streamName"  : baslik,
            "streamThumb" : f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg",
            "streamUrl"   : m3u8_url
        }

    @kekik_cache(ttl=CACHE_TIME)
    async def video2data(self, id: str) -> dict:
        return await self.__data(id)

    @kekik_cache(ttl=CACHE_TIME)
    async def kanal2data(self, channel_id: str) -> dict:
        with YoutubeDL(self.ydl_opts) as ydl:
            try:
                info = ydl.extract_info(f"https://www.youtube.com/channel/{channel_id}/live", download=False)
            except Exception:
                return {}

        live_video_id = info.get("id", None)

        return await self.__data(live_video_id) if live_video_id else {}