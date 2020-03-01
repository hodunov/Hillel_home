import random
import time
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
# Set up the wheels of the slot machine

wheel1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]

# Initialising wheel 2 and 3 by assigning the value of slot 1 to shorten and simplify code

wheel2 = wheel1
wheel3 = wheel1

# Initialise credit and start game
credit = 100
print("Welcome to Hillel's Casino.")
print("Current credit is", credit)
time.sleep(2)
print("Remember each go costs one credit")
print("And remember, when the fun stops, STOP")
time.sleep(2)
print("Good luck!")

# begin play
while True:
    spin = input("Spin? y/n?")
    if spin == "n":
        print("Goodbye 😉 ")
        break
    elif spin == "y":
        credit = credit - 1
        print("Credit = ", credit)
        # do the spins!
        choice1 = (random.choice(wheel1))
        choice2 = (random.choice(wheel2))
        choice3 = (random.choice(wheel3))
        print(choice1, choice2, choice3)
        choices = [choice1, choice2, choice3]
        if choices.count('A') == 3:

        if choice1 == "A" and choice2 == "A" and choice3 == "A":
            credit = credit + 90
            print(f"You've won 90 credits, your credit is now", credit)
        elif choice1 == "B" and choice2 == "B" and choice3 == "B":
            credit = credit + 90
            print(f"You've won 90 credits, your credit is now", credit)
        elif choice1 == "C" and choice2 == "C" and choice3 == "C":
            credit = credit + 90
            print(f"You've won 90 credits, your credit is now", credit)
        elif choice1 == "A" and choice2 == "A" and choice3 == "A":
            credit = credit + 90
            print(f"You've won 90 credits, your credit is now", credit)
        elif choice1 == "A" and choice2 == "A" and choice3 == "A":
            credit = credit + 90
            print(f"You've won 90 credits, your credit is now", credit)


        elif choice1 == "🍉" and choice2 == "🍉" and choice3 == "🍉":
            print("Wow, triple watermelon!")
            print("You've won a voucher for 3 free fruity themed drinks from the casino bar🍹")
        elif choice1 == choice2:
            print("ooh")
        elif choice1 == choice3:
            print("ooh")
        elif choice3 == choice2:
            print("ooh")
        else:
            print("too bad")
        if credit == 0:
            print("GET OUT OF MY CASINO!")
            break
