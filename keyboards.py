from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

greet_kb = InlineKeyboardMarkup()
entry_btn = InlineKeyboardButton('📝 Запись на приём', callback_data='entry')
cancel_btn = InlineKeyboardButton('⛔ Отмена записи', callback_data='cancel')
info_btn = InlineKeyboardButton('📃 Информация', callback_data='info')

greet_kb.row(entry_btn, cancel_btn)
greet_kb.add(info_btn)

masters_kb = InlineKeyboardMarkup()
petrova_btn = InlineKeyboardButton('💆‍♀️ Петрова Н. А. - Парикмахер-универсал', callback_data='petrova')
vorojkova_btn = InlineKeyboardButton('💆‍♀️ Ворожкова С. Н. - Мастер маникюра', callback_data='vorojkova')
vasileva_btn = InlineKeyboardButton('💆‍♀️ Васильева Е. Г. - Визажист', callback_data='vasileva')
masters_kb = InlineKeyboardMarkup().add(petrova_btn).add(vorojkova_btn).add(vasileva_btn)