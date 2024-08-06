# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Core                 import kekik_FastAPI, Request, RedirectResponse, JSONResponse, FileResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

@kekik_FastAPI.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request:Request, exc):
    return RedirectResponse("/") if exc.status_code != 410 else JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

@kekik_FastAPI.get("/favicon.ico")
def get_favicon():
    return FileResponse("Public/Home/Static/favicon.ico")