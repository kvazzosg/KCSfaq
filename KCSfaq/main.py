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
    await bot.send_photo(chat_id=msg.chat.id, photo=startpic, caption=start, reply_markup=menu_kb)

@dp.message_handler(text="FAQ")
async def faqdef(msg:types.Message):
    await bot.send_photo(chat_id=msg.chat.id, photo=voprospic, caption=faq)

@dp.message_handler(text="1")
async def otv1def(msg:types.Message):
    await msg.answer(otv1)

@dp.message_handler(text="2")
async def otv2def(msg:types.Message):
    await msg.answer(otv2)

@dp.message_handler(text="3")
async def otv3def(msg:types.Message):
    await bot.send_photo(chat_id=msg.chat.id, photo=skrinpic, caption=otv3)
    ReplyKeyboardRemove(menu_kb)

@dp.message_handler(text="4")
async def otv4def(msg:types.Message):
    await msg.answer(otv4)

@dp.message_handler(text="5")
async def otv5def(msg:types.Message):
    await msg.answer(otv5)
    ReplyKeyboardRemove(menu_kb)

@dp.message_handler(text="6")
async def otv6def(msg:types.Message):
    await msg.answer(otv6)

@dp.message_handler(text="7")
async def otv7def(msg:types.Message):
    await msg.answer(otv7)

@dp.message_handler(text="8")
async def otv8def(msg:types.Message):
    await msg.answer(otv8)

@dp.message_handler(text="9")
async def otv9def(msg:types.Message):
    await msg.answer(otv9)

@dp.message_handler(text="10")
async def otv10def(msg:types.Message):
    await msg.answer(otv10)

@dp.message_handler(text="11")
async def otv11def(msg:types.Message):
    await msg.answer(otv11)

@dp.message_handler(text="12")
async def otv12def(msg:types.Message):
    await msg.answer(otv12)

@dp.message_handler(text="13")
async def otv13def(msg:types.Message):
    await msg.answer(otv13)

@dp.message_handler(text="14")
async def otv14def(msg:types.Message):
    time.sleep(5)
    await bot.send_photo(chat_id=msg.chat.id, photo=otvpic, caption=otv14)

@dp.message_handler(text="15")
async def otv15def(msg:types.Message):
    await msg.answer(otv15)
@dp.message_handler(commands="help")
async def help(msg:types.Message):
    await bot.send_photo(chat_id=msg.chat.id, photo=pomoshpic, caption=helpdef)

@dp.message_handler(text="О боте")
async def avtor_b(msg:types.Message):
    await bot.send_photo(chat_id=msg.chat.id, photo=o_botepic, caption=avtor, reply_markup=menu_kb2)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)