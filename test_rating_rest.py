import bot_sql
import sqlite3

class Curent:
    def __init__(self):
        self.id = -1


def sel_rest():
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    query = "SELECT * FROM restaurants"
    cursor.execute(query)
    rows = cursor.fetchall()  # Получаем все данные
    conn.close()
    for row in rows:
        print(row)


def sel_rating_rest():
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    query = "SELECT * FROM rating_rest"
    cursor.execute(query)
    rows = cursor.fetchall()  # Получаем все данные
    conn.close()
    for row in rows:
        print(row)



curent_rest = Curent()
print("curent_rest")
print(curent_rest.id)
curent_rest.id = 100
print(curent_rest.id)
curent_rest.id = -1
print(curent_rest.id)

a = 100/0
str_1 = """
1 распечатать restaurants   rating_rest
2 добавить рейтинг  добавляем в таблицу rating_rest строку  10,1,5
3 добавить рейтинг  добавляем в таблицу rating_rest строку  11,1,3
4 добавить рейтинг  добавляем в таблицу rating_rest строку  10,1,1
100  очистить таблицу рейтингов
"""
print(str_1)
val = int(input("введите число "))

if val == 1:
    sel_rest()
    sel_rating_rest()
elif val == 2:
    val = bot_sql.change_rating_rest(1, 10, 5)
    print("val")
    print(val)
elif val == 3:
    val = bot_sql.change_rating_rest(1, 11, 3)
    print("val")
    print(val)
elif val == 4:
    val = bot_sql.change_rating_rest(1, 10, 1)
    print("val")
    print(val)

elif val == 100:
    query1 = 'DELETE FROM rating_rest'
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query1)
    conn.commit()
    conn.close()
