user_list = []

while True:
    user_month = int(input('Enter your month  '))
    if 0 < user_month < 13:
        user_list.append(user_month)
        break
    else:
        print('LOL. Try again')

user_date = int(input('Enter your year  '))
