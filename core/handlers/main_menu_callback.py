from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from core.keyboards.main_menu_inline import main_menu
from core.keyboards.profile_menu_inline import profile_menu
from core.keyboards.subscribe_menu_inline import subscribe_menu
from core.database.db import Database
from core.handlers.functions import time_sub_day
db = Database('database.db')

router_main_menu_callback = Router()

@router_main_menu_callback.callback_query(F.data == 'Profile')
async def show_profile(callback: CallbackQuery):
    await callback.message.answer(f'Профиль', reply_markup=profile_menu)
    await callback.answer()
    await callback.message.answer("Главное меню")
    if not db.user_exists(938346742):
        db.add_user(938346742)
    else:
        await callback.message.answer("Вы уже зарегистрированы!")
        await callback.message.answer(db.get_telegram_id(7))

    user_sub = time_sub_day(db.get_time_sub(938346742))
    end_sub = str(user_sub)
    end_sub = end_sub[:-10]
    if user_sub == False:
        end_sub = "У вас нет подписки"
    end_sub = "\nПодписка истекает через: " + end_sub
    await callback.message.answer(str(938346742) + "\nВаш ID: " + str(938346742) + end_sub)




@router_main_menu_callback.callback_query(F.data == 'Buy_subscribe')
async def show_subscribe(callback: CallbackQuery):
    await callback.message.answer('Выберите подписку', reply_markup=subscribe_menu)
    await callback.answer()