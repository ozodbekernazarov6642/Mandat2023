from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.mandat_respones import return_id_pprint
from aiogram.types import InputFile
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await message.answer("Iltimos Abituriyent ID raqamini kiriting")


@dp.message_handler()
async def bot_start(message: types.Message):
    try:
        id = int(message.text)
        stiker = await message.answer_sticker(InputFile(path_or_bytesio='emoji/AnimatedSticker.tgs'))
        answer = return_id_pprint(message.text)
        await stiker.delete()
        await message.answer(answer)

    except:
        await message.reply("Iltimos ID raqam kiriting")