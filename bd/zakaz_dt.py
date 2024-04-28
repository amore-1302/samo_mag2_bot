"""
zakaz_image  расшифровка заказа - содержит блюда конкретного заказа
Поля
zakaz_image_id   id строки заказа
zakaz_id  ссылка на заказ
dish_id id блюда в строке заказа
kolvo в строке заказа
price цена блюда в строке заказа
sum в строке заказа

CREATE TABLE   IF NOT EXISTS zakaz_image(
    zakaz_image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    zakaz_id INTEGER NOT NULL,
    dish_id INTEGER  NOT NULL,
    kolvo INTEGER  NOT NULL,
    price REAL NOT NULL,
    sum_str REAL NOT NULL,
    FOREIGN KEY (zakaz_id) REFERENCES zakaz(zakaz_id),
    FOREIGN KEY (dish_id) REFERENCES dishs(dish_id)
)



"""


import sqlite3


conn = sqlite3.connect('../samo_mag_bot.db')
cursor = conn.cursor()




cursor.execute('''
CREATE TABLE   IF NOT EXISTS zakaz_image(
    zakaz_image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    zakaz_id INTEGER NOT NULL,
    dish_id INTEGER  NOT NULL,
    kolvo INTEGER  NOT NULL,
    price REAL NOT NULL,
    sum_str REAL NOT NULL,
    FOREIGN KEY (zakaz_id) REFERENCES zakaz(zakaz_id),
    FOREIGN KEY (dish_id) REFERENCES dishs(dish_id)    
)
''')




# Сохраняем изменения в базе данных и закрываем соединение
conn.commit()
conn.close()