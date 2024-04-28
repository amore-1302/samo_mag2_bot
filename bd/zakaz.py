
"""
zakaz главная таблица заказов
Поля
zakaz_id   id заказа, он же номер заказа
dt  дата заказа, дата создания заказа
user_id id пользователя заказа
restaurant_id  - идентификатор ресторана, к которому относится заказ.
sum_all сумма всего заказа
payment_type   вид оплаты нал и БН
status   статус заказа стаусы строго определены в одной таблице


payment_types доп таблица хранит виды оплаты
payment_type_id  номер вида оплаты
name названме вида оплаты
всего две строки
строка 1:    1  нал
строка 2:    2  БН

status_s доп таблица хранит все возможные статусы заказов
status_id  номер статуса
name названме статуса


CREATE TABLE IF NOT EXISTS payment_types (
    payment_type_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)

CREATE TABLE IF NOT EXISTS status_s (
    status_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)



CREATE TABLE IF NOT EXISTS zakaz (
    zakaz_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dt TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    restaurant_id INTEGER NOT NULL,
    sum_all REAL  DEFAULT 0.0,
    payment_type INTEGER,
    status INTEGER NOT NULL,
    delivery_address TEXT ,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id),
    FOREIGN KEY (payment_type) REFERENCES payment_types(payment_type_id),
    FOREIGN KEY (status) REFERENCES status_s(status_id)
)

CREATE  INDEX IF NOT EXISTS   idx1_zakaz ON zakaz (user_id, dt)
CREATE  INDEX IF NOT EXISTS   idx2_zakaz ON zakaz (user_id, status)






"""



import sqlite3

conn = sqlite3.connect('../samo_mag_bot.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS payment_types (
    payment_type_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS status_s (
    status_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS zakaz (
    zakaz_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dt TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    restaurant_id INTEGER NOT NULL,
    sum_all REAL  DEFAULT 0.0,
    payment_type INTEGER,
    status INTEGER NOT NULL,
    delivery_address TEXT ,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id),
    FOREIGN KEY (payment_type) REFERENCES payment_types(payment_type_id),
    FOREIGN KEY (status) REFERENCES status_s(status_id)
)
''')

cursor.execute('''
CREATE  INDEX IF NOT EXISTS   idx1_zakaz ON zakaz (user_id, dt)
''')

cursor.execute('''
CREATE  INDEX IF NOT EXISTS   idx2_zakaz ON zakaz (user_id, status)
''')




# Сохраняем изменения в базе данных и закрываем соединение
conn.commit()
conn.close()