from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menu_o_bote = InlineKeyboardMarkup(row_width=1)

faq_b = InlineKeyboardButton(text="FAQ", callback_data="faq")
help_b = InlineKeyboardButton(text="Помощь", callback_data="/help")

menu_o_bote.add(faq_b,help_b)

menu_kb2 = InlineKeyboardMarkup(row_width=1)

channel_b = InlineKeyboardButton(text="Подписаться на канал разработчиков", url="https://t.me/KomaruCatStudios")
bot_b = InlineKeyboardButton(text="Не нашли нужный вопрос?", url="http://t.me/KomaruStudios_bot")
faq_b = InlineKeyboardButton(text="FAQ", callback_data="faq")
about_b = InlineKeyboardButton(text="О боте", callback_data="О боте")

menu_kb2.add(channel_b,bot_b,faq_b,about_b)

menu_kb3 = InlineKeyboardMarkup(row_width=3)

otv1_b = InlineKeyboardButton(text="1",callback_data="1")
otv2_b = InlineKeyboardButton(text="2",callback_data="2")
otv3_b = InlineKeyboardButton(text="3",callback_data="3")
otv4_b = InlineKeyboardButton(text="4",callback_data="4")
otv5_b = InlineKeyboardButton(text="5",callback_data="5")
otv6_b = InlineKeyboardButton(text="6",callback_data="6")
otv7_b = InlineKeyboardButton(text="7",callback_data="7")
otv8_b = InlineKeyboardButton(text="8",callback_data="8")
otv9_b = InlineKeyboardButton(text="9",callback_data="9")
otv10_b = InlineKeyboardButton(text="10",callback_data="10")
otv11_b = InlineKeyboardButton(text="11",callback_data="11")
otv12_b = InlineKeyboardButton(text="12",callback_data="12")
otv13_b = InlineKeyboardButton(text="13",callback_data="13")
otv14_b = InlineKeyboardButton(text="14",callback_data="14")
otv15_b = InlineKeyboardButton(text="15",callback_data="15")
help_b = InlineKeyboardButton(text="Помощь", callback_data="/help")
about_b = InlineKeyboardButton(text="О боте", callback_data="О боте")

menu_kb3.add(otv1_b,otv2_b,otv3_b,otv4_b,otv5_b,otv6_b,otv7_b,otv8_b,otv9_b,otv10_b,otv11_b,otv12_b,otv13_b,otv14_b,otv15_b, help_b, about_b)


menu_kb = InlineKeyboardMarkup(row_width=1)

comeback_b = InlineKeyboardButton(text="Вернутся к списку вопросов", callback_data="faq")
help_b = InlineKeyboardButton(text="Помощь", callback_data="/help")
about_b = InlineKeyboardButton(text="О боте", callback_data="О боте")

menu_kb.add(comeback_b, help_b,about_b)