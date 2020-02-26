"""
Create function:
Input: Feb 12 2019 2:41PM # Str
Output: 2019-02-12 14:41:00 #Str
"""
from datetime import datetime

date_str = "Feb 12 2019 2:41PM"


def parser(my_datetime):
    return str(datetime.strptime(my_datetime, '%b %d %Y %I:%M%p').strftime("%Y-%m-%d %H:%M:%S"))


print(parser(date_str))

print(parser(str(input('Enter date (format Feb 12 2019 2:41PM) '))))
