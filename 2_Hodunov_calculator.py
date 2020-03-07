sing = input('Input the sign  ')
f_num = input('Input the first number   ')
s_num = input('Input the second number   ')
dev_sings = ('/', '//', '%')
if f_num.isdigit() and s_num.isdigit():
    f_num = int(f_num)
    s_num = int(s_num)
    if sing == '+':
        print(f_num + s_num)
    elif sing == '-':
        print(f_num - s_num)
    elif sing in dev_sings and int(s_num) == 0:
        print('Error: Division by zero!')
    elif sing == '//':
        print(f_num // s_num)
    elif sing == '%':
        print(f_num % s_num)
    elif sing == '/':
        print(f_num / s_num)
    elif sing == '*':
        print(f_num * s_num)
    else:
        print('Oops! Not valid operation!')
else:
    print('Hey Hey Bad News! One of the numbers is not a digit...')


# or Try- except

sing = input('Input the sign  ')
f_num = input('Input the first number   ')
s_num = input('Input the second number   ')
Zerro_Error = 'Error: Division by zero!'
if f_num.isdigit() and s_num.isdigit():
    f_num = int(f_num)
    s_num = int(s_num)
    if sing == '+':
        print(f_num + s_num)
    elif sing == '-':
        print(f_num - s_num)
    elif sing == '//':
        try:
            print(f_num // s_num)
            pass
        except ZeroDivisionError:
            print(Zerro_Error)
    elif sing == '%':
        try:
            print(f_num % s_num)
            pass
        except ZeroDivisionError:
            print(Zerro_Error)
    elif sing == '/':
        try:
            print(f_num / s_num)
            pass
        except ZeroDivisionError:
            print(Zerro_Error)
    elif sing == '*':
        print(f_num * s_num)
    else:
        print('Oops! Not valid operation!')
else:
    print('Hey Hey Bad News! One of the numbers is not a digit...')
