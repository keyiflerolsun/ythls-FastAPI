# ythls-FastAPI

[![Boyut](https://img.shields.io/github/repo-size/keyiflerolsun/ythls-FastAPI?logo=git&logoColor=white&label=Boyut)](#)
[![Görüntülenme](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/keyiflerolsun/ythls-FastAPI&title=Görüntülenme)](#)
<a href="https://KekikAkademi.org/Kahve" target="_blank"><img src="https://img.shields.io/badge/☕️-Kahve Ismarla-ffdd00" title="☕️ Kahve Ismarla" style="padding-left:5px;"></a>

*Bir YouTube kanalının veya videosunun canlı yayın (HLS/m3u8) için kalıcı bir bağlantı oluşturur*

[![ForTheBadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](https://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/keyiflerolsun/)

## 📄 Açıklama

**ythls-FastAPI**, YouTube videoları ve kanalları için HLS URL'lerini ve JSON verilerini elde etmenizi sağlayan bir FastAPI uygulamasıdır. Uygulama, belirli YouTube video ve kanal ID'lerini kullanarak HLS ve JSON formatında veri sağlar.

## 📋 Özellikler

- YouTube videolarının HLS URL'lerini alabilirsiniz.
- YouTube kanallarının canlı yayın HLS URL'lerini alabilirsiniz.
- YouTube videolarının JSON verilerini alabilirsiniz.
- YouTube kanallarının canlı yayın JSON verilerini alabilirsiniz.
- İsteklerin loglanması ve IP detaylarının kaydedilmesi.
- Hızlı ve güvenli veri elde etme.

## 📖 API Endpoint'leri

| Yöntem | Endpoint                                                      | Açıklama                                                                                 |
|--------|---------------------------------------------------------------|------------------------------------------------------------------------------------------|
| `GET`  | **https://ythls.kekikakademi.org/youtube**                    | _API hakkında bilgi verir ve kullanılabilir endpointleri listeler._                      |
| `GET`  | **https://ythls.kekikakademi.org/youtube/channel/{id}.m3u8**  | _YouTube kanalının canlı yayın HLS URL'sini alır. `{id}` ile kanal ID'si değiştirilir._  |
| `GET`  | **https://ythls.kekikakademi.org/youtube/video/{id}.m3u8**    | _YouTube videosunun HLS URL'sini alır. `{id}` ile video ID'si değiştirilir._             |
| `GET`  | **https://ythls.kekikakademi.org/youtube/channel/{id}.json**  | _YouTube kanalının canlı yayın JSON verisini alır. `{id}` ile kanal ID'si değiştirilir._ |
| `GET`  | **https://ythls.kekikakademi.org/youtube/video/{id}.json**    | _YouTube videosunun JSON verisini alır. `{id}` ile video ID'si değiştirilir._            |

## 🌐 Telif Hakkı ve Lisans

* *Copyright (C) 2024 by* [keyiflerolsun](https://github.com/keyiflerolsun) ❤️️
* [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/keyiflerolsun/ythls-FastAPI/blob/master/LICENSE) *Koşullarına göre lisanslanmıştır..*

## ♻️ İletişim

*Benimle iletişime geçmek isterseniz, **Telegram**'dan mesaj göndermekten çekinmeyin;* [@keyiflerolsun](https://t.me/KekikKahve)

## 💸 Bağış Yap

**[☕️ Kahve Ismarla](https://KekikAkademi.org/Kahve)**

***

> **[@KekikAkademi](https://t.me/KekikAkademi)** *için yazılmıştır..*