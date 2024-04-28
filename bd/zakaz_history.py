"""
zakaz_history  истрия заказа - содержит историю изменений статусов заказа
Поля
zakaz_history_id   id строки этой таблицы
zakaz_id  ссылка на заказ
dt дата время когда произошло событие
status_id  id статуса из спец таблицы



CREATE TABLE   IF NOT EXISTS zakaz_history(
    zakaz_history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    zakaz_id INTEGER NOT NULL,
    dt TEXT  NOT NULL,
    status_id INTEGER NOT NULL,
    FOREIGN KEY (zakaz_id) REFERENCES zakaz(zakaz_id),
    FOREIGN KEY (status_id) REFERENCES status_s(status_id)
)

CREATE  INDEX IF NOT EXISTS   idx1_zakaz_history ON zakaz_history(zakaz_id,dt)



"""
import sqlite3

conn = sqlite3.connect('../samo_mag_bot.db')
cursor = conn.cursor()




cursor.execute('''
CREATE TABLE   IF NOT EXISTS zakaz_history(
    zakaz_history_id INTEGER PRIMARY KEY AUTOINCREMENT,
    zakaz_id INTEGER NOT NULL,
    dt TEXT  NOT NULL,
    status_id INTEGER NOT NULL,
    FOREIGN KEY (zakaz_id) REFERENCES zakaz(zakaz_id),
    FOREIGN KEY (status_id) REFERENCES status_s(status_id)
)
''')

cursor.execute('''
CREATE  INDEX IF NOT EXISTS   idx1_zakaz_history ON zakaz_history(zakaz_id,dt)
''')


# Сохраняем изменения в базе данных и закрываем соединение
conn.commit()
conn.close()
