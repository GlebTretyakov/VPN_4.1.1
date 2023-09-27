from aiogram import Bot, Dispatcher
import asyncio
from core.handlers.basic import  main_menu_keyboard
import logging
from core.settings import settings
from aiogram import F
from core.keyboards.comands import start_commands
from core.handlers.main_menu_callback import show_profile, router_main_menu_callback


async def start_bot(bot: Bot):
    await start_commands(bot)
    await bot.send_message(settings.bots.admin_id, "Бот запущен")

async def stop_bot(bot:Bot):
    await bot.send_message(settings.bots.admin_id,"Бот упал")


async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=settings.bots.bot_token)
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.include_router(router_main_menu_callback)
    dp.message.register(main_menu_keyboard, F.text == "/start")
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
