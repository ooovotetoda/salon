import asyncio
import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.markdown import text
from aiogram.utils import executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from config import BOT_TOKEN
from messages import MESSAGES
from quickstart import add
import keyboards as kb


logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG)


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           MESSAGES['start'].format(username=message.from_user.username),
                           reply_markup=kb.greet_kb)

@dp.callback_query_handler(lambda c: c.data == 'entry')
async def process_callback_entry(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'Выберете мастера красоты: ',
                           reply_markup=kb.masters_kb)

@dp.callback_query_handler(lambda c: c.data == 'cancel')
async def process_callback_cancel(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Отмена!')

@dp.callback_query_handler(lambda c: c.data == 'info')
async def process_callback_info(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Информация!')


@dp.callback_query_handler(lambda c: c.data == 'today')
async def process_callback_ondate(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'Выберите дату календаря:',
                           reply_markup=kb.week_kb)

@dp.callback_query_handler(lambda c: c.data == 'tomorrow')
async def process_callback_ondate(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'Выберите дату календаря:',
                           reply_markup=kb.week_kb)

@dp.callback_query_handler(lambda c: c.data == 'aftomorrow')
async def process_callback_ondate(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'Выберите дату календаря:',
                           reply_markup=kb.week_kb)

@dp.callback_query_handler(lambda c: c.data == 'calendar')
async def process_callback_ondate(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'Выберите дату календаря:',
                           reply_markup=kb.week_kb)

@dp.callback_query_handler(lambda c: c.data == 'ondate')
async def process_callback_ondate(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'Выберите дату календаря:',
                           reply_markup=kb.week_kb)

@dp.callback_query_handler(lambda c: c.data == 'dateback')
async def process_callback_ondate(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'Выберите дату календаря:',
                           reply_markup=kb.week_kb)

@dp.callback_query_handler(lambda c: c.data == 'petrova' or 'vorojkova' or 'vasileva')
async def process_callback_master(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           'Выберите дату записи:',
                           reply_markup=kb.date_kb)



@dp.message_handler(commands=['add'])
async def process_add_event(message: types.Message):
    add()


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=shutdown)