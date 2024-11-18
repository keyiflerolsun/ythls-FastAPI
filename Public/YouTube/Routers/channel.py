# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from .        import youtube_router
from Core     import RedirectResponse, HTTPException, cache
from ..Libs   import youtube
from Settings import CACHE_TIME

@youtube_router.get("/channel/{id}.m3u8")
async def get_channel_hls(id: str):
    yt_data    = await youtube.kanal2data(id)
    stream_url = yt_data.get("streamUrl")
    if not stream_url:
        raise HTTPException(status_code=410, detail="HLS URL not found")

    return RedirectResponse(stream_url)

@youtube_router.get("/channel/{id}.json")
@cache(expire=CACHE_TIME)
async def get_channel_json(id: str):
    yt_data = await youtube.kanal2data(id)
    if not yt_data:
        raise HTTPException(status_code=410, detail="Channel not found")

    return yt_data