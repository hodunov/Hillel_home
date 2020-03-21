"""""
ТОDO-list
Написать класс, который позволит сохранить список дел, отмечать сделанное и показывать то, что нужно сделать.
Хранить список дел в json файле При запуске программы должна появится меню с вариантами действий: добавить в список,
вывести весь список, вывести список не сделанных дел, заполнить сделанное Заполнять "имя" дела можно только на 1
языке (любой на выбор, написать для этого регулярку) Для описания задания (дела) лучше использовать что-то типа
namedtuple или какой-то сторонний модуль, который поможет описать красиво или что-то кастомное (по желанию)
"""

def menu:
    menu_input = int(input('Choose number  '))
    if menu_input == 1:
        print("Добавить в список")

    if menu_input == 2:
        print("Вывести весь список")
    if menu_input == 3:
        print("Вывести список не сделанных дел")



import json

with open('questions.json', 'r') as file:
    json_data = json.load(file)
    for each in json_data['questions']:
        print(each["q"])
        each["answer"] = str(input("Your answer- "))
    with open('questions.json', 'w') as f:
        json.dump(json_data, f, indent=2)
