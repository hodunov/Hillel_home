"""
1. Реализовать функцию squeezer, которая на вход принимает название фрукта и возвращает (ключевое слово return) строку
It is тут название фрукта juice. Ипользовать Ф-строки
"""


def squeezer(my_fruit):
    return print(f"It's my {my_fruit} juice")


squeezer(input('Enter fruit  '))

"""
2. Проапгрейдить функцию squeezer так, что бы она могла принимать несколько фруктов (смотреть про *args) и возвращала
строку It is тут название фрукта1, название фрукта2 juice

Тут можно почитать об args  - https://www.geeksforgeeks.org/args-kwargs-python/
"""


def squeezer_2(*my_fruit):
    return print(f"It's my {my_fruit} juice")


squeezer_2(input('Enter first fruit  '), input('Enter second fruit  '))

squeezer_2("banana", "orange", "apple")


"""
3. Написать функцию которая принимает на вход число и возвращает True если число четное и False если не четное
"""


def even_number(number):
    if number % 2 == 0:
        print(True)
    else:
        print(False)
    return


even_number(int(input("Enter any number  ")))

"""
4. Написать функцию которая принимает на вход какой-то аргумент, приводит его к интеджеру и возвращает его. В случает
 ошибки выводит сообщение о том, что данный аргумент не может быть преведен к интеджеру и завершает программу 
 (встроенные функции quit() или exit())
"""


def output_int():
    try:
        value = int(input("Type a number:"))
        return value
    except Exception as exception:
        exit(f"This argument can't be turned to int due to {exception}! Exit from program")


print(type(output_int()))
"""
5. Переписать калькулятор на функцию для базовых операций (*, - , +, /) с ипользованием функции в задании выше
"""

sing = input('Input the sign  ')
f_num = input('Input the first number   ')
s_num = input('Input the second number   ')
dev_sings = ('/', '//', '%')
if f_num.isdigit() and s_num.isdigit():
    f_num = int(f_num)
    s_num = int(s_num)
    if sing == '+':
        print(f_num + s_num)
    elif sing == '-':
        print(f_num - s_num)
    elif sing in dev_sings and int(s_num) == 0:
        print('Error: Division by zero!')
    elif sing == '//':
        print(f_num // s_num)
    elif sing == '%':
        print(f_num % s_num)
    elif sing == '/':
        print(f_num / s_num)
    elif sing == '*':
        print(f_num * s_num)
    else:
        print('Oops! Not valid operation!')
else:
    print('Hey Hey Bad News! One of the numbers is not a digit...')

