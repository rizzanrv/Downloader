import asyncio
from core.loader import dp, bot
from handlers.download import router
from handlers.start import router as start_router

async def main():
    dp.include_router(start_router)
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
 