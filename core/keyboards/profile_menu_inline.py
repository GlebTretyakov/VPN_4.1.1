from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

profile_menu = InlineKeyboardMarkup (inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Ваш профиль',
            callback_data='your_profile'
        )
    ],
    [
        InlineKeyboardButton(
            text='Осталось 6 дней подписки',
            callback_data='Subscribe'
        )
    ]
])