from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Профиль',
            callback_data='Profile'
        )
    ],
    [
        InlineKeyboardButton(
            text='Оформить подписку / продлить',
            callback_data='Buy_subscribe'
        )
    ],
    [
        InlineKeyboardButton(
            text='Пробная подписка',
            callback_data='Trial'
        )
    ],
    [
        InlineKeyboardButton(
            text='Тех. поддержка',
            callback_data='support'
        )
    ],
    [
        InlineKeyboardButton(
            text='Информация',
            callback_data='info'
        )
    ]

])
