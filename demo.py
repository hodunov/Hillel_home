
def output_int(arg):
    try:
        return int(arg)
    except Exception as exception:
        exit(f"This argument can't be turned to int due to {exception}! Exit from program")



sing = input('Input the sign  ')
f_num = output_int(input('Input the first number   '))
s_num = output_int(input('Input the second number   '))
dev_sings = ('/', '//', '%')


def calc(operation, number1, number2):
    if operation == '+':
        print(number1 + number2)
    elif operation == '-':
        print(number1 - number2)
    elif operation in dev_sings and int(number2) == 0:
        print('Error: Division by zero!')
    elif operation == '//':
        print(number1 // number2)
    elif operation == '%':
        print(number1 % number2)
    elif operation == '/':
        print(number1 / number2)
    elif operation == '*':
        print(number1 * number2)
    else:
        print('Oops! Not valid operation!')


calc(sing, f_num, s_num)