from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_back_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⬅️ Ortga")
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)