# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from .        import oxax_router, oxax_global_message
from Core     import Request, kekik_cache
from ..Libs   import oxax
from Settings import CACHE_TIME

@oxax_router.get("/cs3/porno")
@kekik_cache(ttl=CACHE_TIME, is_fastapi=True)
async def get_porno(request: Request):
    slugs = [slug for slug in await oxax.porno_kanal_listesi() if slug in oxax.detail]

    return {**oxax_global_message, "channels": [{"slug": slug, "detail": oxax.detail[slug]} for slug in slugs]}

@oxax_router.get("/cs3/erotic")
@kekik_cache(ttl=CACHE_TIME, is_fastapi=True)
async def get_erotic(request: Request):
    slugs = [slug for slug in await oxax.erotik_kanal_listesi() if slug in oxax.detail]

    return {**oxax_global_message, "channels": [{"slug": slug, "detail": oxax.detail[slug]} for slug in slugs]}

@oxax_router.get("/cs3/hd")
@kekik_cache(ttl=CACHE_TIME, is_fastapi=True)
async def get_hd(request: Request):
    slugs = [slug for slug in await oxax.hd_kanal_listesi() if slug in oxax.detail]

    return {**oxax_global_message, "channels": [{"slug": slug, "detail": oxax.detail[slug]} for slug in slugs]}

@oxax_router.get("/cs3/detail/{slug}")
@kekik_cache(ttl=CACHE_TIME, is_fastapi=True)
async def get_img(request: Request, slug:str):
    return {**oxax_global_message, **oxax.detail.get(slug)} if oxax.detail.get(slug) else {}

@oxax_router.get("/cs3/search/{text}")
@kekik_cache(ttl=CACHE_TIME, is_fastapi=True)
async def get_img(request: Request, text:str):
    return {
        **oxax_global_message,
        "channels": [
            {"slug": slug, "detail": detail}
                for slug, detail in oxax.detail.items()
                    if text.lower().strip() in detail.get("title").lower()
        ]
    }