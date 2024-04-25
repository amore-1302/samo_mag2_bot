import sqlite3

# По конкртному ресторано и категории возвращаем все блюда
# каждая строка id блюда и название блюда
def get_dishs_for_categorys_and_restorany( rest_id , category_id):
    if category_id > 0:
        param = (rest_id, category_id,)
        query = """SELECT 
        t1.dish_id, t1.name, t1.price, t2.name 
        FROM dishs t1
        INNER JOIN categorys t2 ON t1.category_id = t2.category_id 
        WHERE t1.restaurant_id = ?
        AND t1.category_id = ?
        ORDER BY t1.dish_id
        """
    else:
        param = (rest_id, )
        query = """SELECT 
        t1.dish_id, t1.name, t1.price, t2.name  
        FROM dishs t1
        INNER JOIN categorys t2 ON t1.category_id = t2.category_id 
        WHERE t1.restaurant_id = ?
        ORDER BY t2.sort, t1.dish_id
        """

    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()

    cursor.execute(query, param)
    rows = cursor.fetchall()  # Получаем все данные
    conn.close()
    return rows



# По конкртному ресторано возвращаем все категории. каждая строка id категории и название ее
def get_categorys_for_restorany( rest_id ):
    param = (rest_id,)
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    query = """SELECT DISTINCT  t2.category_id, t2.name FROM dishs t1
        INNER JOIN categorys t2 ON t1.category_id = t2.category_id 
        WHERE t1.restaurant_id = ?
        ORDER BY t2.sort
        """
    cursor.execute(query, param)
    rows = cursor.fetchall()  # Получаем все данные
    conn.close()
    return rows

def get_id_user( user_struct ):

    telega_user_id = user_struct.id
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()

    cursor.execute('SELECT user_id FROM users WHERE telega_id=?', (telega_user_id,))
    user = cursor.fetchone()
    conn.close()

    if user:
        # возвращаем user_id из sqlite
        return user[0]

    user_first_name = user_struct.first_name  # Имя пользователя
    user_username = '@'+ user_struct.username  # Ник пользователя в Telegram (может быть None)
    cortege = (telega_user_id, user_username, user_first_name,)


    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (telega_id, telega_url, name) VALUES (?, ?, ?)',cortege  )
    conn.commit()
    conn.close()

    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()

    cursor.execute('SELECT user_id FROM users WHERE telega_id=?', (telega_user_id,))
    user = cursor.fetchone()
    conn.close()
    return user[0]

def sql_list_rest():
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    query = "SELECT * FROM restaurants"
    cursor.execute(query)
    rows = cursor.fetchall()  # Получаем все данные
    conn.close()
    return rows

