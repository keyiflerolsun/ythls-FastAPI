# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from .      import youtube_router
from Core   import RedirectResponse, HTTPException, cache
from ..Libs import youtube

@youtube_router.get("/video/{id}.m3u8")
async def get_video_hls(id: str):
    yt_data    = await youtube.video2data(id)
    stream_url = yt_data.get("streamUrl")
    if not stream_url:
        raise HTTPException(status_code=410, detail="HLS URL not found")

    return RedirectResponse(stream_url)

@youtube_router.get("/video/{id}.json")
@cache()
async def get_video_json(id: str):
    yt_data = await youtube.video2data(id)
    if not yt_data:
        raise HTTPException(status_code=410, detail="Video not found")

    return yt_data