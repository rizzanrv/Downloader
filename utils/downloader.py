import yt_dlp
import os
import re
from typing import Literal

async def download_media(url: str, download_dir: str) -> str:
    """
    Загружает медиа с указанного URL и сохраняет в указанную директорию.

    Поддерживаются SoundCloud, YouTube, Instagram Reels и TikTok.
    Для SoundCloud и большинства аудио-ссылок используется формат mp3,
    для видео Reels и TikTok — mp4.

    Args:
        url (str): Ссылка на медиа.
        download_dir (str): Директория для сохранения файла.

    Returns:
        str: Путь к загруженному файлу или строка с ошибкой.
    """
    os.makedirs(download_dir, exist_ok=True)

    url_lower = url.lower()
    is_soundcloud = "soundcloud.com" in url_lower

    format_choice: Literal["mp3", "mp4"]
    if is_soundcloud or not re.search(r"(reel|instagram|tiktok|youtube)", url_lower):
        format_choice = "mp3"
    else:
        format_choice = "mp4"

    ydl_opts: dict = {
        "outtmpl": os.path.join(download_dir, "%(uploader)s - %(title)s.%(ext)s"),
        "quiet": True,
        "retries": 10,
        "fragment_retries": 10,
        "continuedl": True,
        "noplaylist": True,
    }

    if format_choice == "mp3":
        ydl_opts.update({
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "prefer_ffmpeg": True,
        })
    else:
        ydl_opts["format"] = "bestvideo+bestaudio/best"

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download=True)

        filename = ydl.prepare_filename(result)
        if format_choice == "mp3":
            filename = os.path.splitext(filename)[0] + ".mp3"

        return filename

    except Exception as e:
        return f"ERROR: {str(e)}"
