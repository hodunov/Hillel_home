# CSV

# import csv
#
# db = {}
# with open("csv_example.csv", 'w') as file:
#     writer = csv.writer(file)
#     writer_2 = csv.DictWriter(file, db.items())
#     # writer.writerow('Hello')
#     # writer_2.writerow('Ho')
#
# import xlsxwriter
# sheet = xlsxwriter.Workbook('cs_example.xls')

# Generator

# def gen(val):
#     for i in val:
#         yield i
#
#
# def monitor(func_name, *args, **kwargs):
#     with open('monitor.txt', 'w') as file:  # file = open('monitor.txt', 'w')
#         file.write(f"Result is {func_name(*args, **kwargs)}")
#
#
# def my_fun(a, b):
#     return a + b
#
#
# monitor(my_fun, 1, 2)

# Move data

import requests, json


def get_data(url):
    return requests.get(url)


def parse_data():
    response = get_data('http://www.mocky.io/v2/5e56ab1e300000355b28e97c')
    data = response.json()
    print(data)
    for item in data:
        print(item)


# parse_data()


def parse_data_2():
    response = get_data('http://www.mocky.io/v2/5e56ab1e300000355b28e97c')
    data = response.json()
    with open('animals.json', 'w') as file:
        json.dump(data, file, indent=4)


parse_data_2()
