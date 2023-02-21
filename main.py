from pprint import pprint
with open('recipes.txt', encoding='UTF-8') as file:
    cook_book = {}
    for line in file:
        dishes_name = line.strip()
        food_count = int(file.readline())
        food_list = []
        for element in range(food_count):
            numbers = file.readline().strip()
            ingredient_name, quantity, measure = numbers.split(' | ')
            food_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[dishes_name] = food_list
        file.readline()
# pprint(cook_book, sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    need_dishes = {}
    need_ingrid = {}
    for key, value in cook_book.items():
        if dishes == key:
            for element in value:
                for name, ingrid in element.items():
                    a = {name[ingrid]: {quantity[ingrid]}}
                return a
              # need_ingrid.setdefault[]
                # need_dishes.setdefault[name: ]
        # for name, ingrid in cook_book.items():
        #     if name == fucking_dish:
        #         print(ingrid)


print(get_shop_list_by_dishes('Омлет', 2))