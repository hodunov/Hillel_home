"""
В этом файле есть функции, свзяанные и нет. Нужно по понять как  они работают, что за чем выполняется.
Лучше использовать дебагер в пайчаме
"""

# 1


def monitor(func_name, *args, **kwargs):  # функция принимает любые аргументы и функцию, что с ними делать
    with open('monitor.txt', 'a+') as file:
        res = func_name(*args, **kwargs)
        file.write(f'{res}')  # записывает результаты в отдельный тхт файл
        return res


def my_fun(arg1, arg2):  # функция что делать с аргументами
    return arg1 + arg2


print(monitor(my_fun, 1, 2))

# 2 Морсткой бой

import random
from prettytable import PrettyTable  # модуль для красивых табличек (pip install prettytable)

desk1 = [  # Таблицы для отображения полей
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
]
desk2 = [
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
]


def ships(players, bot):  # Функция для определения координат коралей
    cord1, cord2 = None, None  # Координаты не определены изначально
    if bot:  # Для бота
        for _ in range(1, 3):
            try:
                cord1, cord2 = input(f'{players[0][1]} введите кординаты {_} коробля').split('-')  # Ввод координат
                cord1, cord2 = int(cord1), int(cord2)  # Преобразование в int
            except ValueError as err:  # Обработка ошибки преобразования
                print(err)
            players[0][0][cord1][cord2] = 'K'
            players[1][0][random.randint(0, 9)][random.randint(0, 9)] = 'K'  # рандомное определение координат
    else:
        for player in players:  # для игрока аналогично
            for _ in range(1, 3):
                try:
                    cord1, cord2 = input(f'{player[1]} введите кординаты {_} коробля').split('-')
                    cord1, cord2 = int(cord1), int(cord2)
                except ValueError as err:
                    print(err)
                player[0][cord1][cord2] = 'K' # по введённым координатам


def shoot(coords_list, player):  # Функция выстрела
    try:
        coord1, coord2 = coords_list  # координаты
        coord1, coord2 = int(coord1), int(coord2)  # преобразования в int
    except ValueError:  # обработка ошибки ввода
        raise ValueError('AXAXAXAXAXAXAXAX')
    if player[coord1][coord2] == 'K':
        player[coord1][coord2] = '*'
        try:
            if player[coord1][coord2 + 1] == 'K':
                return 'Ранил'
            if player[coord1 + 1][coord2] == 'K':
                return 'Ранил'
            if player[coord1 + 1][coord2 + 1] == 'K':
                return 'Ранил'
            if player[coord1][coord2 - 1] == 'K':
                return 'Ранил'
            if player[coord1 - 1][coord2] == 'K':
                return 'Ранил'
            if player[coord1 - 1][coord2 - 1] == 'K':
                return 'Ранил'
            if player[coord1 - 1][coord2 + 1] == 'K':
                return 'Ранил'
            if player[coord1 + 1][coord2 - 1] == 'K':
                return 'Ранил'
        except IndexError:  # Обработка ошибок
            print('err')
        return 'Убил'
    else:
        return 'Мимо'


def check_loser(player):  # Функция для обработки выстрелов попал/не попал
    if ('K' in player[0]) or ('K' in player[1]) or ('K' in player[2]) or ('K' in player[3]) or ('K' in player[4]) or (
            'K' in player[5]) or ('K' in player[6]) or ('K' in player[7]) or ('K' in player[8]) or ('K' in player[9]):
        return False
    return True


def play_game():  # Основная логика
    first_player = desk1  # Рабочее поле
    second_player = desk2
    bot = input('Хотите включить бота?').lower() == 'y'  # Добавил бы подсказку что вводить и обработку ошибок
    players_list = [[first_player, 'first_player'], [second_player, 'second_player']] # Список игороков
    ships(players_list, bot)
    while True:
        print(f'{players_list[0][0][0]}  {players_list[1][0][9]} \n')
        print(f'{players_list[0][0][1]} {players_list[1][0][1]} \n')
        print(f'{players_list[0][0][2]} {players_list[1][0][2]} \n')
        print(f'{players_list[0][0][3]} {players_list[1][0][3]} \n')
        print(f'{players_list[0][0][4]} {players_list[1][0][4]} \n')
        print(f'{players_list[0][0][5]} {players_list[1][0][5]} \n')
        print(f'{players_list[0][0][6]} {players_list[1][0][6]} \n')
        print(f'{players_list[0][0][7]} {players_list[1][0][7]} \n')
        print(f'{players_list[0][0][8]} {players_list[1][0][8]} \n')
        print(f'{players_list[0][0][9]} {players_list[1][0][9]} \n')
        if bot:  # условие для бота
            for player in players_list:
                if player[1] == 'first_player':
                    coords_list = input(f'{player[1]}Введите кординаты[1-9]').split('-')
                    print(shoot(coords_list, players_list[1][0]))
                    if check_loser(players_list[1][0]):
                        return f'Win {player[1]}'
                else:
                    coords_list = [random.randint(0, 9), random.randint(0, 9)]
                    print(f'Бот походил:{shoot(coords_list, players_list[0][0])}')
                    if check_loser(players_list[0][0]):
                        return f'Win {player[1]}'
        else:  # Условие игрока
            for player in players_list:
                print(player[0])
                coords_list = input(f'{player[1]}Введите кординаты[1-9]').split('-')  # Ввод координат
                if player[1] == 'first_player':
                    print(shoot(coords_list, players_list[1][0]))
                    if check_loser(players_list[1][0]):
                        return f'Win {player[1]}'
                else:
                    print(shoot(coords_list, players_list[0][0]))
                    if check_loser(players_list[0][0]):
                        return f'Win {player[1]}'


print(play_game())
