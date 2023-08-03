from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from states.id_qr_states import menu_State
from utils.Qr_response import Qr_answer
from aiogram.types import InputFile
from keyboards.default.input_button import menu_Button
from keyboards.default.back_button import menu_back_button
from loader import dp


@dp.message_handler(Text(equals='🪪 Qr-code orqali'))
async def answer_qr(message: types.Message):
    await message.answer("Qr-code rasmini yuboring", reply_markup=menu_back_button)
    await menu_State.qr.set()


@dp.message_handler(content_types=types.ContentType.PHOTO, state=menu_State.qr)
async def qr_scanner(message: types.Message, state: FSMContext):
    photo = message.photo[-1]
    emoji = await message.answer_sticker(InputFile(path_or_bytesio='emoji/AnimatedSticker.tgs'))
    respones = await Qr_answer(photo)
    if respones != False:
        if respones == "Exception: An invalid request URI was provided. Either the request URI must be an absolute URI or BaseAddress must be set.":
            await emoji.delete()
            await message.reply("Kechirasiz QR-code scanner ishlashda xatolik yuz berdi!\n\n"
                                "Hozirda ID raqamdan foydalansangiz ham boladi👇.\n", reply_markup=menu_back_button)
            await state.finish()
            await menu_State.id.set()
        elif respones == "Xato":
            await emoji.delete()
            await message.reply("Siz QR-code yubormadingiz\n\n"
                                "Qr-code rasmini yuboring")
            await next(qr_scanner)
        else:
            await emoji.delete()
            await message.answer(f"{respones}\n\n"
                                 f"________________________________________________\n\n"
                                 f"Bu men👉: <a href='https://t.me/e_Mandatbot'>E-Mandat 2023 | Rasmiy bot</a>", reply_markup=menu_back_button)
            await state.finish()
    elif respones == False:
        await emoji.delete()
        await message.answer("❌ Xatolik\n\n"
                             "🪪 QR-code o'qilmadi", reply_markup=menu_back_button)
        await next(qr_scanner)


    await state.finish()

@dp.message_handler(state=menu_State.qr)
async def error_Qr(message: types.Message):
    await message.reply("Iltimos Qr-code yuboring 👇", reply_markup=menu_back_button)


