# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from .      import sinewix_router, sinewix_global_message
from Core   import cache, HTTPException
from ..Libs import SineWixDB

@sinewix_router.get("/serie/{series_id}")
@cache(expire=6 * 60 * 60)
async def get_serie(series_id: str):
    try:
        sinewixdb = SineWixDB()

        veri = await sinewixdb.get_series_details(int(series_id))

        return {**sinewix_global_message, **veri}
    except Exception as hata:
        raise HTTPException(status_code=410, detail=f"{type(hata).__name__} » {hata}") from hata

@sinewix_router.get("/series/{sayfa}")
@cache(expire=6 * 60 * 60)
async def get_series(sayfa: str):
    try:
        sinewixdb = SineWixDB()

        veri = await sinewixdb.get_series_page(int(sayfa))

        return {**sinewix_global_message, "data": veri}
    except Exception as hata:
        raise HTTPException(status_code=410, detail=f"{type(hata).__name__} » {hata}") from hata

@sinewix_router.get("/series/{genre_id}/{sayfa}")
@cache(expire=6 * 60 * 60)
async def get_series_genre(genre_id:str, sayfa: str):
    try:
        sinewixdb = SineWixDB()

        veri = await sinewixdb.get_series_page(int(sayfa), genre_id=int(genre_id))

        return {**sinewix_global_message, "data": veri}
    except Exception as hata:
        raise HTTPException(status_code=410, detail=f"{type(hata).__name__} » {hata}") from hata