# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from .        import oxax_router, oxax_global_message
from Core     import cache
from ..Libs   import oxax
from Settings import CACHE_TIME

@oxax_router.get("/cs3/porno")
@cache(expire=CACHE_TIME)
async def get_porno():
    slugs = [slug for slug in await oxax.porno_kanal_listesi() if slug in oxax.detail]

    return {**oxax_global_message, "channels": [{"slug": slug, "detail": oxax.detail[slug]} for slug in slugs]}

@oxax_router.get("/cs3/erotic")
@cache(expire=CACHE_TIME)
async def get_erotic():
    slugs = [slug for slug in await oxax.erotik_kanal_listesi() if slug in oxax.detail]

    return {**oxax_global_message, "channels": [{"slug": slug, "detail": oxax.detail[slug]} for slug in slugs]}

@oxax_router.get("/cs3/hd")
@cache(expire=CACHE_TIME)
async def get_hd():
    slugs = [slug for slug in await oxax.hd_kanal_listesi() if slug in oxax.detail]

    return {**oxax_global_message, "channels": [{"slug": slug, "detail": oxax.detail[slug]} for slug in slugs]}

@oxax_router.get("/cs3/detail/{slug}")
@cache(expire=CACHE_TIME)
async def get_img(slug:str):
    return {**oxax_global_message, **oxax.detail.get(slug)} if oxax.detail.get(slug) else {}

@oxax_router.get("/cs3/search/{text}")
@cache(expire=CACHE_TIME)
async def get_img(text:str):
    return {
        **oxax_global_message,
        "channels": [
            {"slug": slug, "detail": detail}
                for slug, detail in oxax.detail.items()
                    if text.lower().strip() in detail.get("title").lower()
        ]
    }