"""
restaurants  таблица ресторанов
Поля
restaurant_id  id ресторана
name название
address адрес


CREATE TABLE restaurants (
    restaurant_id INTEGER PRIMARY KEY  AUTOINCREMENT,
    name TEXT   NOT NULL,
    address TEXT  NOT NULL
);

"""

import sqlite3

# Подключаемся к базе данных (или создаем новую)
conn = sqlite3.connect('../samo_mag_bot.db')
cursor = conn.cursor()

# Создаем таблицу, если она еще не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS restaurants (
    restaurant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT  NOT NULL,
    address TEXT  NOT NULL
);
''')



# Сохраняем изменения в базе данных и закрываем соединение
conn.commit()
conn.close()


