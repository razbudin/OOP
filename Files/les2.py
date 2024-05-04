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


def get_shop_list_by_dishes(dishes, person_count):
    ''' Функция для создания словаря необходимых продуктов
    на указонное количество человек'''
    cook_for_person = {}
    for dish in dishes:
        if cook_book.get(dish) is None:
            print(f'Блюда {dish}, нет в списке рецептов')
            print()
        else:
            dish_list = cook_book.get(dish)
            for li in dish_list:
                ingredients = li.get('ingredient_name')
                measure = li.get('measure')
                quantity = int(li.get('quantity')) * person_count
                if cook_for_person.get(ingredients) is None:
                    cook_for_person[ingredients] = {
                        'measure': measure,
                        'quantity': quantity}
                else:
                    cook_for_person[ingredients]['quantity'] += quantity
    return cook_for_person


ingredients_dishes = get_shop_list_by_dishes(
    ['Омлет', 'Запеченный картофель', 'Ципленок табака'], 2)

for key, value in ingredients_dishes.items():
    print(key)
    print(value)
