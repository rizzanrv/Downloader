from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass
class Config:
    bot_token: str = os.getenv("BOT_TOKEN")
    download_dir: str = os.getenv("DOWNLOAD_DIR", "downloads")
    max_photo_size: int = 5 * 1024 * 1024
    max_file_size: int = 50 * 1024 * 1024

config = Config()
