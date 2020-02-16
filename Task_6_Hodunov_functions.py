"""
1. Реализовать функцию squeezer, которая на вход принимает название фрукта и возвращает (ключевое слово return) строку
It is тут название фрукта juice. Ипользовать Ф-строки
"""


def squeezer(my_fruit):
    return print(f"It's my {my_fruit} juice")


squeezer(input('Enter fruit  '))

print(input("Press ENTER for step 2"))

"""
2. Проапгрейдить функцию squeezer так, что бы она могла принимать несколько фруктов (смотреть про *args) и возвращала
строку It is тут название фрукта1, название фрукта2 juice

Тут можно почитать об args  - https://www.geeksforgeeks.org/args-kwargs-python/
"""


def squeezer_2(*my_fruit):
    return print(f"It's my {my_fruit} juice")


squeezer_2(input('Enter first fruit  '), input('Enter second fruit  '))

squeezer_2("banana", "orange", "apple")

print(input('Press Enter for STEP 3'))

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

print(input("Press ENTER for step 4"))

"""
4. Написать функцию которая принимает на вход какой-то аргумент, приводит его к интеджеру и возвращает его. В случает
 ошибки выводит сообщение о том, что данный аргумент не может быть преведен к интеджеру и завершает программу 
 (встроенные функции quit() или exit())
"""


def output_int(arg):
    try:
        return int(arg)
    except Exception as exception:
        exit(f"This argument can't be turned to int due to {exception}! Exit from program")


print(output_int(input('number  ')))
print(type(output_int(input('number  '))))

print(input('Press Enter for STEP 5'))

"""
5. Переписать калькулятор на функцию для базовых операций (*, - , +, /) с ипользованием функции в задании выше
"""

sing = input('Input the sign  ')
f_num = output_int(input('Input the first number   '))
s_num = output_int(input('Input the second number   '))
dev_sings = ('/', '//', '%')


def calc(operation, number1, number2):
    if operation == '+':
        print(number1 + number2)
    elif operation == '-':
        print(number1 - number2)
    elif operation in dev_sings and int(number2) == 0:
        print('Error: Division by zero!')
    elif operation == '//':
        print(number1 // number2)
    elif operation == '%':
        print(number1 % number2)
    elif operation == '/':
        print(number1 / number2)
    elif operation == '*':
        print(number1 * number2)
    else:
        print('Oops! Not valid operation!')


calc(sing, f_num, s_num)
