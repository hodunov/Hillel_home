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

def gen(val):
    for i in val:
        yield i




