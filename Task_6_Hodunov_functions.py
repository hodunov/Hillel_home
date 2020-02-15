"""
1. Реализовать функцию squeezer, которая на вход принимает название фрукта и возвращает (ключевое слово return) строку
It is тут название фрукта juice. Ипользовать Ф-строки
"""


def squeezer():
    my_fruit = input('Enter fruit  ')
    return print(f"It's my {my_fruit} juice")


squeezer()

"""
2. Проапгрейдить функцию squeezer так, что бы она могла принимать несколько фруктов (смотреть про *args) и возвращала
строку It is тут название фрукта1, название фрукта2 juice

Тут можно почитать об args  - https://www.geeksforgeeks.org/args-kwargs-python/
"""


def squeezer_2():
    my_fruit_1 = input('Enter fruit  ')
    my_fruit_2 = input("Enter second fruit  ")
    return print(f"It's my {my_fruit_1} and {my_fruit_2} juice")


squeezer_2()

"""
3. Написать функцию которая принимает на вход число и возвращает True если число четное и False если не четное
"""

# Write your code here


# def even_number(number):
#     if number/2 ==0:
#         print(True)
#     else:
#         print(False)
#     return
#
#
# print(even_number(12))

"""
4. Написать функцию которая принимает на вход какой-то аргумент, приводит его к интеджеру и возвращает его. В случает
 ошибки выводит сообщение о том, что данный аргумент не может быть преведен к интеджеру и завершает программу 
 (встроенные функции quit() или exit())
"""


def output_int():
    try:
        return print(int(input('Enter any argument  ')))
    except Exception as exception:
        return exit(f"This argument can't be turned to int due to {exception}! Exit from program")


output_int()
"""
5. Переписать калькулятор на функцию для базовых операций (*, - , +, /) с ипользованием функции в задании выше
"""

# Write your code here
