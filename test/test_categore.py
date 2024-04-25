


import bot_sql


str_1 = "Выберите ресторан от 1 до 4"
print(str_1)
id_rest = int(input("введите число "))
rows = bot_sql.get_categorys_for_restorany(id_rest)
print(rows)
print("  ")
count = 0
for row in rows:
    count = count + 1
    print(row)
print("count ")
print(count)
