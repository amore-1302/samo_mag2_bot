"""
review_rest таблица отзывов о ресторане
Поля
review_rest_id  id отзыва
user_id  id пользователя кто сделал отзыв
restaurant_id  id ресторана о котором  натисан отзыв
dt дата в формате гггг-мм-дд:чч:мм
descr сам отзыв



CREATE TABLE review_rest (
    review_rest_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    restaurant_id INTEGER NOT NULL,
    dt TEXT  NOT NULL,
    name TEXT  NOT NULL,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
)

CREATE  INDEX idx_review_rest_dt ON review_rest (dt)
CREATE  INDEX idx1_review_rest_dt ON review_rest (restaurant_id,dt)

"""


import sqlite3

# Подключаемся к базе данных (или создаем новую)
conn = sqlite3.connect('../samo_mag_bot.db')
cursor = conn.cursor()

# Создаем  таблицу, если она еще не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS review_rest (
    review_rest_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    restaurant_id INTEGER NOT NULL,
    dt TEXT  NOT NULL,
    name TEXT  NOT NULL,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
''')

# Создаем уникальный индекс на поле dt
cursor.execute('''
CREATE  INDEX IF NOT EXISTS  idx_review_rest_dt ON review_rest (dt)
''')

cursor.execute('''
CREATE  INDEX IF NOT EXISTS   idx1_review_rest_dt ON review_rest (restaurant_id,dt)
''')


# Сохраняем изменения в базе данных и закрываем соединение
conn.commit()
conn.close()