''' Создание словаря из файла
со списком ингредиентов  '''

cook_book = {}
with open('ingredients.txt') as f:
    data_key = f.readline().rstrip()
    while data_key != '':
        cook_book.setdefault(data_key, [])
        data_len = f.readline().rstrip()
        # print(data_len)
        # print(data)
        for i in range(int(data_len)):
            data = f.readline().strip().split(' | ')
            if data == '':
                break
            dict_line = {'ingredient_name': data[0],
                         'quantity': data[1],
                         'measure': data[2]}
            cook_book[data_key] += [dict_line]
        data_key = f.readline().rstrip()
        data_key = f.readline().rstrip()

for key, value in cook_book.items():
    print(key)
    for val in value:
        print(val)
    print()


# with open('ingredients.txt') as f:
#     data = f.read()
#     print(data)
