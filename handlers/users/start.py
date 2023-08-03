from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.id_qr_states import menu_State
from keyboards.default.input_button import menu_Button
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n\n"
                         f"Botdan foydalanish uchun tugmalardan birini tanlang🤳", reply_markup=menu_Button)



@dp.message_handler(CommandStart(), state=menu_State.id)
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n\n"
                         f"Botdan foydalanish uchun tugmalardan birini tanlang🤳", reply_markup=menu_Button)


@dp.message_handler(CommandStart(), state=menu_State.qr)
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n\n"
                         f"Botdan foydalanish uchun tugmalardan birini tanlang🤳", reply_markup=menu_Button)
