# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from httpx     import AsyncClient, Timeout
from aiocached import cached
from Settings  import CACHE_TIME

@cached(ttl=CACHE_TIME)
async def ip_log(hedef_ip:str) -> dict[str, str]:
    oturum = AsyncClient(
        headers = {
            "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        },
        timeout = Timeout(10, connect=10, read=5*60, write=10)
    )

    istek = await oturum.get(f"http://ip-api.com/json/{hedef_ip}")
    veri  = istek.json()

    if veri["status"] != "fail":
        return {
            "ulke"   : veri["country"] or "",
            "il"     : veri["regionName"] or "",
            "ilce"   : veri["city"] or "",
            "isp"    : veri["isp"] or "",
            "sirket" : veri["org"] or "",
            "host"   : veri["as"] or ""
        }
    else:
        return {"hata": "Veri Bulunamadı.."}