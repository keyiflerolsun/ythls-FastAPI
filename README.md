# ythls-FastAPI

[![Size](https://img.shields.io/github/repo-size/keyiflerolsun/ythls-FastAPI?logo=git&logoColor=white&label=Size)](#)
[![Views](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/keyiflerolsun/ythls-FastAPI&title=Views)](#)
<a href="https://KekikAkademi.org/Kahve" target="_blank"><img src="https://img.shields.io/badge/☕️-Buy Me a Coffe-ffdd00" title="☕️ Buy Me a Coffe" style="padding-left:5px;"></a>

*Creates a permanent link for the live feed (HLS/m3u8) of a Youtube channel or video*

[![ForTheBadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](https://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/keyiflerolsun/)

## 📄 Description

**ythls-FastAPI** is a FastAPI application that retrieves HLS URLs and JSON data for YouTube videos and channels. The application provides data in both HLS and JSON formats using specific YouTube video and channel IDs.

## 📋 Features

- Retrieve HLS URLs for YouTube videos.
- Retrieve live stream HLS URLs for YouTube channels.
- Retrieve JSON data for YouTube videos.
- Retrieve live stream JSON data for YouTube channels.
- Log requests and store IP details.
- Fast and secure data retrieval.

## 📖 API Endpoints

| Method | Endpoint                                                      | Description                                                                                |
|--------|---------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| `GET`  | **https://ythls.kekikakademi.org/youtube**                    | _Provides information about the API and lists available endpoints._                        |
| `GET`  | **https://ythls.kekikakademi.org/youtube/channel/{id}.m3u8**  | _Get the HLS URL for a YouTube channel live stream. Replace `{id}` with the channel ID._   |
| `GET`  | **https://ythls.kekikakademi.org/youtube/video/{id}.m3u8**    | _Get the HLS URL for a YouTube video. Replace `{id}` with the video ID._                   |
| `GET`  | **https://ythls.kekikakademi.org/youtube/channel/{id}.json**  | _Get the JSON data for a YouTube channel live stream. Replace `{id}` with the channel ID._ |
| `GET`  | **https://ythls.kekikakademi.org/youtube/video/{id}.json**    | _Get the JSON data for a YouTube video. Replace `{id}` with the video ID._                 |

## 🌐 License and Copyright

* *Copyright (C) 2024 by* [keyiflerolsun](https://github.com/keyiflerolsun) ❤️️
* *Licensed under the* [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/keyiflerolsun/ythls-FastAPI/blob/master/LICENSE).

## ♻️ Contact

*Feel free to contact me on* **Telegram:** [@keyiflerolsun](https://t.me/KekikKahve)

## 💸 Donate

**[☕️ Buy Me a Coffe](https://KekikAkademi.org/Kahve)**

***

> *Written for* **[@KekikAkademi](https://t.me/KekikAkademi)**