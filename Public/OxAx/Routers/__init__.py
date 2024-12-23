# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from fastapi  import APIRouter
from Core     import cache
from Settings import CACHE_TIME

oxax_router         = APIRouter()
oxax_global_message = {
    "using_in"    : "https://github.com/keyiflerolsun/Kekik-cloudstream",
    "source_code" : "https://github.com/keyiflerolsun/ythls-FastAPI"
}

@oxax_router.get("")
@cache(expire=CACHE_TIME)
async def get_oxax_router():
    return oxax_global_message

from .cs3   import *
from .local import *