# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI    import konsol
from .      import oxax_router
from Core   import RedirectResponse, HTTPException
from ..Libs import oxax

@oxax_router.get("/{oxax_slug}.m3u8")
async def get_oxax(oxax_slug: str):
    if not oxax.kanallar:
        oxax.kanallar = await oxax.kanallari_al()
        konsol.log(f"[bold green]OxAx[/] [blue]|[/] [bold yellow2]{len(oxax.kanallar)}[/] [blue]kanal yüklendi...[/]")

    if oxax_slug not in oxax.kanallar:
        raise HTTPException(status_code=410, detail="Channel not found")

    stream_url = await oxax.yayin_ver(f"http://oxax.tv/{oxax_slug}.html")
    if not stream_url:
        raise HTTPException(status_code=410, detail="Stream not found")

    return RedirectResponse(stream_url)