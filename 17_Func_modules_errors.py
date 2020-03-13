"""
1.Написать функцию, которая выведет все пятницы 13-го в указаном году. Использовать можно все что прошли
"""
import calendar

my_year = 2012


def friday_13(year):
    start = 0
    for month in range(1, 13):
        for day in calendar.Calendar().itermonthdays2(year, month):
            if day[0] == 13 and day[1] == 4:
                start = start + 1
    return start


print(f"1. {my_year} has {friday_13(my_year)} Friday the 13ths")

"""
2.Реализовать функции min и max
Функции принимают 1 аргумент (list с числами) и возвращает максимальное/минимальное значение. Использовать сортировку нельзя.
"""


def min_max(x):
    minimum = maximum = x[0]
    for i in x[1:]:
        if i < minimum:
            minimum = i
        else:
            if i > maximum: maximum = i
    return minimum, maximum


user_list = [4, 8, 15, 16, 23, 42]
list_out = min_max(user_list)
print(f'2. Min and max on the list {user_list} are {" and ".join(str(e) for e in list_out)}')

"""
3.Написать функцию, которая принимает 1 аргумент — год, и возвращающую True, если год високосный, иначе False
"""


def year_is_leap(year):
    """year -> 1 if leap year, else 0."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# Alternative. Simpler


def is_leap(year):
    return calendar.isleap(year)


print(f"3.1. {my_year} is leap = {is_leap(my_year)}")
print(f"3.2. {my_year} is leap = {year_is_leap(my_year)}")
"""
4.Написать игру. 2 игрока бросают игровые кубики по 10 раз,

нужно определить кто выиграл и вывести результаты обоих игроков (суммы бросков).

Если у двух игроков за 1 ход выпало на кубиках одинаковое число, то игроки перебрасывают кубики.

(модуль random)
"""
from random import randrange

print("4. Cube game")

chances = 0
player_1 = 0
player_2 = 0
while chances < 10:
    sum1 = randrange(1, 6) + randrange(1, 6)
    sum2 = randrange(1, 6) + randrange(1, 6)
    if sum1 != sum2:
        chances += 1
        player_1 += sum1
        player_2 += sum2
    if not chances < 10:
        if player_1 > player_2:
            print(f" Win Player 1! \n Game score: \n Player 1: {player_1} \n Player 2: {player_2} \n ")
        if player_2 > player_1:
            print(f" Win Player 2! \n Game score: \n Player 1: {player_1} \n Player 2: {player_2} \n ")
        if player_2 == player_1:
            print(f" Tie score! \n Game score: \n Player 1: {player_1} \n Player 2: {player_2} \n ")

"""
5.Написать функцию для сортировки для данного списка словарей.

Сортировать по ключу `name`, если такого ключа нету в словаре, то по ключу `lastname`

data = [
    {'name': 'Bill', 'lastname': 'Boll'},
    {'name': 'Bob', 'lastname': 'Zip'},
    {'lastname': 'Fuf'},
    {'lastname': 'Albertus'},
    {'name': 'Dimon', 'lastname': 'Nomid'},
]

def sort_func(i):
    ...

data.sort(key=sort_func)
print(data.sort)
"""

print('5. Sort a list of dictionaries')
data = [
    {'name': 'Bill', 'lastname': 'Boll'},
    {'name': 'Bob', 'lastname': 'Zip'},
    {'lastname': 'Fuf'},
    {'lastname': 'Albertus'},
    {'name': 'Dimon', 'lastname': 'Nomid'}
]


def get_name(dictionary):
    """ Return the value of a key in a dictionary. """
    if 'name' in dictionary.values():
        return dictionary['name']
    else:
        return dictionary['lastname']


data.sort(key=get_name)
print(data)
