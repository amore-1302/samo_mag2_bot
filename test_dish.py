import bot_sql


str_1 = "Выберите ресторан от 1 до 4"
print(str_1)
id_rest = int(input("введите число "))

print("Категория 0 означает что блюда всех категорий")
str_1 = "Выберите категорию от 0 до 10"
id_category = int(input("введите число "))
print(str_1)

# строка имеет колонки id_блюда  название_блюда  цена  название категории
rows = bot_sql.get_dishs_for_categorys_and_restorany(id_rest, id_category)
print(rows)
print("  ")
count = 0
for row in rows:
    count = count + 1
    print(row)
print("count ")
print(count)