import re

# my_str = "Artem Артем 010101 Артёмка"
# print(my_str.split(" "))
# for every_word in my_str.split(" "):
#     if re.match(r'\w', every_word, flags=re.ASCII) is None:
#         raise BaseException('Not match reg exp(((')
#     else:
#         pass

my_str2 = "Artem Hodunov"
print(my_str2.split(" "))
for every_word in my_str2.split(" "):
    if re.match(r'\w', every_word, flags=re.ASCII) is None:
        raise BaseException('Not match reg exp(((')
    else:
        task = Item(task_name, done)
        self.tasks.update({task.name: task.done})
