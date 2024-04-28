import bot_sql
import os
import sqlite3


def sel_zakaz():
    print("sel_zakaz")
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    query = "SELECT * FROM zakaz"
    cursor.execute(query)
    rows = cursor.fetchall()  # Получаем все данные
    conn.close()
    for row in rows:
        print(row)

def sel_zakaz_dt():
    print("sel_zakaz_image")
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    query = "SELECT * FROM zakaz_image"
    cursor.execute(query)
    rows = cursor.fetchall()  # Получаем все данные
    conn.close()
    for row in rows:
        print(row)


def sel_zakaz_history():
    print("sel_zakaz_history")
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    query = "SELECT * FROM zakaz_history"
    cursor.execute(query)
    rows = cursor.fetchall()  # Получаем все данные
    conn.close()
    for row in rows:
        print(row)



def del_zakaz():
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    query = "DELETE FROM zakaz"
    cursor.execute(query)
    conn.commit()
    conn.close()

def del_zakaz_dt():
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    query = "DELETE FROM zakaz_image"
    cursor.execute(query)
    conn.commit()
    conn.close()



def del_zakaz_history():
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    query = "DELETE FROM zakaz_history"
    cursor.execute(query)
    conn.commit()
    conn.close()




str_1 = """
1 создать заказ
2 добавить 4 порции
3 добавить 1 порции товара 2
4 удалить блюдо 1
5 удалить блюдо 2
100  Показать все три таблицы заказов
101  Удалить  таблицы заказов
"""
print(str_1)
val = int(input("введите число "))


if val == 1:
    id_user = 1  # пользователь 1
    id_rest = 1  # Макдональс
    id_dish = 1  # Биг Спешиал цена 269
    kolvo = 3  # Колво должно быть больше 0
    # Для конкретного пользователя и по конкретному ресторану
    # Если есть заказ=Корзина то добавляется в него, иначе создается новый заказ со статусом корзина
    # Возвращает если все ошибка то кортеж ( "error", "Описание ошибки", )
    # Возвращает если все ок то кортеж ( "ok",  id_zakaz, )
    rez = bot_sql.sql_merge_zaraz(id_user, id_rest, id_dish, kolvo)
    print("rez")
    print(rez)
elif val == 2:
    id_user = 1  # пользователь 1
    id_rest = 1  # Макдональс
    id_dish = 1  # Биг Спешиал цена 269
    kolvo = 5  # Колво должно быть больше 0
    rez = bot_sql.sql_merge_zaraz(id_user, id_rest, id_dish, kolvo)
    print("rez")
    print(rez)
elif val == 3:
    id_user = 1  # пользователь 1
    id_rest = 1  # Макдональс
    id_dish = 2  # блюдо 2
    kolvo = 1  # Колво должно быть больше 0
    rez = bot_sql.sql_merge_zaraz(id_user, id_rest, id_dish, kolvo)
    print("rez")
    print(rez)
elif val == 4:
    id_user = 1  # пользователь 1
    id_rest = 1  # Макдональс
    id_dish = 1  # блюдо 1
    rez = bot_sql.sql_delete_dish_from_zaraz(id_user, id_rest, id_dish)
    print("rez")
    print(rez)
elif val == 5:
    id_user = 1  # пользователь 1
    id_rest = 1  # Макдональс
    id_dish = 2  # блюдо 1
    rez = bot_sql.sql_delete_dish_from_zaraz(id_user, id_rest, id_dish)
    print("rez")
    print(rez)


elif val == 100:
    sel_zakaz()
    sel_zakaz_dt()
    sel_zakaz_history()
elif val == 101:
    del_zakaz_dt()
    del_zakaz_history()
    del_zakaz()

