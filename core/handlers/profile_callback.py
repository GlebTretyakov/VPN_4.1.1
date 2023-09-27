from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from core.keyboards.profile_menu_inline import profile_menu
router1 = Router()

@router1.callback_query(F.data == 'Profile')
async def show_profile(callback: CallbackQuery):
    await callback.message.answer(f'Профиль', reply_markup=profile_menu)
