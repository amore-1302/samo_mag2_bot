
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
TOKEN = '7093861093:AAH5k8q2J-fITlb7lfSOv3hlYFtwLCG1CsM'
# TOKEN = '6708953536:AAHOykPXIJK2ZaIGB7rHGh5Pt0CchHE-bH0' # @zelenograd_food_bot
bot = telebot.TeleBot(TOKEN)

# необходимо объединить в класс и хранить объект класса для каждого пользователя
_choose_restaurant = ""
_order = []

# Список ресторанов их меню
_restaurants = []
_restaurant_about_menu = []
_restaurant_dishes_menu = []
_restaurant_details = {"Описание", "Отзывы", "Рейтинг", "Блюда", "Галерея" }

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
            item_btn = types.KeyboardButton(restaurant[1])
            markup.add(item_btn)
            _restaurants.append(restaurant[1])
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
#*****************************************************************************
# Заказы
#*****************************************************************************
@bot.message_handler(func=lambda message: message.text == 'Заказы')
def handle_orders(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add(types.KeyboardButton('Главное меню'))
    if orders_queue:
        bot.send_message(message.chat.id, "Очередь заказов:")
        for ord in orders_queue:
            bot.send_message(message.chat.id, ord, reply_markup=markup)
        bot.send_message(message.chat.id, f"Время ожидания: {waiting_time} мин", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "У вас нет заказа.", reply_markup=markup)
#*****************************************************************************
# Настройка
#*****************************************************************************
@bot.message_handler(func=lambda message: message.text == 'Настройки')
def handle_settings(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.add(types.KeyboardButton('Главное меню'))
    bot.send_message(message.chat.id, "Настройки пока недоступны", reply_markup=markup)

bot.polling()