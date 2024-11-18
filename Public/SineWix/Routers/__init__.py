# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from fastapi  import APIRouter
from Core     import cache
from Settings import CACHE_TIME

sinewix_router         = APIRouter()
sinewix_global_message = {
    "attention"  : "please use our original app : https://www.sinewix.com/",
    "using_in"    : "https://github.com/keyiflerolsun/Kekik-cloudstream",
    "source_code" : "https://github.com/keyiflerolsun/ythls-FastAPI"
}

@sinewix_router.get("")
@cache(expire=CACHE_TIME)
async def get_sinewix_router():
    return sinewix_global_message

from .movies import *
from .series import *
from .animes import *
from .search import *