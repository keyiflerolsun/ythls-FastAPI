# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Settings import AYAR

if AYAR.get("yt-dlp"):
    from .ytdl    import YouTube
else:
    from .YouTube import YouTube

youtube = YouTube()