def int_check:
    while True:
        try:
            your_number = int(input('Enter your number  '))
            break
        except ValueError:
            print("Not an integer! Please enter an integer")