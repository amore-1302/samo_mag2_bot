"""
в restaurants  таблица ресторанов
добавляем столбец  raiting REAL если он там не существует


ALTER TABLE restaurants ADD COLUMN  raiting REAL


"""


import sqlite3


# Подключаемся к базе данных (или создаем новую)
conn = sqlite3.connect('../samo_mag_bot.db')
cursor = conn.cursor()

# Получаем информацию о таблице
table_name = "restaurants"
column_name = 'raiting'
cursor.execute(f"PRAGMA table_info({table_name})")
columns = cursor.fetchall()
if column_name not in [col[1] for col in columns]:
    print("Добавляем столбец " + column_name)
    # Сохраняем изменения в базе данных и закрываем соединение
    cursor.execute('ALTER TABLE restaurants ADD COLUMN  raiting REAL')
    conn.commit()

conn.close()