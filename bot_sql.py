import sqlite3
import datetime

# По   конкртному ресторано и категории возвращаем все блюда
# каждая строка id блюда и название блюда

def sql_get_all_review_rest(id_rest):
    param = (id_rest,)
    query = """SELECT *
        FROM review_rest
        WHERE restaurant_id = ?
        ORDER BY dt DESC
        """
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()

    cursor.execute(query, param)
    rows = cursor.fetchall()  # Получаем все данные
    conn.close()
    return rows


def add_review_rest(sq_user_id, rest_id, curent_review ):
    now_dt_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    param = (sq_user_id, rest_id, now_dt_time, curent_review,)
    query = 'INSERT INTO review_rest(user_id, restaurant_id, dt, name)  VALUES(?, ?, ?, ?)'

    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query, param)
    conn.commit()
    conn.close()



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


def sql_delete_dish_from_zaraz(id_user, id_rest, id_dish):
    param = (id_user, id_rest, 1,)  # 1 означает статусЗаказа = корзина
    query = """
            SELECT zakaz_id from zakaz
            WHERE user_id = ? and restaurant_id = ? and status_id = ? 
    """
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query, param)
    rows = cursor.fetchall()  # Получаем все данные
    conn.close()
    if len(rows) <= 0:
        rez = ("error", f"ОШИБКА сейчас нет в корзине заказа с пользователем = {id_user} и рестораном = {id_rest}")
        return rez

    row = rows[0]
    current_zakaz = row[0]

    param = (current_zakaz, id_dish, )
    query = """
            DELETE from zakaz_image
            WHERE zakaz_id = ? and dish_id = ? 
    """
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query, param)
    conn.commit()
    conn.close()

    return sql_match_summa_zakaz(current_zakaz)



def sql_match_summa_zakaz(current_zakaz):
    param = (current_zakaz,)
    query = """
            SELECT sum(sum_str) from zakaz_image
            WHERE   zakaz_id = ?  
    """
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query, param)
    row = cursor.fetchone()  # Получаем все данные
    conn.close()
    if row == None:
        current_summa = 0.0
    else:
        current_summa = row[0]
        if current_summa == None:
            current_summa = 0.0
        else:
            current_summa = round(current_summa, 2)

    param = (current_summa ,current_zakaz,)
    query = """
            UPDATE zakaz SET  sum_all = ?  
            WHERE   zakaz_id = ?  
    """
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query, param)
    conn.commit()
    conn.close()
    rez = ("ok", current_zakaz,)
    return rez




def sql_update_zakaz(current_zakaz, id_dish, add_kolvo, price):
    param = (current_zakaz, id_dish,)
    query = """
            SELECT zakaz_image_id, kolvo from zakaz_image
            WHERE   zakaz_id = ? AND  dish_id = ?  
    """
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query, param)
    row = cursor.fetchone()  # Получаем все данные
    conn.close()
    if row == None:
        curent_kolv0 = add_kolvo
        cur_summa_0 = curent_kolv0 * price
        cur_summa = round(cur_summa_0, 2)

        param = (current_zakaz,id_dish, curent_kolv0, price, cur_summa,)
        query = """
            INSERT INTO zakaz_image(zakaz_id, dish_id, kolvo, price, sum_str)  
            VALUES(?, ?, ?, ?, ?)  
        """
        conn = sqlite3.connect('./samo_mag_bot.db')
        cursor = conn.cursor()
        cursor.execute(query, param)
        conn.commit()
        conn.close()


    else:
        curent_zakaz_image_id = row[0]
        curent_kolv0 = row[1]
        curent_kolv0 = curent_kolv0 + add_kolvo
        cur_summa_0 = curent_kolv0 * price
        cur_summa = round(cur_summa_0, 2)

        param = (curent_kolv0, price, cur_summa, curent_zakaz_image_id,)

        query = """
            UPDATE zakaz_image  SET    kolvo = ?, price = ?, sum_str = ?  
            WHERE  zakaz_image_id = ?  
        """
        conn = sqlite3.connect('./samo_mag_bot.db')
        cursor = conn.cursor()
        cursor.execute(query, param)
        conn.commit()
        conn.close()

    return sql_match_summa_zakaz(current_zakaz)

def sql_new_zakaz(id_user, id_rest, id_dish, kolvo, price):
    cur_summa_0 = kolvo * price
    cur_summa = round(cur_summa_0, 2)
    now_dt_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    id_corzina = 1
    param = (now_dt_time, id_user, id_rest, cur_summa, id_corzina, "Самовывоз",)

    query = '''
    INSERT INTO zakaz(dt,user_id,restaurant_id, sum_all,status_id,delivery_address)
    VALUES(?,?,?,?,?,?) 
    '''

    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query, param)
    conn.commit()
    conn.close()


    param = (now_dt_time, id_user, id_rest,)
    query = '''
    SELECT zakaz_id  FROM zakaz
    WHERE dt = ? AND user_id = ? AND restaurant_id = ?  
    '''
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query, param)
    row = cursor.fetchone()  # Получаем все данные
    conn.close()
    if row == None:
        str1 = f"ОШИБКА не нашли блюда с id = {id_dish}"
        rez = ( "error", str1, )
        return rez

    new_id_zakaz = row[0]
    #print( f"new_id_zakaz = {new_id_zakaz}")
    param = (new_id_zakaz, id_dish,kolvo, price, cur_summa,)
    query = '''
    INSERT INTO zakaz_image(zakaz_id, dish_id, kolvo, price, sum_str)
    VALUES(?,?,?,?,?) 
    '''
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query, param)
    conn.commit()
    conn.close()

    param = (new_id_zakaz, now_dt_time, id_corzina,)
    query = '''
    INSERT INTO zakaz_history(zakaz_id, dt, status_id)
    VALUES(?,?,?) 
    '''
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query, param)
    conn.commit()
    conn.close()

    rez = ("ok", new_id_zakaz)
    return rez


def sql_merge_zaraz(id_user, id_rest, id_dish, kolvo):
    if kolvo <= 0:
        rez = ( "error", "При добавдении в заказ колво не может быть меньше равно 0", )
        return rez

    param = (id_dish ,)
    query = """
            SELECT price from dishs
            WHERE dish_id = ?  
    """
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query, param)
    row = cursor.fetchone()  # Получаем все данные
    conn.close()
    if row == None:
        str1 = f"ОШИБКА не нашли блюда с id = {id_dish}"
        rez = ( "error", str1, )
        return rez
    price = row[0]

    #    print(f"price = {price}")
    #    print(f"id_dish = {id_dish}")


    param = (id_user, id_rest, 1,)  # 1 означает статусЗаказа = корзина
    query = """
            SELECT zakaz_id from zakaz
            WHERE user_id = ? and restaurant_id = ? and status_id = ? 
    """
    conn = sqlite3.connect('./samo_mag_bot.db')
    cursor = conn.cursor()
    cursor.execute(query, param)
    rows = cursor.fetchall()  # Получаем все данные
    conn.close()
    if len(rows) <= 0:
        return sql_new_zakaz(id_user, id_rest, id_dish, kolvo, price)
    else:
        row = rows[0]
        current_zakaz = row[0]
        return sql_update_zakaz(current_zakaz, id_dish, kolvo, price)

