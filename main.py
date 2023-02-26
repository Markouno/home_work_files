from pprint import pprint
import time
def read_file(): # Читаем тексты
    with open('recipes.txt', encoding='UTF-8') as file:
        cook_book = {}
        for line in file:
            dishes_name = line.strip()
            food_count = int(file.readline())
            food_list = []
            for _ in range(food_count):
                numbers = file.readline().strip()
                ingredient_name, quantity, measure = numbers.split(' | ')
                food_list.append(
                    {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
                    )
            cook_book[dishes_name] = food_list
            file.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count): # Функция для расчета ингридов на кол-во персон
    start = time.time()
    cook_book = read_file()
    dishes_dict = {}
    for dish in dishes:
        for element in cook_book[dish]:
            if element['ingredient_name'] not in dishes_dict:
                dishes_dict[element['ingredient_name']] = {'measure': element['measure'], 'quantity': int(element['quantity']) * person_count}
            else:
                dishes_dict[element['ingredient_name']]['quantity'] += int(element['quantity']) * person_count 
    return dishes_dict


def read_fuckings_files(txt_list): # Читаем файлики и записываем их по кол-ву строк в новый файл, ю ноу...
    txt_dict = {}
    ready_txt = open('final_text.txt', 'w', encoding='UTF-8')
    for book in txt_list:
        with open(book, encoding='UTF-8') as file:
            counter = 0
            for line in file:
                counter += 1
            txt_dict[book] = counter           
    for key, value in sorted(txt_dict.items(), key=lambda p: p[1]):
        ready_txt.writelines(f'{key}\n{value}\n')
        for line in open(key, encoding='UTF-8'):
            ready_txt.writelines(line)
        ready_txt.writelines('\n')
    ready_txt.close()

read_fuckings_files(['1.txt', '2.txt', '3.txt'])
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Жаренная картошка'], 2))
