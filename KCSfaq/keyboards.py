from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

help_b = KeyboardButton("/help")
about_b = KeyboardButton("О боте")
vopros_b = KeyboardButton("FAQ")

menu_kb.add( vopros_b, help_b, about_b)


menu_kb2 = InlineKeyboardMarkup(row_width=1)

channel_b = InlineKeyboardButton(text="Подписаться на канал разработчиков", url="https://t.me/KomaruCatStudios")
bot_b = InlineKeyboardButton(text="Не нашли нужный вопрос?", url="http://t.me/KomaruStudios_bot")

menu_kb2.add(channel_b,bot_b)