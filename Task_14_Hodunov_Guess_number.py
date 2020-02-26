"""""
Нужно реализовать функциями. Одна функция сравнивает значения, другая отвечает за логику выполнения программы.
Диапазон 1 - 50
Если число юзера больше или меньше, то программа выводит сообщение больше это число или меньше
и предлагает ввести число снова.
Если число равно. то выводим сообщение о победе и завершаем работу программы
'"""
import random

target_number = random.randint(1, 50)

while True:
    try:
        your_number = int(input('Enter your number  '))
        break
    except ValueError:
        print("Not an integer! Please enter an integer")


def comparison(number):
    global target_number
    if number > target_number:
        print(f"Your guess was too high: Guess a number lower than {number}")
    if number < target_number:
        print(f"Your guess was too low: Guess a number higher than {number}")


def main_func():
    global target_number, your_number
    while your_number != target_number:
        comparison(your_number)
        while True:
            try:
                your_number = int(input('Enter your number again  '))
                break
            except ValueError:
                print("Not an integer! Please enter an integer")
    print('Congratulation You win!')


main_func()
