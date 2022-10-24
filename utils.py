from crud import funcs, database as db, anek_model
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton

def fill_categories_markup(start: int, limit: int):
    markup = InlineKeyboardMarkup()
    categories = funcs.get_categories_by_range(db.load_session(), start=start, limit=limit)
    for category in categories:
        markup.add(InlineKeyboardButton(category, callback_data=f"category:{category}"))
    return markup

def form_answer_from_anek(anek: anek_model.Anek) -> str:
    answer = f'Анекдот из категории "{anek.cat}" с номером {anek.id}:\n\n'\
        f'{anek.text}'
    return answer

def form_help_message() -> str:
    message = f'Чтобы прочитать случайный анекдот используйте одну из следующих команд:\n'\
              f'/anek /random /анек /анекдот /рандом\n\n'\
              f'Чтобы получить список категорий используйте одну из следующих команд:\n'\
              f'/categories /cats /категории'
    return message