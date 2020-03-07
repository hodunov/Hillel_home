def sum_digits(number):
    """
    Функция, которая на вход принимает число и возвращает сумму всех его цифр.
    Повторяет операццию до тех пор, пока не останется одна цифра.
    """
    if len(str(number)) == 1:
        return number
    else:
        all_but_last, last = number // 10, number % 10
        return sum_digits(sum_digits(all_but_last) + last)


print(f"An example of how the function works. sum_digits(189)= {sum_digits(189)}")

your_digit = int(input('Now Input your digit - '))
print(f"sum_digits({your_digit})= {sum_digits(your_digit)}")

print("That's all. God save the Stackoverflow")
