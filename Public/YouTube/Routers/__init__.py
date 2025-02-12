# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from fastapi  import APIRouter
from Core     import Request, kekik_cache
from Settings import CACHE_TIME

youtube_router         = APIRouter()
youtube_global_message = {
    "source_code" : "https://github.com/keyiflerolsun/ythls-FastAPI",
    "message"     : "Welcome to the YTHLS API!",
    "endpoints"   : {
        "/youtube/channel/{id}.m3u8" : "Get the HLS URL for a YouTube channel live stream. Replace {id} with the channel ID.",
        "/youtube/video/{id}.m3u8"   : "Get the HLS URL for a YouTube video. Replace {id} with the video ID.",
        "/youtube/channel/{id}.json" : "Get the JSON data for a YouTube channel live stream. Replace {id} with the channel ID.",
        "/youtube/video/{id}.json"   : "Get the JSON data for a YouTube video. Replace {id} with the video ID."
    }
}

@youtube_router.get("")
@kekik_cache(ttl=CACHE_TIME, is_fastapi=True)
async def get_youtube_router(request: Request):
    return youtube_global_message

from .channel import *
from .video   import *