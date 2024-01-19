from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
import uuid
router_subscribe_callback = Router()



@router_subscribe_callback.callback_query(F.data == 'Buy_subscribe_test')
async def test_show(callback: CallbackQuery):
    await callback.message.answer(str(uuid.uuid4()))