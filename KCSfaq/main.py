from aiogram import Bot,Dispatcher,types, executor
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import InputFile
from config import TOKEN
from text import *
from keyboards import *
import time

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
startpic = InputFile("KCSlogo.png")
voprospic = InputFile("chast_vopros.png")
skrinpic = InputFile("rofl.png")
pomoshpic = InputFile("pomosh.png")
o_botepic = InputFile("o_bote.png")
otvpic = InputFile("logo_otv14.png")

@dp.message_handler(commands="start")
async def hello(msg:types.Message):
    await bot.send_photo(chat_id=msg.chat.id, photo=InputFile("chast_vopros.png"), caption=faq, reply_markup=menu_kb3)

@dp.callback_query_handler(text="faq")
async def otv4def(call: types.CallbackQuery):
    await bot.send_photo(chat_id=call.from_user.id, photo=InputFile("chast_vopros.png"), caption=faq, reply_markup=menu_kb3)
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)


@dp.callback_query_handler(text="1")
async def otv1def(call: types.CallbackQuery):
    await call.message.answer(text=otv1, reply_markup=menu_kb)
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

@dp.callback_query_handler(text="2")
async def otv2def(call: types.CallbackQuery):
    await call.message.answer(text=otv2, reply_markup=menu_kb)
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

@dp.callback_query_handler(text="3")
async def otv3def(call: types.CallbackQuery):
    await bot.send_photo(chat_id=call.from_user.id, photo=InputFile("rofl.png"), caption=otv3, reply_markup=menu_kb)
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

@dp.callback_query_handler(text="4")
async def otv4def(call: types.CallbackQuery):
    await call.message.answer(text=otv4, reply_markup=menu_kb)
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

@dp.callback_query_handler(text="5")
async def otv5def(call: types.CallbackQuery):
    await call.message.answer(text=otv5, reply_markup=menu_kb)
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

@dp.callback_query_handler(text="6")
async def otv6def(call: types.CallbackQuery):
    await call.message.answer(text=otv6, reply_markup=menu_kb)
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

@dp.callback_query_handler(text="7")
async def otv7def(call: types.CallbackQuery):
    await call.message.answer(text=otv7, reply_markup=menu_kb)
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

@dp.callback_query_handler(text="8")
async def otv8def(call: types.CallbackQuery):
    await call.message.answer(text=otv8, reply_markup=menu_kb)
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

@dp.callback_query_handler(text="9")
async def otv9def(call: types.CallbackQuery):
    await call.message.answer(text=otv9, reply_markup=menu_kb)
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

@dp.callback_query_handler(text="10")
async def otv10def(call: types.CallbackQuery):
    await call.message.answer(text=otv10, reply_markup=menu_kb)
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

@dp.callback_query_handler(text="11")
async def otv11def(call: types.CallbackQuery):
    await call.message.answer(text=otv11, reply_markup=menu_kb)
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

@dp.callback_query_handler(text="12")
async def otv12def(call: types.CallbackQuery):
    await call.message.answer(text=otv12, reply_markup=menu_kb)
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

@dp.callback_query_handler(text="13")
async def otv13def(call: types.CallbackQuery):
    await call.message.answer(text=otv13, reply_markup=menu_kb)
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

@dp.callback_query_handler(text="14")
async def otv14def(call: types.CallbackQuery):
    await bot.send_photo(chat_id=call.from_user.id, photo=InputFile("logo_otv14.png"), caption=otv14, reply_markup=menu_kb)
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

@dp.callback_query_handler(text="15")
async def otv15def(call: types.CallbackQuery):
    await call.message.answer(text=otv15, reply_markup=menu_kb)
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

@dp.callback_query_handler(text="/help")
async def hepldef(call: types.CallbackQuery):
    await bot.send_photo(chat_id=call.from_user.id, photo=InputFile("pomosh.png"), caption=help, reply_markup=menu_kb2)
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

@dp.callback_query_handler(text="О боте")
async def aboutdef(call: types.CallbackQuery):
    await bot.send_photo(chat_id=call.from_user.id, photo=InputFile("o_bote.png"), caption=avtor, reply_markup=menu_o_bote)
    await call.answer()
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)