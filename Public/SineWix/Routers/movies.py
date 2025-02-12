# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from .      import sinewix_router, sinewix_global_message
from Core   import Request, kekik_cache, HTTPException
from ..Libs import SineWixDB

@sinewix_router.get("/movie/{movie_id}")
@kekik_cache(ttl=6 * 60 * 60, is_fastapi=True)
async def get_movie(request: Request, movie_id: str):
    try:
        sinewixdb = SineWixDB()

        veri = await sinewixdb.get_movie_details(int(movie_id))

        return {**sinewix_global_message, **veri}
    except Exception as hata:
        raise HTTPException(status_code=410, detail=f"{type(hata).__name__} » {hata}") from hata

@sinewix_router.get("/movies/{sayfa}")
@kekik_cache(ttl=6 * 60 * 60, is_fastapi=True)
async def get_movies(request: Request, sayfa: str):
    try:
        sinewixdb = SineWixDB()

        veri = await sinewixdb.get_movie_page(int(sayfa))

        return {**sinewix_global_message, "data": veri}
    except Exception as hata:
        raise HTTPException(status_code=410, detail=f"{type(hata).__name__} » {hata}") from hata

@sinewix_router.get("/movies/{genre_id}/{sayfa}")
@kekik_cache(ttl=6 * 60 * 60, is_fastapi=True)
async def get_movies_genre(request: Request, genre_id:str, sayfa: str):
    try:
        sinewixdb = SineWixDB()

        veri = await sinewixdb.get_movie_page(int(sayfa), genre_id=int(genre_id))

        return {**sinewix_global_message, "data": veri}
    except Exception as hata:
        raise HTTPException(status_code=410, detail=f"{type(hata).__name__} » {hata}") from hata