from aiogram import Router
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import CommandStart

router: Router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):

    text = (
        "👋 Привет!\n\n"
        "Я Open-Source Telegram бот для скачивания медиа с различных платформ.\n\n"
        "🎯 Возможности:\n"
        "- Скачивание видео и аудио с YouTube, TikTok, Instagram Reels, SoundCloud и многих других.\n"
        "- Автоматическое преобразование форматов (MP4, MP3)\n\n"
        "💻 Я полностью открытый! Ты можешь посмотреть исходный код и помочь с разработкой нажатием кнопки ниже."
    )

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📂 Репозиторий", url="https://github.com/rizzanrv/Downloader")
        ],
        [
            InlineKeyboardButton(text="✉️ Связаться с разработчиком", url="https://t.me/pacxw")
        ]
    ])

    await message.answer(text, reply_markup=keyboard)
