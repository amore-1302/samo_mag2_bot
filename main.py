
import telebot
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



bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):

    user_struct = message.from_user
    user_first_name = user_struct.first_name  # Имя пользователя
    user_username = '@'+ user_struct.username  # Ник пользователя в Telegram (может быть None)

    sq_user_id = bot_sql.get_id_user(user_struct)


    bot.send_message(message.chat.id, f"Добро пожаловать, {user_first_name}! Я чат-бот Доставка еды!")

    return sq_user_id


@bot.message_handler(commands=["list"])
def list_message(message):
    sql_list_command(message)


bot.polling(none_stop=True)