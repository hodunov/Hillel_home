print("Hey. Now we're going to find out if your date (MONTHS-YEAR) belongs to the time range. ")

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

print(f'Your date is {".".join( str(e) for e in user_list )}')  


def date_range(date):
    first_date = [10, 1994]
    second_date = [2, 2020]
    first_date_out, second_date_out = ".".join(str(e) for e in first_date),".".join(str(e) for e in second_date)
    date_out = ".".join(str(e) for e in date)
    if first_date[1] < date[1] < second_date[1]:
        return f'Nothing to worry about! Date {date_out} in range between {first_date_out} and {second_date_out}'
    elif date[1] == first_date[1]:
        if date[0] >= first_date[0]:
            return f"It's all right. Date {date_out} in range between {first_date_out} and {second_date_out}"
        else:
            return f"Relax. Date {date_out} is out of range between {first_date_out} and {second_date_out}"
    elif date[1] == second_date[1]:
        if date[0] <= second_date[0]:
            return f"You did a nice job. Date {date_out} in range between {first_date_out} and {second_date_out}"
        else:
            return f"Bad news! Date {date_out} is out of range between {first_date_out} and {second_date_out}"
    else:
        return f"Houston, we're in trouble! Date {date_out} is out of range =("


print(date_range(user_list))
input("Work done, time for coffee. Press ENTER and let's go")
