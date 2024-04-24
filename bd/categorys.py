"""
users таблица категорий блюд
Поля
category_id   id категории
name имя категории
descr описание категории
sort упорядочиваем категории по полю sort

CREATE TABLE categorys (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    descr TEXT NOT NULL,
    sort INT NOT NULL
)

CREATE UNIQUE INDEX IF NOT EXISTS idx_sort ON categorys(sort)

"""

import sqlite3

# Подключаемся к базе данных (или создаем новую)
conn = sqlite3.connect('../samo_mag_bot.db')
cursor = conn.cursor()

# Создаем  таблицу, если она еще не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS categorys (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    descr TEXT NOT NULL,
    sort INT NOT NULL    
)
''')



cursor.execute('''
CREATE UNIQUE INDEX IF NOT EXISTS idx_sort ON categorys(sort)
''')

# Сохраняем изменения в базе данных
conn.commit()

# Закрываем соединение с базой данных
conn.close()