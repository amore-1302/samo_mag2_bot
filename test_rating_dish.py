import bot_sql
import sqlite3

def sel_dishs():
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    query = "SELECT * FROM dishs"
    cursor.execute(query)
    rows = cursor.fetchall()  # Получаем все данные
    conn.close()
    for row in rows:
        print(row)


def sel_rating_dishs():
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    query = "SELECT * FROM rating_dish"
    cursor.execute(query)
    rows = cursor.fetchall()  # Получаем все данные
    conn.close()
    for row in rows:
        print(row)


str_1 = """
1 распечатать  dishs rating_dish
2 добавить рейтинг  добавляем в таблицу rating_rest строку  10,1,5
3 добавить рейтинг  добавляем в таблицу rating_rest строку  11,1,3
4 добавить рейтинг  добавляем в таблицу rating_rest строку  10,1,1
100  очистить таблицу рейтингов блюд
"""
print(str_1)
val = int(input("введите число "))

if val == 1:
    sel_dishs()
    sel_rating_dishs()
elif val == 2:
    val = bot_sql.change_rating_dish(1, 10, 5)
    print("val")
    print(val)
elif val == 3:
    val = bot_sql.change_rating_dish(1, 11, 3)
    print("val")
    print(val)
elif val == 4:
    val = bot_sql.change_rating_dish(1, 10, 1)
    print("val")
    print(val)

elif val == 100:
    query1 = 'DELETE FROM rating_dish'
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query1)
    conn.commit()
    conn.close()
