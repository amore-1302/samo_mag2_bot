

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = '11111111111111111'
# Замените 'your_token' на ваш токен бота

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton("Кнопка 1", callback_data="btn1")
    button_2 = types.InlineKeyboardButton("Кнопка 2", callback_data="btn2")
    button_3 = types.InlineKeyboardButton("Кнопка +", callback_data="btn3")
    button_4 = types.InlineKeyboardButton("Кнопка -", callback_data="btn4")
    keyboard.add(button_1, button_2, button_3, button_4)
    await message.answer("Выберите кнопку:", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'btn1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    # Обновление клавиатуры
    keyboard = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton("Новая кнопка", callback_data="btn13")
    button_2 = types.InlineKeyboardButton("Кнопка 2", callback_data="btn2")
    button_3 = types.InlineKeyboardButton("Кнопка +", callback_data="btn3")
    button_4 = types.InlineKeyboardButton("Кнопка -", callback_data="btn4")
    keyboard.add(button_1, button_2, button_3, button_4)
    await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                text="Вы нажали на новую кнопку 1",
                                reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'btn2')
async def process_callback_button2(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                text="Вы нажали кнопку 2")
@dp.callback_query_handler(lambda c: c.data == 'btn3')
async def process_callback_button2(callback_query: types.CallbackQuery):
    print("нажали +")


@dp.callback_query_handler(lambda c: c.data == 'btn4')
async def process_callback_button2(callback_query: types.CallbackQuery):
    print("нажали -")

@dp.callback_query_handler(lambda c: c.data == 'btn13')
async def process_callback_button2(callback_query: types.CallbackQuery):
    await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                text="Вы нажали кнопку 13")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

