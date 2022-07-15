from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.markdown import text
from aiogram.utils import executor

from config import BOT_TOKEN
from messages import MESSAGES
from quickstart import add
import keyboards as kb

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

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

@dp.message_handler(commands=['add'])
async def process_callback_info(message: types.Message):
    add()


if __name__ == '__main__':
    executor.start_polling(dp)