# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from fastapi             import FastAPI, Request, Response
from Kekik_fastapi_cache import FastAPICache, InMemoryBackend
from contextlib          import asynccontextmanager
from Settings            import CACHE_TIME
from urllib.parse        import urlencode
from hashlib             import md5

def cache_key(
    func,
    namespace: str = "",
    *,
    request: Request = None,
    response: Response = None,
    **kwargs,
) -> str:
    veri = request.state.req_veri
    args = md5(f"{urlencode(veri)}".encode()).hexdigest() if veri else ""

    return f"{request.url.path}?{args}"

@asynccontextmanager
async def lifespan(app: FastAPI):
    FastAPICache.init(InMemoryBackend(), expire=CACHE_TIME, key_builder=cache_key)
    yield