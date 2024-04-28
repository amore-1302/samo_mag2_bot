import bot_sql
import sqlite3

def sel_review_rest():

    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    query = "SELECT * FROM review_rest"
    cursor.execute(query)
    rows = cursor.fetchall()  # Получаем все данные
    conn.close()
    for row in rows:
        print(row)


str_1 = """
1 распечатать отзывы реётинг ресторанов review_rest
2 добавить отзыв 1
3 добавить отзыв 2
4 добавить отзыв 3
100  очистить таблицу рейтингов
"""
print(str_1)
val = int(input("введите число "))

if val == 1:
    sel_review_rest()
elif val == 2:
    bot_sql.add_review_rest(10, 1, "Вкусно и точка первый озывst 1")
elif val == 3:
    bot_sql.add_review_rest(10, 1, "Вкусно и точка второй тестовый отзыв")
elif val == 4:
    bot_sql.add_review_rest(10, 1, "Вкусно и точка третий тестовый 333333333333333 отзыв")
elif val == 100:
    query1 = 'DELETE FROM review_rest'
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query1)
    conn.commit()
    conn.close()