from aiogram import Bot, Dispatcher
from core.config import config

bot: Bot = Bot(token=config.bot_token)
dp: Dispatcher = Dispatcher()
