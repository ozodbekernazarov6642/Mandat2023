from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


menu_Button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🆔 ID-raqam orqali"),
            KeyboardButton(text='🪪 Qr-code orqali')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)