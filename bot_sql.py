import sqlite3

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

