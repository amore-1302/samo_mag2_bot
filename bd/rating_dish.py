"""
rating_dish таблица лайков, рейтинга блюд в глазах пользователя
Поля
user_id  id пользователя кто сделал рейтин
dish_id  id блюда  которому пользователь поставил рейтинг
rating рейтинг от 1 до 5


CREATE TABLE rating_dish (
    user_id INTEGER NOT NULL,
    dish_id INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    PRIMARY KEY (dish_id,user_id)
)

"""


import sqlite3

# Подключаемся к базе данных (или создаем новую)
conn = sqlite3.connect('../samo_mag_bot.db')
cursor = conn.cursor()

# Создаем  таблицу, если она еще не существует
cursor.execute('''

CREATE TABLE  IF NOT EXISTS  rating_dish (
    user_id INTEGER NOT NULL,
    dish_id INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    PRIMARY KEY (dish_id,user_id)
)

''')


# Сохраняем изменения в базе данных и закрываем соединение
conn.commit()
conn.close()