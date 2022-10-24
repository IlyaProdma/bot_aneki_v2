from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton
import logging
from config import TOKEN
from crud import funcs, database as db, anek_model
from utils import fill_categories_markup, form_answer_from_anek, form_help_message

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)

dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
callback_acts = CallbackData('prev', 'next')
num_categories = funcs.get_categories_count(db.load_session())


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.answer(form_help_message())

@dp.message_handler(commands=['анек', 'anek', 'анекдот', 'рандом', 'random'])
async def get_random_anek(message: types.Message):
    anek = funcs.get_random_anek(db.load_session())
    await message.answer(form_answer_from_anek(anek).replace('\\n', ' '))

@dp.message_handler(commands=['категории', 'categories', 'cats'])
async def get_categories(message: types.Message):
    markup = fill_categories_markup(0, 5)
    markup.add(
        InlineKeyboardButton(">", callback_data=f"next:5")
    )
    await message.answer('Категории:', reply_markup=markup)

@dp.callback_query_handler(text_startswith='next')
async def show_next_categories(call: types.CallbackQuery):
    await call.answer()
    last_index = int(call.data.split(':')[1])
    markup = fill_categories_markup(last_index, 5)
    if last_index + 5 < num_categories:
        markup.add(
            InlineKeyboardButton("<", callback_data=f"prev:{last_index}"),
            InlineKeyboardButton(">", callback_data=f"next:{last_index + 5}")
        )
    else:
        markup.add(
            InlineKeyboardButton("<", callback_data=f"prev:{last_index}")
        )
    await call.message.edit_text("Категории", reply_markup=markup)

@dp.callback_query_handler(text_startswith='prev')
async def show_prev_categories(call: types.CallbackQuery):
    await call.answer()
    first_index = int(call.data.split(':')[1])
    markup = fill_categories_markup(first_index - 5, 5)
    if first_index - 5 > 0:
        markup.add(
            InlineKeyboardButton("<", callback_data=f"prev:{first_index - 5}"),
            InlineKeyboardButton(">", callback_data=f"next:{first_index}")
        )
    else:
        markup.add(
            InlineKeyboardButton(">", callback_data=f"next:{first_index}")
        )
    await call.message.edit_text("Категории", reply_markup=markup)

@dp.callback_query_handler(text_startswith='category')
async def get_category_anek(call: types.CallbackQuery):
    await call.answer()
    anek = funcs.get_category_anek(db.load_session(), call.data.split(':')[1])
    await call.message.answer(form_answer_from_anek(anek))

async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

if __name__ == '__main__':
    while True:
        try:
            executor.start_polling(dispatcher=dp, skip_updates=True)
        except (KeyboardInterrupt, SystemExit):
            break
        except Exception:
            logging.exception('polling error')