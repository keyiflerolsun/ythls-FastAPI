# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from fastapi  import APIRouter
from Core     import Request, kekik_cache
from Settings import CACHE_TIME

cnbce_router         = APIRouter()
cnbce_global_message = {
    "using_in"    : "https://github.com/keyiflerolsun/Kekik-cloudstream",
    "source_code" : "https://github.com/keyiflerolsun/ythls-FastAPI"
}

@cnbce_router.get("")
@kekik_cache(ttl=CACHE_TIME, is_fastapi=True)
async def get_cnbce_router(request: Request):
    return cnbce_global_message

from .cnbce import *