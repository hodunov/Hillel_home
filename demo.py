user_list = []

while True:
    try:
        user_month = int(input('Enter your month  '))
        if 0 < user_month < 13:
            user_list.append(user_month)
            break
        else:
            print('Enter month number from 1 to 12')
    except ValueError:
        print('Input the numbers!')

while True:
    try:
        user_year = int(input('Enter your year  '))
        if 0 < user_year:
            user_list.append(user_year)
            break
        else:
            print('Try another year!')
    except ValueError:
        print('Input the numbers!')

print(f'Your date is {user_list}')  # Как убрать квадратные скобки в отображении листа?


def date_range(date):
    first_date = [10, 1994]
    second_date = [2, 2020]
    if first_date[1] < date[1] < second_date[1]:
        return f'Date {date} in range'
    elif date[1] == first_date[1]:
        if date[0] >= first_date[0]:
            return f"Date {date} in range between {first_date} and {second_date}"
        else:
            return f"Date {date} is out of range between {first_date} and {second_date}"
    elif date[1] == second_date[1]:
        if date[0] <= second_date[0]:
            return f"Date {date} in range between {first_date} and {second_date}"
        else:
            return f"Date {date} is out of range between {first_date} and {second_date}"
    else:
        return f"Date {date} is out of range =("


print(date_range(user_list))
