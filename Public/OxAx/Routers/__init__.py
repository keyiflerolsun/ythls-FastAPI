# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from fastapi  import APIRouter
from Core     import Request, kekik_cache
from Settings import CACHE_TIME

oxax_router         = APIRouter()
oxax_global_message = {
    "using_in"    : "https://github.com/keyiflerolsun/Kekik-cloudstream",
    "source_code" : "https://github.com/keyiflerolsun/ythls-FastAPI"
}

@oxax_router.get("")
@kekik_cache(ttl=CACHE_TIME, is_fastapi=True)
async def get_oxax_router(request: Request):
    return oxax_global_message

from .cs3   import *
from .local import *