import telebot
from telebot import types

TOKEN = 'YOUR_BOT_TOKEN'
TOKEN = ''


bot = telebot.TeleBot(TOKEN)


# Функция для отправки сообщения с кнопками оценок
@bot.message_handler(commands=['start', 'rate'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=5)
    # Создаем кнопки для оценок от 1 до 5
    buttons = [types.InlineKeyboardButton(text=str(i), callback_data=str(i)) for i in range(1, 6)]
    but_0 = types.InlineKeyboardButton(text=str(0), callback_data=str(0))
    buttons.append(but_0)
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Оцените это сообщение от 0 до 5:", reply_markup=markup)

# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data.isdigit():
        rating = int(call.data)
        bot.answer_callback_query(call.id, f"Спасибо за вашу оценку: {rating}")
        # Здесь можно добавить логику обработки оценки, например, сохранение в базу данных

bot.polling(none_stop=True, interval=3)