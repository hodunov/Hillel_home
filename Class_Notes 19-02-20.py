# # Class Notes 19-02-2020
#
# # Fibonachi
#
#
# def fib(n):
#     if n < 3:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# def fact(n):
#     if n < 1:
#         return 1
#     return n * fact(n - 1)
#
#
# print(fib(10))
#
#
#
#
# bank_data = {
#     'Ivan':
#         {
#             'allowed_to_get_cash': False
#         },
#     'Petr':
#         {
#             'allowed_to_get_cash': True
#         }
# }
#
#
# def bank(cash, years, data, name, in_one_year=True):
#     def in_one_year_fun(money):
#         return money * (1 + 0.1) ** years
#
#     if in_one_year:
#         if data[name]['allowed_to_get_cash']:
#             return in_one_year_fun(cash)
#         return f'Sorry! Not allowed for {name}'
#     return in_one_year_fun(cash) * years
#
#
# print(bank(10, 2, bank_data, 'Petr'))
#
#
# def season(number):
#
#     seasons = {
#         'summer': (6, 7, 8),
#         'winter': (12, 1, 2),
#         'spring': (3, 4, 5),
#         'autumn': (9, 10, 11),
#     }
#     for key,value in seasons.items():
#         if number in value:
#             return key
#
#
# print(season(5))
#

""

""
#
#
# def my_fun(string, separator):
#     res = {}
#     new_list = string.split(separator)
#     for item in new_list:
#         res.update({item: new_list.count(item)})
#     return res
#
#
# my_str = input('String')
# delimeter = input('String')
#
# print(my_fun(my_str, delimeter))

"""

"""
# import math
#
#
# def square(a):
#     return a*4, a*a, a * math.sqrt(2)
#
#
# print(square(2))
#
#
#
# def args_test(*arg):
#     a, *b, c =
#
#
#
#
# def test_kwargs(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#
#
# test_kwargs(**{'a':1,'b':2})

with open('/Users/artgo/PycharmProjects/Hillel_home/text.txt', 'w') as file:
    file.writelines('abbb')
    print(file.write('Hello its a new doc!'))

