# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from fastapi  import APIRouter
from Core     import cache
from Settings import CACHE_TIME

cnbce_router         = APIRouter()
cnbce_global_message = {
    "using_in"    : "https://github.com/keyiflerolsun/Kekik-cloudstream",
    "source_code" : "https://github.com/keyiflerolsun/ythls-FastAPI"
}

@cnbce_router.get("")
@cache(expire=CACHE_TIME)
async def get_cnbce_router():
    return cnbce_global_message

from .cnbce import *