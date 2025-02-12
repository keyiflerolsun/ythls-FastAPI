# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI      import konsol
from httpx    import AsyncClient, Timeout
from parsel   import Selector
from re       import findall
from Core     import kekik_cache
from Settings import CACHE_TIME

class YouTube:
    def __init__(self):
        self.oturum = AsyncClient(
            headers = {
                "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            },
            timeout = Timeout(10, connect=10, read=5*60, write=10)
        )

    @kekik_cache(ttl=CACHE_TIME)
    async def __data(self, kaynak_kod: str) -> dict:
        secici = Selector(kaynak_kod)
        baslik = secici.xpath("normalize-space(//title)").get().rstrip("- YouTube").strip()
        if not baslik:
            return {}

        if id_regex := findall(r'"liveStreamabilityRenderer":{"videoId":"([^"]+)"', kaynak_kod):
            video_id = id_regex[0]
        else:
            try:
                video_id = secici.xpath("//link[@rel='canonical']/@href").get().split("v=")[1]
            except IndexError:
                return {}

        if author_regex := findall(r'"pageOwnerDetails":{"name":"([^"]+)"', kaynak_kod):
            author_name = author_regex[0]
        else:
            author_name = secici.xpath("//link[@itemprop='name']/@content").get()

        if m3u8_regex := findall(r'(?<="hlsManifestUrl":").*\.m3u8', kaynak_kod):
            m3u8_url = m3u8_regex[0]
        else:
            m3u8_url = None

        konsol.print(f"\n[yellow]{author_name} | {baslik}")

        try:
            author_logo = findall(r'channelAvatar":{"thumbnails":\[{"url":"(https://[^"]+)"', kaynak_kod)[0]
        except IndexError:
            author_logo = None

        return {
            "authorName" : author_name,
            "authorLogo" : author_logo,
            "streamName" : baslik,
            "streamThumb": f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg",
            "streamUrl"  : m3u8_url
        }

    @kekik_cache(ttl=CACHE_TIME)
    async def video2data(self, id: str) -> dict:
        istek = await self.oturum.get(f"https://www.youtube.com/watch?v={id}", follow_redirects=True)

        return await self.__data(istek.text) if istek.status_code == 200 else {}

    @kekik_cache(ttl=CACHE_TIME)
    async def kanal2data(self, id: str) -> dict:
        istek = await self.oturum.get(f"https://www.youtube.com/channel/{id}/live", follow_redirects=True)

        return await self.__data(istek.text) if istek.status_code == 200 else {}