"""
rating_rest таблица лайков, рейтинга ресторана в глазах пользователя
Поля
user_id  id пользователя кто сделал рейтинг
restaurant_id  id ресторана  которому пользователь поставил рейтинг
rating рейтинг от 1 до 5


CREATE TABLE rating_rest (
    user_id INTEGER NOT NULL,
    restaurant_id INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    PRIMARY KEY (restaurant_id,user_id)
)

"""


import sqlite3

# Подключаемся к базе данных (или создаем новую)
conn = sqlite3.connect('../samo_mag_bot.db')
cursor = conn.cursor()

# Создаем  таблицу, если она еще не существует
cursor.execute('''
CREATE TABLE  IF NOT EXISTS  rating_rest (
    user_id INTEGER NOT NULL,
    restaurant_id INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    PRIMARY KEY (restaurant_id,user_id)
)
''')


# Сохраняем изменения в базе данных и закрываем соединение
conn.commit()
conn.close()