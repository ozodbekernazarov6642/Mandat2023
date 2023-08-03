from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from keyboards.default.input_button import menu_Button
from states.id_qr_states import menu_State
from loader import dp
from aiogram import types


@dp.message_handler(Text(equals='⬅️ Ortga'), state=menu_State.id)
async def back(message: types.Message, state: FSMContext):
    await message.answer("Tugmalarni biri tanlang👇", reply_markup=menu_Button)
    await state.finish()

@dp.message_handler(Text(equals='⬅️ Ortga'), state=menu_State.qr)
async def back(message: types.Message, state: FSMContext):
    await message.answer("Tugmalarni biri tanlang👇", reply_markup=menu_Button)
    await state.finish()

@dp.message_handler(Text(equals='⬅️ Ortga'))
async def back(message: types.Message, state: FSMContext):
    await message.answer("Tugmalarni biri tanlang👇", reply_markup=menu_Button)
