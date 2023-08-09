from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from keyboards.default.back_button import menu_back_button

from states.id_qr_states import menu_State
from utils.mandat_response import return_id_pprint
from aiogram.types import InputFile
from loader import dp


@dp.message_handler(Text(equals='🆔 ID-raqam orqali'))
async def answer_handler_id(message: types.Message):
    await message.answer_photo(photo='http://telegra.ph//file/8323ba43e0a2a0825cb9f.jpg', caption="Namunaga binoan Abituriyent ID raqamini kiriting👇", reply_markup=menu_back_button)
    await menu_State.id.set()


@dp.message_handler(state=menu_State.id)
async def result_id(message: types.Message, state: FSMContext):
        try:
            raqam = int(message.text)
            stiker = await message.answer_sticker(InputFile(path_or_bytesio='emoji/AnimatedSticker.tgs'))
            answer = return_id_pprint(message.text)
            await stiker.delete()
            await message.answer(answer, reply_markup=menu_back_button)
            await state.finish()
        except:
            await message.reply_photo(photo='http://telegra.ph//file/8323ba43e0a2a0825cb9f.jpg',caption="Iltimos Namunaga binoan ID raqam kiriting👇", reply_markup=menu_back_button)
            await next(result_id)

            await state.finish()

