
import telebot
from telebot import types
import bot_sql

def  sql_list_command(message):
    rows = bot_sql.sql_list_rest()
    curent_pos = 0
    res_str = 'Список ресторанов :\n'
    for row in rows:
        curent_pos = curent_pos + 1
        res_str = res_str + f'{curent_pos} {row[1]}\n'
    if curent_pos <= 0:
        res_str = 'Список ресторанов пустой !!!'

    bot.reply_to(message, res_str)


# основной бот
TOKEN = 'TOKEN'




bot = telebot.TeleBot(TOKEN)

# необходимо объединить в класс и хранить объект класса для каждого пользователя
_choose_restaurant = ""
_order = []

# Список ресторанов их меню
_restaurants = {}
_restaurant_about_menu = []
_restaurant_category_menu = {}
_restaurant_dishes_menu = []
_restaurant_details = ["Меню", "Галерея", "Рейтинг ресторана", "Оценить ресторан", "Отзывы", "Добавить отзыв"]

# Рейтинги
_rating=""

# Очередь заказов и время ожидания
_orders_queue = []
_waiting_time = 10


#*****************************************************************************
# Главное меню
#*****************************************************************************
def main_menu_markup():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    buttons = [types.KeyboardButton(text) for text in ['Рестораны', 'Заказы', 'Настройки']]
    markup.add(*buttons)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):

    user_struct = message.from_user
    user_first_name = user_struct.first_name  # Имя пользователя
    user_username = '@'+ user_struct.username  # Ник пользователя в Telegram (может быть None)

    sq_user_id = bot_sql.get_id_user(user_struct)

    bot.send_message(message.chat.id, f"Добро пожаловать, {user_first_name}! Я чат-бот Доставка еды!")
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=main_menu_markup())
    return sq_user_id

@bot.message_handler(func=lambda message: message.text == 'Главное меню')
def handle_main_menu(message):
    bot.send_message(message.chat.id, "Возвращаемся в главное меню:", reply_markup=main_menu_markup())


@bot.message_handler(commands=["list"])
def list_message(message):
    sql_list_command(message)


# *****************************************************************************
# Блюда
#  *****************************************************************************
def category_menu_markup(markup):
    id_rest = _restaurants[_choose_restaurant]
    rows = bot_sql.get_categorys_for_restorany(id_rest)
    _restaurant_category_menu.clear()
    for text in rows:
        markup.add(types.KeyboardButton(text[1]))
        _restaurant_category_menu[text[1]] = text[0]
    return markup

@bot.message_handler(func=lambda message: message.text == 'Категории блюд ресторана')
def handle_restaurant_category(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup = category_menu_markup(markup)
    bot.send_message(message.chat.id, f"Выберете категорию блюд {_choose_restaurant}:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in _restaurant_category_menu.keys())
def handle_category(message):
    global _choose_restaurant  # Добавляем это, чтобы обновлять глобальную переменную
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add(types.KeyboardButton('Главное меню'))
    markup.add(types.KeyboardButton('Категории блюд ресторана'))
    markup.add(types.KeyboardButton('Сделать заказ'))
    rows = bot_sql.get_dishs_for_categorys_and_restorany(_restaurants[_choose_restaurant], _restaurant_category_menu[message.text])
    for row in rows:
        bot.send_message(message.chat.id, f"{row[0]}.\t{row[1]}:\t\t\t\t{row[2]}")
    bot.send_message(message.chat.id, "Выберите номер блюда или вернитесь в <Категории блюд ресторана>:", reply_markup=markup)

#*****************************************************************************
# Рестораны
#*****************************************************************************
@bot.message_handler(func=lambda message: message.text == 'Рестораны')
def handle_restaurants(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add(types.KeyboardButton('Главное меню'))
    restaurants = bot_sql.sql_list_rest()
    if not restaurants:
        res_str = 'Список ресторанов пустой. Проверьте соединение.'
    else:
        _restaurants.clear()
        for restaurant in restaurants:
            name_rest = restaurant[1]
            #            if restaurant[3]:
            #    val_0 = int(restaurant[3])
            #    if val_0 > 0:
            #        name_rest = f"{name_rest}    ({val_0})"

            item_btn = types.KeyboardButton(name_rest)
            markup.add(item_btn)
            _restaurants[restaurant[1]] = restaurant[0]
        bot.send_message(message.chat.id, "Выберите ресторан:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in _restaurants)
def handle_restaurant(message):
    global _choose_restaurant  # Добавляем это, чтобы обновлять глобальную переменную
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add(types.KeyboardButton('Главное меню'))
    markup.add(types.KeyboardButton('Рестораны'))
    restaurant = message.text
    _choose_restaurant = message.text
    _restaurant_about_menu.clear()
    for details in _restaurant_details:
        menu_name = _choose_restaurant+'. '+details
        _restaurant_about_menu.append(menu_name)
        item_btn = types.KeyboardButton(menu_name)
        markup.add(item_btn)
    menu_text = f"Вы выбрали {restaurant}.\nВыберите информацию о ресторане\n" # + '\n'.join(menu)
    bot.send_message(message.chat.id, menu_text, reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in _restaurant_about_menu)
def handle_restaurant_info(message):
    global _rating
    comma_index = message.text.find('.')
    info = "Невозможно предоставить информацию"
    if comma_index != -1:  # Если точка найдена
        info = message.text[comma_index+2:]
    if info == "Отзывы":
        bot.send_message(message.chat.id, "Выводим 5 популярных отзыва")
    elif info == "Рейтинг ресторана":
        bot.send_message(message.chat.id, "Выводим рейтинг ресторана")
    elif info == "Оценить ресторан":
        _rating = "restaurant"
        markup = types.InlineKeyboardMarkup(row_width=5)
        # Создаем кнопки для оценок от 1 до 5
        buttons = [types.InlineKeyboardButton(text=str(i), callback_data=str(i)) for i in range(1, 6)]
        but_0 = types.InlineKeyboardButton(text="Убрать оценку", callback_data="Убрать оценку")
        buttons.append(but_0)
        markup.add(*buttons)
        bot.send_message(message.chat.id, "Оцените ресторан от 1 до 5:", reply_markup=markup)
    elif info == "Галерея":
        bot.send_message(message.chat.id, "Выводим галерею ресторана")
    elif info == "Меню":
        markup = types.ReplyKeyboardMarkup(row_width=3)
        markup.add(types.KeyboardButton('Главное меню'))
        markup.add(types.KeyboardButton('Рестораны'))
        markup = category_menu_markup(markup)
        bot.send_message(message.chat.id, f"Выберете категорию блюд {_choose_restaurant}:", reply_markup=markup)

#*****************************************************************************
# Рейтинги
#*****************************************************************************
@bot.callback_query_handler(func=lambda call: True)
def handle_rating(call):
    global _rating
    if not call.data.isdigit():
        bot.answer_callback_query(call.id, f"Оценка отменена")
        return

    if _rating == "restaurant":
        bot.answer_callback_query(call.id, f"Спасибо за вашу оценку ресторана: {call.data}")
        id_telega = call.from_user.id
        sq_user_id = bot_sql.get_from_telega_user_id_id_user(id_telega)
        val0 = int(call.data)
        #print(_restaurants)

        #Временно поставил ресторан 1
        bot_sql.change_rating_rest(1, sq_user_id, val0 )
    elif _rating == "dish":
        bot.answer_callback_query(call.id, f"Спасибо за вашу оценку блюда: {call.data}")
    _rating = ""
#*****************************************************************************
# Заказы
#*****************************************************************************
@bot.message_handler(func=lambda message: message.text == 'Заказы')
def handle_orders(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add(types.KeyboardButton('Главное меню'))
    if _orders_queue:
        bot.send_message(message.chat.id, "Очередь заказов:")
        for ord in _orders_queue:
            bot.send_message(message.chat.id, ord, reply_markup=markup)
        bot.send_message(message.chat.id, f"Время ожидания: {_waiting_time} мин", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "У вас нет заказа.", reply_markup=markup)
#*****************************************************************************
#  Настройка
#*****************************************************************************
@bot.message_handler(func=lambda message: message.text == 'Настройки')
def handle_settings(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add(types.KeyboardButton('Главное меню'))
    bot.send_message(message.chat.id, "Настройки пока недоступны", reply_markup=markup)

bot.polling(none_stop=True, interval=3)