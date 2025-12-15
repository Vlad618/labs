from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🚀 Старт")]
    ],
    resize_keyboard=True
)

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛒 Каталог")],
        [KeyboardButton(text="📦 Оформити замовлення")]
    ],
    resize_keyboard=True
)