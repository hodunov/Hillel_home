"""
В этом файле есть функции, свзяанные и нет. Нужно по понять как  они работают, что за чем выполняется.
Лучше использовать дебагер в пайчаме
"""


# 1


def monitor(func_name, *args, **kwargs):
    with open('monitor.txt', 'a+') as file:
        res = func_name(*args, **kwargs)
        file.write(f'{res}')
        return res


def my_fun(arg1, arg2):
    return arg1 + arg2


print(monitor(my_fun, 1, 2))

# 2 Морсткой бой

import random
from prettytable import PrettyTable  # модуль для красивых табличек (pip install prettytable)

desk1 = [
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


def ships(players, bot):
    cord1, cord2 = None, None
    if bot:
        for _ in range(1, 3):
            try:
                cord1, cord2 = input(f'{players[0][1]} введите кординаты {_} коробля').split('-')
                cord1, cord2 = int(cord1), int(cord2)
            except ValueError as err:
                print(err)
            players[0][0][cord1][cord2] = 'K'
            players[1][0][random.randint(0, 9)][random.randint(0, 9)] = 'K'
    else:
        for player in players:
            for _ in range(1, 3):
                try:
                    cord1, cord2 = input(f'{player[1]} введите кординаты {_} коробля').split('-')
                    cord1, cord2 = int(cord1), int(cord2)
                except ValueError as err:
                    print(err)
                player[0][cord1][cord2] = 'K'


def shoot(coords_list, player):
    try:
        coord1, coord2 = coords_list
        coord1, coord2 = int(coord1), int(coord2)
    except ValueError:
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
        except IndexError:
            print('err')
        return 'Убил'
    else:
        return 'Мимо'


def check_loser(player):
    if ('K' in player[0]) or ('K' in player[1]) or ('K' in player[2]) or ('K' in player[3]) or ('K' in player[4]) or (
            'K' in player[5]) or ('K' in player[6]) or ('K' in player[7]) or ('K' in player[8]) or ('K' in player[9]):
        return False
    return True


def play_game():
    first_player = desk1
    second_player = desk2
    bot = input('Хотите включить бота?').lower() == 'y'
    players_list = [[first_player, 'first_player'], [second_player, 'second_player']]
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
        if bot:
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
        else:
            for player in players_list:
                print(player[0])
                coords_list = input(f'{player[1]}Введите кординаты[1-9]').split('-')
                if player[1] == 'first_player':
                    print(shoot(coords_list, players_list[1][0]))
                    if check_loser(players_list[1][0]):
                        return f'Win {player[1]}'
                else:
                    print(shoot(coords_list, players_list[0][0]))
                    if check_loser(players_list[0][0]):
                        return f'Win {player[1]}'


print(play_game())
