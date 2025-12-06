from aiogram import Router
from aiogram.types import Message, FSInputFile
from core.config import config
from utils.downloader import download_media
import os

router: Router = Router()

@router.message()
async def download_handler(message: Message):
    url: str = message.text.strip()

    if not url.startswith("http"):
        await message.answer("Пришли нормальную ссылку, пожалуйста.")
        return
    
    if "spotify.com" in url.lower():
        await message.answer("Spotify не поддерживается.")
        return

    status_msg = await message.answer("Секунду... качаю")

    file_path: str = await download_media(url, config.download_dir)

    if file_path.startswith("ERROR"):
        await status_msg.delete()
        await message.answer(f"Ошибка загрузки: {file_path}")
        return

    file_size: int = os.path.getsize(file_path)
    file_name: str = os.path.basename(file_path)
    file_ext: str = os.path.splitext(file_name)[1].lower()

    if file_ext in [".jpg", ".jpeg", ".png", ".webp", ".gif"] and file_size > config.max_photo_size:
        await status_msg.delete()
        await message.answer("Фото слишком большое (макс. 5MB).")
        os.remove(file_path)
        return
    elif file_size > config.max_file_size:
        await status_msg.delete()
        await message.answer("Файл слишком большой (макс. 50MB).")
        os.remove(file_path)
        return

    try:
        document: FSInputFile = FSInputFile(path=file_path)
        bot_info = await message.bot.get_me()
        bot_username = bot_info.username or bot_info.first_name
        await message.answer_document(document, caption=f"*Скачано с помощью @{bot_username}*", parse_mode="Markdown")
    except Exception as e:
        await message.answer("Файл скачался, но отправить его не получилось.")
        print(f"Error sending file: {e}")
    finally:
        if status_msg:
            await status_msg.delete()
        if os.path.exists(file_path):
            os.remove(file_path)
