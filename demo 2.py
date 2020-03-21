import re

# my_str = "Artem Артем 010101 Артёмка"
# print(my_str.split(" "))
# for every_word in my_str.split(" "):
#     if re.match(r'\w', every_word, flags=re.ASCII) is None:
#         raise BaseException('Not match reg exp(((')
#     else:
#         pass

my_str2 = " Artem Hodunov "
print(my_str2.split(" "))
my_str2 = my_str2.lstrip(" ").rstrip(" ")
for every_word in my_str2.split(" "):
    if re.match(r'\w', every_word, flags=re.ASCII) is None:
        raise BaseException('Not match reg exp(((')
    print({my_str2: 123})
