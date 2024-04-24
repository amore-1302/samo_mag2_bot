"""
dishs таблица блюд
Поля
dish_id   id блюда
restaurant_id  - идентификатор ресторана, к которому относится блюдо.
category_id    - категория блюда
name название название блюда
descr описание блюда
price стоимость блюда рубли, копейки

фотографией займемся потом
два варианта
вариант 1 ссылка на фото
вариант 2 хранить в столбце blob

descr описание категории

CREATE TABLE IF NOT EXISTS dishs (
    dish_id INTEGER PRIMARY KEY AUTOINCREMENT,
    restaurant_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    descr TEXT NOT NULL,
    price REAL NOT NULL,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id),
    FOREIGN KEY (category_id) REFERENCES categorys(category_id)
)


"""



import sqlite3

# Подключаемся к базе данных (или создаем новую)
conn = sqlite3.connect('../samo_mag_bot.db')
cursor = conn.cursor()

# Создаем  таблицу, если она еще не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS  dishs (
    dish_id INTEGER PRIMARY KEY AUTOINCREMENT,
    restaurant_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    descr TEXT NOT NULL,
    price REAL NOT NULL,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id),
    FOREIGN KEY (category_id) REFERENCES categorys(category_id)
)

''')

# Сохраняем изменения в базе данных
conn.commit()

# Закрываем соединение с базой данных
conn.close()