import sqlite3

# По   конкртному ресторано и категории возвращаем все блюда
# каждая строка id блюда и название блюда

def all_rating_rest(id_rest):
    param = (id_rest,)
    query = """SELECT  AVG(rating)
        FROM rating_rest
        WHERE restaurant_id = ?
        """

    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()

    cursor.execute(query, param)
    rows = cursor.fetchone()  # Получаем все данные
    conn.close()
    if len(rows) <= 0:
        new_rating = 0
    else:
        new_rating_0 = rows[0]
        new_rating = round(new_rating_0, 2)

    param = (new_rating, id_rest,)
    query = """UPDATE restaurants set raiting = ? 
            WHERE restaurant_id = ?
            """
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query, param)
    conn.commit()
    conn.close()
    return new_rating

def change_rating_rest(id_rest, id_user, new_rating):
    if new_rating > 0:
        param = (id_rest, id_user,)
        query = """SELECT 
        t1.restaurant_id 
        FROM rating_rest t1
        WHERE t1.restaurant_id = ?
        AND t1.user_id = ?
        """
        conn = sqlite3.connect('./samo_mag_bot.db')
        cursor = conn.cursor()

        cursor.execute(query, param)
        rows = cursor.fetchall()  # Получаем все данные
        conn.close()

        if len(rows) > 0:
            param = (new_rating, id_rest, id_user,)
            query = """UPDATE rating_rest set rating = ? 
            WHERE restaurant_id = ?
            AND user_id = ?
            """
            conn = sqlite3.connect('./samo_mag_bot.db')
            cursor = conn.cursor()

            cursor.execute(query, param)
            conn.commit()
            conn.close()
        else:
            param = (id_user, id_rest, new_rating,)

            query = 'INSERT INTO rating_rest(user_id, restaurant_id, rating )  VALUES(?, ?, ?)'

            conn = sqlite3.connect('./samo_mag_bot.db')
            cursor = conn.cursor()
            cursor.execute(query, param)
            conn.commit()
            conn.close()
    else:
        param = ( id_rest, id_user,)
        query = """DELETE FROM  rating_rest 
            WHERE restaurant_id = ?
            AND user_id = ?
            """
        conn = sqlite3.connect('./samo_mag_bot.db')
        cursor = conn.cursor()

        cursor.execute(query, param)
        conn.commit()
        conn.close()


    # расчитываем общий рейтинг ресторана
    return all_rating_rest(id_rest)

def all_rating_dish(id_dish):
    param = (id_dish,)
    query = """SELECT  AVG(rating)
        FROM rating_dish
        WHERE dish_id = ?
        """

    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()

    cursor.execute(query, param)
    rows = cursor.fetchone()  # Получаем все данные
    conn.close()
    if len(rows) <= 0:
        new_rating = 0
    else:
        new_rating_0 = rows[0]
        new_rating = round(new_rating_0, 2)

    param = (new_rating, id_dish,)
    query = """UPDATE dishs set raiting = ? 
            WHERE dish_id = ?
            """
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query, param)
    conn.commit()
    conn.close()
    return new_rating

def change_rating_dish(id_dish, id_user, new_rating):

    if new_rating > 0:
        param = (id_dish, id_user,)
        query = """SELECT 
        t1.dish_id 
        FROM rating_dish t1
        WHERE t1.dish_id = ?
        AND t1.user_id = ?
        """
        conn = sqlite3.connect('./samo_mag_bot.db')
        cursor = conn.cursor()

        cursor.execute(query, param)
        rows = cursor.fetchall()  # Получаем все данные
        conn.close()

        if len(rows) > 0:
            param = (new_rating, id_dish, id_user,)
            query = """UPDATE rating_dish set rating = ? 
            WHERE dish_id = ?
            AND user_id = ?
            """
            conn = sqlite3.connect('./samo_mag_bot.db')
            cursor = conn.cursor()

            cursor.execute(query, param)
            conn.commit()
            conn.close()
        else:
            param = (id_user, id_dish, new_rating,)

            query = 'INSERT INTO rating_dish(user_id, dish_id, rating )  VALUES(?, ?, ?)'
            conn = sqlite3.connect('./samo_mag_bot.db')
            cursor = conn.cursor()
            cursor.execute(query, param)
            conn.commit()
            conn.close()
    else:
        param = ( id_dish, id_user,)
        query = """DELETE FROM  rating_dish 
            WHERE dish_id = ?
            AND user_id = ?
            """
        conn = sqlite3.connect('./samo_mag_bot.db')
        cursor = conn.cursor()

        cursor.execute(query, param)
        conn.commit()
        conn.close()


    # расчитываем общий рейтинг ресторана
    return all_rating_dish(id_dish)




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

def get_from_telega_user_id_id_user( telega_user_id ):
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


def sql_get_one_rest(id_rest):
    nabor = ( id_rest, )
    query = "SELECT * FROM restaurants WHERE restaurant_id = ?"
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query, nabor )
    rows = cursor.fetchone()  # Получаем все данные
    conn.close()
    return rows

