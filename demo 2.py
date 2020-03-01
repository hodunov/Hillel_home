import random
import time

# Set up the Slots of the fruit machine

slot1 = ["🥞", "🍒", "🍒", "🍒", "🍒", "🥑", "🥑", "🌽", "🌽", "🥜", "🥜", "🍉", "🍉", "🍓", "🍓"]

# Initialising slot 2 and 3 by assigning the value of slot 1 to shorten and simplify code

slot3 = slot1
slot2 = slot1

# Initialise credit and start game
credit = 100
print("Welcome to Jasmine's Casino.")
print("Current credit is", credit)
time.sleep(2)
print("Today we have a jackpot of 2500 credits, all of you have to do is get 🥞🥞🥞")
print("If you get 🍓🍉 🍒your credit will increase by 15")
time.sleep(2)
print("If you get  🍉 🍉 🍉you win a voucher for 3 free fruity themed drinks from the casino bar🍹")
time.sleep(2)
print("If you get 🥑🥑🥑 your credit will increase by  10")
time.sleep(2)
print("If you get  🍒  🍒  🍒 your credit will increase by  5")
time.sleep(3)
print("Remember each go costs one credit")
print("And remember, when the fun stops, STOP")
time.sleep(2)
print("Good luck!")

# begin play
while True:
    spin = input("Spin? y/n?")
    if spin == "n":
        print(
            "Any money you have won has been wired to your bank account, don't ask how  we got your bank details just take the money and move on")
        print("Goodbye 😉 ")
        break
    elif spin == "y":
        credit = credit - 1

        print("Credit = ", credit)
        # do the spins!
        slot1_value = (random.choice(slot1))
        slot2_value = (random.choice(slot2))
        slot3_value = (random.choice(slot3))

        print(slot1_value, slot2_value, slot3_value)

        if slot1_value == "🍓" and slot2_value == "🍉" and slot3_value == "🍒":
            credit = credit + 15
            print("Tutti Fruitti!")
            print("You've won 15 credits, your credit is now", credit)
        elif slot1_value == "🍉" and slot2_value == "🍉" and slot3_value == "🍉":
            print("Wow, triple watermelon!")
            print("You've won a voucher for 3 free fruity themed drinks from the casino bar🍹")
        elif slot1_value == "🥑" and slot2_value == "🥑" and slot3_value == "🥑":
            credit = credit + 10
            print("GOOD JOB!")
            print("You've won 10 credits, your credit is now", credit)
            print("Did you know an avocado is a fruit, more specifically a berry")
        elif slot1_value == "🍒" and slot2_value == "🍒" and slot3_value == "🍒":
            print("AMAZING!")
            credit = credit + 5
            print("You've won 5 credits")
            print("Did you know cherries belong to the rose family")
        elif slot1_value == "🥞" and slot2_value == "🥞" and slot3_value == "🥞":
            print("BIG MONEY. WINNER!!!!!!!!")
            credit = credit + 2500
            print("credit=", credit)
            num = random.randint(1, 33)
            print("\n-----------------------------------------------------------\n")
            print("You have unlocked our secret game that gives you a chance to double your money")
            time.sleep(2)
            print("All you have to do is guess correctly what number the ball is going to land on")
            print("But if you get it wrong you will lose everything")
            time.sleep(2)
            print("It will be a  random number between 1-33")
            Q = input("Do you want to try to double your money or continue?")
            if Q == "double":
                guess = input("What do number do you think the ball will land on?")
                if guess == num:
                    credit = credit * 2
                    print("WINNER!It was", num, "Your credit has now doubled to", credit)
                    print("\n-----------------------------------------------------------\n")
                else:
                    print("Unlucky, it was", num, "let's play on")
                    print("\n-----------------------------------------------------------\n")



        elif slot1_value == slot2_value:
            print("ooh")
        elif slot1_value == slot3_value:
            print("ooh")
        elif slot3_value == slot2_value:
            print("ooh")
        else:
            print("too bad")

        if credit == 0:
            print("GET OUT OF MY CASINO!")
            break
