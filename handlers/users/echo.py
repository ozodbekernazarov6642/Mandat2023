from aiogram import types
from keyboards.default.input_button import menu_Button
from loader import dp


# Echo bot
@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer("Iltimos tugmalardan birini tanlang👇", reply_markup=menu_Button)
