from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from datetime import date, datetime, timedelta
from weekdays_converter import convert

greet_kb = InlineKeyboardMarkup()
entry_btn = InlineKeyboardButton('📝 Запись на приём', callback_data='entry')
cancel_btn = InlineKeyboardButton('⛔ Отмена записи', callback_data='cancel')
info_btn = InlineKeyboardButton('📃 Информация', callback_data='info')

greet_kb.row(entry_btn, cancel_btn)
greet_kb.add(info_btn)

masters_kb = InlineKeyboardMarkup()
petrova_btn = InlineKeyboardButton('💆‍♀️ Петрова Н. А. - Парикмахер-универсал', callback_data='petrova_state')
vorojkova_btn = InlineKeyboardButton('💆‍♀️ Ворожкова С. Н. - Мастер маникюра', callback_data='vorojkova_state')
vasileva_btn = InlineKeyboardButton('💆‍♀️ Васильева Е. Г. - Визажист', callback_data='vasileva_state')
masters_kb.add(petrova_btn).add(vorojkova_btn).add(vasileva_btn)

date_kb = InlineKeyboardMarkup()
today_btn = InlineKeyboardButton('🕖 На сегодня', callback_data='today')
tomorrow_btn = InlineKeyboardButton('🕜 На завтра', callback_data='tomorrow')
aftomorrow_btn = InlineKeyboardButton('🕐 На послезавтра', callback_data='after_tomorrow')
calendar_btn = InlineKeyboardButton('📅 Календарь дат', callback_data='calendar')
ondate_btn = InlineKeyboardButton('🔢 На дату', callback_data='on_date')
dateback_btn = InlineKeyboardButton('◀️ Возврат', callback_data='date_back')
date_kb.add(today_btn, calendar_btn).add(tomorrow_btn, ondate_btn).add(aftomorrow_btn, dateback_btn)

first_day = date.today()
second_day = first_day + timedelta(days=1)
third_day = first_day + timedelta(days=2)
fourth_day = first_day + timedelta(days=3)
fifth_day = first_day + timedelta(days=4)
sixth_day = first_day + timedelta(days=5)
seventh_day = first_day + timedelta(days=6)

week_kb = InlineKeyboardMarkup()
first_day_btn = InlineKeyboardButton(f'🔔 Запись на {convert(datetime.today().weekday())} - {first_day}', callback_data='first_day')
second_day_btn = InlineKeyboardButton(f'🔔 Запись на {convert(datetime.today().weekday() + 1)} - {second_day} ', callback_data='second_day')
third_day_btn = InlineKeyboardButton(f'🔔 Запись на {convert(datetime.today().weekday() + 2)} - {third_day} ', callback_data='third_day')
fourth_day_btn = InlineKeyboardButton(f'🔔 Запись на {convert(datetime.today().weekday() + 3)} - {fourth_day} ', callback_data='fourth_day')
fifth_day_btn = InlineKeyboardButton(f'🔔 Запись на {convert(datetime.today().weekday() + 4)} - {fifth_day} ', callback_data='fifth_day')
sixth_day_btn = InlineKeyboardButton(f'🔔 Запись на {convert(datetime.today().weekday() + 5)} - {sixth_day} ', callback_data='sixth_day')
seventh_day_btn = InlineKeyboardButton(f'🔔 Запись на {convert(datetime.today().weekday() + 6)} - {seventh_day} ', callback_data='seventh_day')
week_kb.add(first_day_btn).add(second_day_btn).add(third_day_btn).add(fourth_day_btn).add(fifth_day_btn).add(
    sixth_day_btn).add(seventh_day_btn)

time_kb = InlineKeyboardMarkup()
t10_btn = InlineKeyboardButton('🕛 Запись на 10', callback_data='time_10')
t11_btn = InlineKeyboardButton('🕛 Запись на 11', callback_data='time_11')
t12_btn = InlineKeyboardButton('🕛 Запись на 12', callback_data='time_12')
t13_btn = InlineKeyboardButton('🕛 Запись на 13', callback_data='time_13')
t14_btn = InlineKeyboardButton('🕛 Запись на 14', callback_data='time_14')
t15_btn = InlineKeyboardButton('🕛 Запись на 15', callback_data='time_15')
time_kb.add(t10_btn).add(t11_btn).add(t12_btn).add(t13_btn).add(t14_btn).add(t15_btn)