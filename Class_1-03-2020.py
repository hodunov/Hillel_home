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
import datetime
import random

wheel1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
wheel2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
wheel3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]


def game():
    choice1 = random.choice(wheel1)
    choice2 = random.choice(wheel2)
    choice3 = random.choice(wheel3)

def login():
    print('Welcome to HILLEL CASiNO')

    while True:
        play = input("Do you want to play game? Y or N")
        if play.lower() == "y":
            game()
        if play.lower() == 'n':
            play_out = input("damn. maybe still a batch? Y or N")
            if play_out.lower() == 'y':
                game()
            if play_out.lower() == 'n':
                logout()


print(login())


def user_data():
    credit = int(input('Do you have money on your balance?(y/n)'))
    if credit == 0:
        print('You need to pay. How much money do you want to give?')


def logout():
    user_name = str(input('Enter you name'))
    user_age = str(input('Enter you age'))
    user_money = int(input('How much money do you have?'))
    user_datetime = datetime.datetime.now()


while True:
    global credit
    spin = input("Spin? y/n?")
    if spin == "n":
        print(
            "Any money you have won has been wired to your bank account, don't ask how  we got your bank details just "
            "take the money and move on")
        print("Goodbye 😉 ")
        break
    elif spin == "y":
        credit = credit - 1
        print("Credit = ", credit)
        # do the spins!
        choice1 = random.choice(wheel1)
        choice2 = random.choice(wheel2)
        choice3 = random.choice(wheel3)
        print(choice1, choice2, choice3)
        if choice1 == "A" and choice2 == "A" and choice3 == "A":
            credit = credit + 90
            print("Tutti Fruitti!")
            print("You've won 15 credits, your credit is now", credit)


game()
