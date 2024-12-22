# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from .     import cnbce_router
from Core  import RedirectResponse, HTTPException
from httpx import AsyncClient, Timeout

@cnbce_router.get("/stream.m3u8")
async def get_cnbce():
    oturum   = AsyncClient(timeout=Timeout(10, connect=10, read=5*60, write=10))
    oturum.headers.update({"Origin": "https://www.cnbce.com"})

    try:
        stream_url = await oturum.post("https://www.cnbce.com/api/live-stream/source")
        stream_url = stream_url.json()["source"]
    except Exception as hata:
        raise HTTPException(status_code=410, detail=f"Stream bulunamadı: {hata}") from hata

    return RedirectResponse(stream_url)