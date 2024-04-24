"""
users таблица пользователей
Поля
user_id  id пользователя
telega_id id в телеграмме - уникальный во всей таблице
telega_url адрес в телеграмме
name имя пользователя

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    telega_id INTEGER,
    telega_url TEXT  ,
    name TEXT  NOT NULL
)
CREATE UNIQUE INDEX idx_telega_id ON users (telega_id)

"""

import sqlite3

# Подключаемся к базе данных (или создаем новую)
conn = sqlite3.connect('../samo_mag_bot.db')
cursor = conn.cursor()

# Создаем  таблицу, если она еще не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    telega_id INTEGER NOT NULL,
    telega_url TEXT ,
    name TEXT NOT NULL
)
''')

# Создаем уникальный индекс на поле telega_id
cursor.execute('''
CREATE UNIQUE INDEX IF NOT EXISTS idx_telega_id ON users (telega_id);
''')

# Сохраняем изменения в базе данных и закрываем соединение
conn.commit()
conn.close()