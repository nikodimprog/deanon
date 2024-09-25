import os
from banner import banner
from pystyle import *


# Database Path
database_file = 'interbase.csv'  # enter name base

#example C:\\Users\\nikodimprog\\Desktop\\Financial Ghost Team\\interbase.csv

# Color code
color_code = {
    "reset": "\033[0m",  
    "underline": "\033[04m", 
    "green": "\033[32m",     
    "yellow": "\033[93m",    
    "red": "\033[31m",       
    "cyan": "\033[36m",     
    "bold": "\033[01m",        
    "pink": "\033[95m",
    "url_l": "\033[36m",       
    "li_g": "\033[92m",      
    "f_cl": "\033[0m",
    "dark": "\033[90m",     
}

# Очистка экрана
os.system("clear")
os.system("cls")

# Функция для поиска совпадений в базе данных
def get_information(database_file, search_value):
    matches = []
    
    with open(database_file, 'r', encoding='utf-8') as file:
        for line in file:
            if search_value.lower() in line.lower():  # Поиск без учёта регистра
                matches.append(line.strip())  # Добавляем строку в список совпадений

    if matches:
        print(f'{color_code["green"]}Найдено совпадений: {len(matches)}{color_code["reset"]}')
        for match in matches:
            print(f'{color_code["cyan"]}[⋗] {color_code["yellow"]}{match}{color_code["reset"]}')
    else:
        print(f'{color_code["red"]}Совпадений не найдено.{color_code["reset"]}')


# Отображение баннера и выбор пользователя
alignment = "{:>50}".format(banner)
colored_banner = Colorate.Vertical(Colors.yellow_to_red, alignment)
print(colored_banner)

select = input(f'{color_code["yellow"]}[%]{color_code["yellow"]} Выбрать:{color_code["yellow"]} ')

if select == '1':
    search_value = input(f'{color_code["yellow"]}[?]{color_code["yellow"]} введите номер телефона (в формате +79999999999) >{color_code["yellow"]} ')
    if search_value.isalpha():
        print(f'{color_code["cyan"]}[⋗] {color_code["yellow"]} Введите числовое значение.{color_code["yellow"]} ')
    else:
        get_information(database_file, search_value)

if select == '2':
    search_value = input(f'{color_code["cyan"]}[⋗] {color_code["bold"]} введите ФИО{color_code["yellow"]} ')
    if search_value.isdigit():
        print(f'{color_code["cyan"]}[⋗] {color_code["yellow"]} Используйте только слова.{color_code["yellow"]} ')
    else:
        get_information(database_file, search_value)
    os.system("pause")

if select == '3':
    search_value = input(f'{color_code["cyan"]}[⋗] {color_code["yellow"]} введите ИНН >{color_code["yellow"]} ')
    if search_value.isalpha():
        print(f'{color_code["cyan"]}[⋗] {color_code["yellow"]} Введите числовое значение.{color_code["yellow"]} ')
    else:
        get_information(database_file, search_value)
    os.system("pause")

if select == '4':
    search_value = input(f'{color_code["cyan"]}[⋗] {color_code["yellow"]} введите адрес >{color_code["yellow"]} ')
    get_information(database_file, search_value)
    os.system("pause")

if select == '5':
    search_value = input(f'{color_code["cyan"]}[⋗] {color_code["yellow"]} введите СНИЛЛС >{color_code["yellow"]} ')
    if search_value.isalpha():
        print(f'{color_code["cyan"]}[⋗] {color_code["yellow"]} Введите числовое значение.{color_code["yellow"]} ')
    else:
        get_information(database_file, search_value)
    os.system("pause")

if select == '6':
    search_value = input(f'{color_code["cyan"]}[⋗] {color_code["yellow"]} введите известное вам имущество  >{color_code["yellow"]} ')
    get_information(database_file, search_value)
    os.system("pause")

elif select == '10':
    print("[$] слив by tg @nikodimprog")

elif select == '99':
    print("досвидос.")
