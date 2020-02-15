"""
В этом файле код различного типа, который написан не корректно и будет вызывать ошибки разного рода.
Задача в том, чтобы обработать ошибки (использовать не только Exception, а и ZeroDivisionError и т.д по ситуации) и
вместо трейсбека, как в примере в <<<>>> было сообщение о неисправности.
<<<
Traceback (most recent call last):
  File "/Users/vitaliifisenko/python_beginer/VVP2/3/HW/catch_errors.py", line 4, in <module>
    1/0
ZeroDivisionError: division by zero
>>>
Условие:
код с ошибками менять нельзя. Можно дополнять свой верный))


"""
# 1

try:
    1 / 0
except ZeroDivisionError:

    print("Zero Division Exception Raised")
else:
    print("Success, no error!")

print(input('Press Enter for step 2'))

# 2

value = input('Input something  ')

try:
    new_value = float(value) * (1 / 0)
except ZeroDivisionError:
    print("Zero Division Exception Raised")
else:
    print(new_value)

print(input('Press Enter for step 3'))

# 3

example_str = 'Mama myla ramu'
try:
    example_str[-1] = 'y'
except TypeError:
    print('TypeError Exception Raised')
else:
    print(example_str)

print(input('Press Enter for step 4'))

# 4 x2 our fruits

example_dict = {'apple': 9, 'banana': 5, 'plum': 2, 'lemon': 1}
try:
    print({k: v * 2 for k, v in example_dict})
except ValueError:
    print('ValueError: too many values to unpack (expected 2)')
else:
    print({k: v * 2 for k, v in example_dict})

print(input('Press Enter for step 5'))

# 5
"""
Тут задача чтобы вызвать функцию с аргументами и обработать ошибки, которые будут рвйзится 
Пример:
<<< 
def some_fun(a,b):
    return a/b

try:
    some_fun(5, '10')
except TypeError:
    print(Some msg)
>>>
Функция должбыть вызвана не менее 5-ти раз с разными по значению или типу аргументами
"""


def func_with_errors(some_val1, some_val2):
    """
    Функция которая намеренно вызывает ошибки в зависимости от входных данных
    :param some_val1: int
    :param some_val2: int
    :return: None
    """
    if some_val1 == some_val2:
        raise TypeError
    elif type(some_val1) == type(some_val2) and some_val1 < some_val2:
        raise ImportWarning
    elif type(some_val1) == type(some_val2) and some_val1 > some_val2:
        raise NotImplemented
    elif some_val1 != some_val2:
        raise SystemError


try:
    func_with_errors(5, 5)
except TypeError:
    print("Oops!  That's TypeError!")

try:
    func_with_errors([1, 2, 3, 4], [1, 2, 3])
except TypeError:
    print("Oops!  That's TypeError!")

try:
    func_with_errors(5, 6)
except ImportWarning:
    print("Oops!  That's ImportWarning!")

try:
    func_with_errors(6.0, 5.5)
except TypeError:
    print("Oops!  That's TypeError!")

Type_A = [1, 2, 'Python']
Type_B = 12
try:
    func_with_errors(Type_A, Type_B)
except SystemError:
    print("Oops!  That's SystemError!")

Type_A = [1, 2, 3, 4]
Type_B = (1, 2, 3, 4)
try:
    func_with_errors(Type_A, Type_B)
except SystemError:
    print("Oops!  That's SystemError!")

print(input('Press Enter to finish the code'))
