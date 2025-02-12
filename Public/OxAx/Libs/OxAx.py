# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from httpx        import AsyncClient, Timeout
from parsel       import Selector
from re           import findall, search
from base64       import b64encode, b64decode
from urllib.parse import quote, unquote
from Core         import kekik_cache
from Settings     import CACHE_TIME

class OxAx:
    def __init__(self):
        self.oturum   = AsyncClient(timeout=Timeout(10, connect=10, read=5*60, write=10))
        self.kanallar = None
        self.detail   = {
            "oh-ah"              : {"title": "ОxАx HD",            "img": "https://i.imgur.com/Ck89ehE.png", "tags": ["HD", "Porno"]},
            "brazzers-tv-europe" : {"title": "Brazzers TV Europe", "img": "https://i.imgur.com/YQrr9bJ.png", "tags": ["Porno"]},
            "brazzers-tv"        : {"title": "Brazzers TV",        "img": "https://i.imgur.com/GigEnAE.png", "tags": ["Porno"]},
            "red-lips"           : {"title": "Red Lips",           "img": "https://i.imgur.com/lfM61ug.png", "tags": ["Porno"]},
            "french_lover"       : {"title": "French Lover",       "img": "https://i.imgur.com/L5S67gF.png", "tags": ["Porno"]},
            "kino-xxx"           : {"title": "KinoXXX",            "img": "https://i.imgur.com/RJxLBmE.png", "tags": ["Porno"]},
            "xy-max-hd"          : {"title": "XY Max HD",          "img": "https://i.imgur.com/MJbFG1z.png", "tags": ["HD", "Porno"]},
            "xy-plus-hd"         : {"title": "XY Plus HD",         "img": "https://i.imgur.com/aguADMz.png", "tags": ["HD", "Porno"]},
            "xy-mix-hd"          : {"title": "XY Mix HD",          "img": "https://i.imgur.com/yp1VBl6.png", "tags": ["HD", "Porno"]},
            "barely-legal"       : {"title": "Barely legal",       "img": "https://i.imgur.com/yNt8FyL.png", "tags": ["Porno"]},
            "playboy-tv"         : {"title": "Playboy TV",         "img": "https://i.imgur.com/OJ3osog.png", "tags": ["Erotic TV"]},
            "vivid-red"          : {"title": "Vivid Red HD",       "img": "https://i.imgur.com/eoExtXF.png", "tags": ["HD", "Porno"]},
            "hot-pleasure"       : {"title": "Exxxotica HD",       "img": "https://i.imgur.com/ViQLY4S.png", "tags": ["HD", "Porno"]},
            "babes-tv"           : {"title": "Babes TV",           "img": "https://i.imgur.com/7ShkmKH.png", "tags": ["HD", "Porno"]},
            "pink-o"             : {"title": "Pink O TV",          "img": "https://i.imgur.com/Nq12KtX.png", "tags": ["Porno"]},
            "eroxxx-hd"          : {"title": "Eroxxx HD",          "img": "https://i.imgur.com/EilmlnN.png", "tags": ["HD", "Porno"]},
            "hustler-hd"         : {"title": "Hustler HD",         "img": "https://i.imgur.com/mofbYfp.png", "tags": ["HD", "Porno"]},
            "private-tv"         : {"title": "Private TV",         "img": "https://i.imgur.com/KsCvoTA.png", "tags": ["HD", "Porno"]},
            "redlight-hd"        : {"title": "Redlight HD",        "img": "https://i.imgur.com/llc5OIj.png", "tags": ["HD", "Porno"]},
            "penthouse-gold"     : {"title": "Penthouse Gold HD",  "img": "https://i.imgur.com/Nchjh70.png", "tags": ["HD", "Porno"]},
            "penthouse-2"        : {"title": "Penthouse Quickies", "img": "https://i.imgur.com/PqhYNMo.png", "tags": ["HD", "Porno"]},
            "blue-hustler"       : {"title": "Blue Hustler",       "img": "https://i.imgur.com/beBJTt4.png", "tags": ["Porno"]},
            "shalun"             : {"title": "Shalun",             "img": "https://i.imgur.com/62dWh8a.png", "tags": ["HD", "Porno"]},
            "dorcel-tv"          : {"title": "Dorcel TV",          "img": "https://i.imgur.com/MvoOgyh.png", "tags": ["HD", "Porno"]},
            "candy"              : {"title": "Candy",              "img": "https://i.imgur.com/om2kK8W.png", "tags": ["Erotic TV", "HD"]},
            "extasyhd"           : {"title": "Extasy HD",          "img": "https://i.imgur.com/o6Oe8Xt.png", "tags": ["HD", "Porno"]},
            "xxl"                : {"title": "XXL",                "img": "https://i.imgur.com/QhSHIY7.png", "tags": ["Porno"]},
            "fap-tv-2"           : {"title": "FAP TV 2",           "img": "https://i.imgur.com/fPmNFiR.png", "tags": ["HD", "Porno"]},
            "fap-tv-3"           : {"title": "FAP TV 3",           "img": "https://i.imgur.com/Wm0oMub.png", "tags": ["HD", "Porno"]},
            "fap-tv-4"           : {"title": "FAP TV 4",           "img": "https://i.imgur.com/F0DaE5j.png", "tags": ["HD", "Porno"]},
            "fap-tv-parody"      : {"title": "FAP TV Parody",      "img": "https://i.imgur.com/b6x2z4s.png", "tags": ["HD", "Porno"]},
            "fap-tv-bbw"         : {"title": "FAP TV BBW",         "img": "https://i.imgur.com/YB5ZK6Y.png", "tags": ["HD", "Porno"]},
            "fap-tv-teens"       : {"title": "FAP TV Teens",       "img": "https://i.imgur.com/qEOXqJQ.png", "tags": ["HD", "Porno"]},
            "fap-tv-lesbian"     : {"title": "FAP TV Lesbian",     "img": "https://i.imgur.com/Oatn5sk.png", "tags": ["HD", "Porno"]},
            "fap-tv-compilation" : {"title": "FAP TV Compilation", "img": "https://i.imgur.com/eJdOcgH.png", "tags": ["HD", "Porno"]},
            "fap-tv-anal"        : {"title": "FAP TV Anal",        "img": "https://i.imgur.com/EqGtDVW.png", "tags": ["HD", "Porno"]}
        }

    async def __base64_encode(self, str):
        return b64encode(quote(str).encode()).decode()

    async def __base64_decode(self, str):
        return unquote(b64decode(str).decode())

    async def __decode_atob(self, base64_str):
        b64_keys = {
            0: "556G3",
            1: "556G3D",
            2: "556G3DQ",
            3: "556G3DQ1",
            4: "556G3DQ1V"
        }

        file_separator = "F"

        cleanb64 = base64_str[2:]
        for i in range(4, -1, -1):
            if b64_keys[i]:
                cleanb64 = cleanb64.replace(file_separator + await self.__base64_encode(b64_keys[i]), "")

        try:
            cleanb64 = await self.__base64_decode(cleanb64)
        except Exception:
            cleanb64 = ""

        return cleanb64

    @kekik_cache(ttl=CACHE_TIME)
    async def yayin_ver(self, link:str) -> str | None:
        istek = await self.oturum.get(link)
        if istek.status_code != 200:
            return None

        kaynak = istek.text

        try:
            kodk     = findall(r'var kodk="(.*?)"', kaynak)[0]
            kos      = findall(r'var kos="(.*?)"', kaynak)[0]
            playerjs = findall(r'new Playerjs\("(.*?)"', kaynak)[0]
        except IndexError:
            return None

        decoded_data = await self.__decode_atob(playerjs)

        v1, v2 = search(r'\{v1\}(.*?)\{v2\}([a-zA-Z0-9]*)', decoded_data).groups()

        yayin_link = f"{kodk}{v1}{kos}{v2}" 

        yayin_test = await self.oturum.get(yayin_link, follow_redirects=True)

        return yayin_link if yayin_test.text else None

    @kekik_cache(ttl=CACHE_TIME)
    async def __spisok_list(self, vse=int) -> list[str]:
        istek  = await self.oturum.get(f"http://oxax.tv/spisok?vse={vse}")
        secici = Selector(istek.text)

        return [
            search(r"/([^/]+)\.html", link.xpath(".//a/@href").get()).group(1)
                for link in secici.xpath("//div[@class='tv_sp']")
        ]

    @kekik_cache(ttl=CACHE_TIME)
    async def hd_kanal_listesi(self) -> list[str]:
        return await self.__spisok_list(2)

    @kekik_cache(ttl=CACHE_TIME)
    async def porno_kanal_listesi(self) -> list[str]:
        return await self.__spisok_list(4)

    @kekik_cache(ttl=CACHE_TIME)
    async def erotik_kanal_listesi(self) -> list[str]:
        return await self.__spisok_list(3)

    @kekik_cache(ttl=CACHE_TIME)
    async def kanallari_al(self) -> list:
        return sorted({*await self.hd_kanal_listesi(), *await self.porno_kanal_listesi(), *await self.erotik_kanal_listesi()})