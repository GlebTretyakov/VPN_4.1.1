from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

subscribe_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='1 неделя подписки',
            callback_data='Buy_subscribe_test'
        )
    ],
    [
        InlineKeyboardButton(
            text='1 месяц подписки',
            callback_data='Buy_subscribe_1'
        )
    ],
    [
        InlineKeyboardButton(
            text='2 месяца подписки',
            callback_data='Buy_subscribe_2'
        )
    ],
    [
        InlineKeyboardButton(
            text='3 месяца подписки',
            callback_data='Buy_subscribe_3'
        )
    ],
    [
        InlineKeyboardButton(
            text='6 месяцев подписки',
            callback_data='Buy_subscribe_6'
        )
    ],
    [
        InlineKeyboardButton(
            text='12 месяцев подписки',
            callback_data='Buy_subscribe_12'
        )
    ]
])
