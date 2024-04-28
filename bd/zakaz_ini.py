

import sqlite3

def add_payment_types(payment_type_id, name):
    param = (payment_type_id,)
    #print("add_payment_types")
    query = "SELECT * FROM payment_types WHERE payment_type_id = ?"

    conn = sqlite3.connect('../samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query, param)
    #rows = cursor.fetchone()  # Получаем все данные
    rows = cursor.fetchall()  # Получаем все данные
    conn.close()

    if len(rows) > 0:
        return

    #print("123")
    param = (payment_type_id, name,)
    query = "INSERT INTO payment_types(payment_type_id, name ) VALUES (?,?)"
    conn = sqlite3.connect('../samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query, param)
    conn.commit()
    conn.close()




def sel_payment_types():
    print("payment_types")
    conn = sqlite3.connect('../samo_mag_bot.db')
    cursor = conn.cursor()
    query = "SELECT * FROM payment_types"
    cursor.execute(query)
    rows = cursor.fetchall()  # Получаем все данные
    conn.close()
    for row in rows:
        print(row)

def sel_status_s():
    print("status_s")
    conn = sqlite3.connect('../samo_mag_bot.db')
    cursor = conn.cursor()
    query = "SELECT * FROM status_s"
    cursor.execute(query)
    rows = cursor.fetchall()  # Получаем все данные
    conn.close()
    for row in rows:
        print(row)


def add_status_s(status_id, name):
    param = (status_id,)
    #print("add_payment_types")
    query = "SELECT * FROM status_s WHERE status_id = ?"

    conn = sqlite3.connect('../samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query, param)
    #rows = cursor.fetchone()  # Получаем все данные
    rows = cursor.fetchall()  # Получаем все данные
    conn.close()

    if len(rows) > 0:
        return

    #print("123")
    param = (status_id, name,)
    query = "INSERT INTO status_s(status_id, name ) VALUES (?,?)"
    conn = sqlite3.connect('../samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query, param)
    conn.commit()
    conn.close()

add_payment_types(1, "нал")
add_payment_types(2, "БН")
sel_payment_types()

add_status_s(1, "Корзина")
add_status_s(2, "Сформирован")
add_status_s(3, "БН_к_оплате")
add_status_s(4, "БН_оплачено")
add_status_s(5, "доставляется")
add_status_s(6, "Доставен")
add_status_s(7, "нал_к_оплате")
add_status_s(8, "нал_оплачено")
add_status_s(9, "Завершен")
add_status_s(100, "Отказ от заказа")

sel_status_s()

