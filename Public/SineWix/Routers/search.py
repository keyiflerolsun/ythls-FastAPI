# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from .      import sinewix_router, sinewix_global_message
from Core   import Request, kekik_cache, HTTPException
from ..Libs import SineWixDB

@sinewix_router.get("/search/{metin}")
@kekik_cache(ttl=6 * 60 * 60, is_fastapi=True)
async def search(request: Request, metin: str):
    try:
        sinewixdb = SineWixDB()

        veri    = await sinewixdb.search(metin)
        veriler = [*veri["animes"], *veri["movies"], *veri["series"]]

        return {**sinewix_global_message, "search": veriler}
    except Exception as hata:
        raise HTTPException(status_code=410, detail=f"{type(hata).__name__} » {hata}") from hata