import random
import datetime
import json

"""
Игра казино

Условия:
 - если есть деньги  - можешь инрать, елси нет - нужно ложить
 - если юзер захочет выйти  - предложить остаться (любые методы)
 - юзеру можно смотреть текущий счет
 - все игроки казино должны иметь имя и возраст
 - по выходу из казино данные об игроках записываются в файл (формат на выбор)
"""

"""
ITEMS       3       2       2 + XXX
------------------------------------
XXX         100     10      100
A           90      9       18
B           80      8       16
C           70      7       14
D           60      6       12
E           50      5       10
F           40      4       8
G           30      3       6
H           20      2       4
I           10      1       2
"""

wheel1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
wheel2 = wheel1  # Initialising wheel 2 and 3 by assigning the value of slot 1 to shorten and simplify code
wheel3 = wheel1
credit = 0
user_data = {'Name': "Ar",
             "Age": "10",
             'City': "Kharkiv",
             "Money": '2',
             'Date': 'time'
             }


def ask_user_name():  # Function for string name
    while True:
        try:
            user_name = str(input("Enter your name.\n"))
            if user_name.isdigit():
                raise ValueError
            break
        except ValueError:
            print('Please, input the str')
    return user_name


def ask_user_age():  # Function for int age
    while True:
        try:
            user_age = int(input("Enter your age.\n"))
            break
        except ValueError:
            print("Oh,No! Please enter a number")
    return user_age


def logout():  # Function for write data to json
    global user_data
    print("Before you go, please tell me about yourself ;)")
    user_data['Name'] = ask_user_name()
    user_data["Age"] = ask_user_age()
    user_data["City"] = str(input('Which city are you from?'))
    user_data["Money"] = credit
    date_now = datetime.datetime.now()
    user_data["Date"] = date_now.strftime("%Y-%m-%d %H:%M:%S")
    with open("user_data.json", "w") as f:
        json.dump(user_data, f, indent=4)


def start_spin():  # Function for start spin
    global credit
    choice1 = (random.choice(wheel1))
    choice2 = (random.choice(wheel2))
    choice3 = (random.choice(wheel3))
    print(choice1, choice2, choice3)
    choices = [choice1, choice2, choice3]
    if choices.count('XXX') == 3:
        credit = credit + 100
        print(f"You've won 100 credits, your credit is now {credit}")
    elif choices.count('A') == 3:
        credit = credit + 90
        print(f"You've won 90 credits, your credit is now {credit}")
    elif choices.count('B') == 3:
        credit = credit + 80
        print(f"You've won 80 credits, your credit is now {credit}")
    elif choices.count('C') == 3:
        credit = credit + 70
        print(f"You've won 70 credits, your credit is now {credit}")
    elif choices.count('D') == 3:
        credit = credit + 60
        print(f"You've won 60 credits, your credit is now {credit}")
    elif choices.count('E') == 3:
        credit = credit + 50
        print(f"You've won 50 credits, your credit is now {credit}")
    elif choices.count('F') == 3:
        credit = credit + 40
        print(f"You've won 40 credits, your credit is now {credit}")
    elif choices.count('G') == 3:
        credit = credit + 30
        print(f"You've won 30 credits, your credit is now {credit}")
    elif choices.count('H') == 3:
        credit = credit + 20
        print(f"You've won 20 credits, your credit is now {credit}")
    elif choices.count('I') == 3:
        credit = credit + 10
        print(f"You've won 10 credits, your credit is now {credit}")
    elif choices.count('XXX') == 2:
        credit = credit + 10
        print(f"You've won 10 credits, your credit is now {credit}")
    elif choices.count('A') == 2:
        credit = credit + 9
        print(f"You've won 9 credits, your credit is now {credit}")
    elif choices.count('B') == 2:
        credit = credit + 8
        print(f"You've won 8 credits, your credit is now {credit}")
    elif choices.count('C') == 2:
        credit = credit + 7
        print(f"You've won 7 credits, your credit is now {credit}")
    elif choices.count('D') == 2:
        credit = credit + 6
        print(f"You've won 6 credits, your credit is now {credit}")
    elif choices.count('E') == 2:
        credit = credit + 5
        print(f"You've won 5 credits, your credit is now {credit}")
    elif choices.count('F') == 2:
        credit = credit + 4
        print(f"You've won 4 credits, your credit is now {credit}")
    elif choices.count('G') == 2:
        credit = credit + 3
        print(f"You've won 3 credits, your credit is now {credit}")
    elif choices.count('H') == 2:
        credit = credit + 2
        print(f"You've won 2 credits, your credit is now {credit}")
    elif choices.count('I') == 2:
        credit = credit + 1
        print(f"You've won 1 credits, your credit is now {credit}")
    elif choices.count('A') == 2 and choices.count('XXX'):
        credit = credit + 18
        print(f"You've won 18 credits, your credit is now {credit}")
    elif choices.count('B') == 2 and choices.count('XXX'):
        credit = credit + 16
        print(f"You've won 16 credits, your credit is now {credit}")
    elif choices.count('C') == 2 and choices.count('XXX'):
        credit = credit + 14
        print(f"You've won 14 credits, your credit is now {credit}")
    elif choices.count('D') == 2 and choices.count('XXX'):
        credit = credit + 12
        print(f"You've won 12 credits, your credit is now {credit}")
    elif choices.count('E') == 2 and choices.count('XXX'):
        credit = credit + 10
        print(f"You've won 10 credits, your credit is now {credit}")
    elif choices.count('F') == 2 and choices.count('XXX'):
        credit = credit + 8
        print(f"You've won 8 credits, your credit is now {credit}")
    elif choices.count('G') == 2 and choices.count('XXX'):
        credit = credit + 6
        print(f"You've won 6 credits, your credit is now {credit}")
    elif choices.count('H') == 2 and choices.count('XXX'):
        credit = credit + 4
        print(f"You've won 4 credits, your credit is now {credit}")
    elif choices.count('I') == 2 and choices.count('XXX'):
        credit = credit + 2
        print(f"You've won 2 credits, your credit is now {credit}")
    else:
        print('You lost!')
        print("Credit = ", credit)


def credit_pass():  # Function for pass if user have enough money
    global credit
    while True:
        ask_user_credit = int(input('You should put your money on the account. Enter 1- Yes, 2-No\n'))
        if ask_user_credit == 1:
            while credit <= 0:
                credit = int(input(" Enter the amount you want to deposit \n"))
                if credit > 0:
                    return credit
        if ask_user_credit == 2:
            logout()
            print("Goodbye 😉 ")
            exit()
        else:
            pass


def spin_game(): # begin game
    global credit
    credit_pass()
    while True:
        spin = int(input("Let's play! Enter: 1- Spin, 2- Out, 3-show balance \n"))
        if spin == 2:
            if credit > 0:
                ask_again = int(input("Is it really time to go? "
                                      "How about a beer on the house and do new spin? 1-Yes, any number for No"))
                if ask_again == 1:
                    start_spin()
                else:
                    logout()
                    print("Goodbye 😉 ")
            else:
                credit_pass()
                logout()
                print("Goodbye 😉 ")
                break
        elif spin == 1:
            if credit > 0:
                credit = credit - 1
                # do the spins!
                start_spin()
            if credit <= 0:
                credit_pass()
        elif spin == 3:
            print("Credit = ", credit)
        elif credit == 0:
            credit_pass()
            break
        else:
            pass


spin_game()  # Try to play
