# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from fastapi             import FastAPI, Request, Response, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses   import JSONResponse, HTMLResponse, RedirectResponse, PlainTextResponse, FileResponse
from Kekik.cache         import kekik_cache

kekik_FastAPI = FastAPI(
    title       = "Kekik-FastAPI",
    openapi_url = None,
    docs_url    = None,
    redoc_url   = None
)

# ! ----------------------------------------» Routers

from Core.Modules           import _istek, _hata
from Public.Home.Routers    import home_router
from Public.YouTube.Routers import youtube_router
from Public.OxAx.Routers    import oxax_router
from Public.SineWix.Routers import sinewix_router
from Public.CNBCE.Routers   import cnbce_router

kekik_FastAPI.include_router(home_router, prefix="")
kekik_FastAPI.mount("/static/home", StaticFiles(directory="Public/Home/Static"), name="static_home")

kekik_FastAPI.include_router(youtube_router, prefix="/youtube")

kekik_FastAPI.include_router(oxax_router,    prefix="/oxax")

kekik_FastAPI.include_router(sinewix_router, prefix="/sinewix")

kekik_FastAPI.include_router(cnbce_router, prefix="/cnbce")