# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from .      import sinewix_router, sinewix_global_message
from Core   import Request, kekik_cache, HTTPException
from ..Libs import SineWixDB

@sinewix_router.get("/serie/{series_id}")
@kekik_cache(ttl=6 * 60 * 60, is_fastapi=True)
async def get_serie(request: Request, series_id: str):
    try:
        sinewixdb = SineWixDB()

        veri = await sinewixdb.get_series_details(int(series_id))

        return {**sinewix_global_message, **veri}
    except Exception as hata:
        raise HTTPException(status_code=410, detail=f"{type(hata).__name__} » {hata}") from hata

@sinewix_router.get("/series/{sayfa}")
@kekik_cache(ttl=6 * 60 * 60, is_fastapi=True)
async def get_series(request: Request, sayfa: str):
    try:
        sinewixdb = SineWixDB()

        veri = await sinewixdb.get_series_page(int(sayfa))

        return {**sinewix_global_message, "data": veri}
    except Exception as hata:
        raise HTTPException(status_code=410, detail=f"{type(hata).__name__} » {hata}") from hata

@sinewix_router.get("/series/{genre_id}/{sayfa}")
@kekik_cache(ttl=6 * 60 * 60, is_fastapi=True)
async def get_series_genre(request: Request, genre_id:str, sayfa: str):
    try:
        sinewixdb = SineWixDB()

        veri = await sinewixdb.get_series_page(int(sayfa), genre_id=int(genre_id))

        return {**sinewix_global_message, "data": veri}
    except Exception as hata:
        raise HTTPException(status_code=410, detail=f"{type(hata).__name__} » {hata}") from hata