from aiogram import Bot
from aiogram.types import Message
from core.keyboards.main_menu_inline import main_menu
from core.database.db import Database

db = Database('database.db')


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Privet {message.from_user.first_name} Hello_World')


async def subscribe(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, "Выберите версию подписки")


async def main_menu_keyboard(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, "Главное меню", reply_markup=main_menu)
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
    else:
        await bot.send_message(message.from_user.id, "Вы уже зарегистрированы!")
