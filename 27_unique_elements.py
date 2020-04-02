import random
import string

N = 1000
data = []

"""
Тут происходит наполнение списка данными
"""
for _ in range(N):
    data.append(int(random.choice(string.digits)))


"""
В списке будет 999 (в данном случае) объектов. 

ЗАДАЧА

Вывести унникальные элементы не нарушая их порядок. Решение должно работать не только для интов, а и для строк, флоат, 
тюплов. Идеальное решение в 2 строчки)))
"""
print("Our list looks like:", data)  # let's print our list for check

from more_itertools import unique_everseen  # pip install more_itertools
print("1 Method:", list(unique_everseen(data)))

unique = []  # Using new list
[unique.append(item) for item in data if item not in unique]
print("2 Method:", unique)

print("3 Method:", list(dict.fromkeys(data)))  # using dicts in Python 3.7+
