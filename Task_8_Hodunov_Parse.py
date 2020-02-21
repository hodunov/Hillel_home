def parse(my_str):
    my_list = []
    data = 0
    for i in my_str:
        if i == 'i':
            data += 1  # Когда надо ставить continue?
        if i == 'd':
            data += -1  # Не важно if или elif?
        if i == 's':
            data = data ** 2
        if i == 'o':
            my_list.append(data)
    return my_list


exp = 'iiisdoso'
print(f"That's what came out of it, Comrad {parse(exp)} ")
print("Now you can try to type the line yourself. ")

while True:
    try:
        user_data = str(input('Enter your str  '))
        if user_data.isdigit():
            raise ValueError
        break
    except ValueError:
        print('Please, input the str')

print(f"Good job. That's what came out of it, Comrad {parse(user_data)} ")
exit("That's all")
