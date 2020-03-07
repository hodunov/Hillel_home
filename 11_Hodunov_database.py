"""
->Создать глобальный словарь для хранения данных о человеке.
    Структура словаря (можно добавлять поля):
     db = {
         идентификатор_юзера : {
         'name': имя,
         'age': возраст,
         'email': емейл,
         }
     }

->Создать функцию, которая будет запрашивать сохранять в глобальный словать имя, возраст и емейл, запрошенные у юзера.
     Условия:
      1. Возрастр обязательно должен быть интом (тут юзер не послушный)
      2. Должна стоять валидация на емейл (обязательно @ и точка)
      3. Если емейл не валидный - юзера в базу не сохраняем и выводим сообщение о невалидности емейла
-> Создать функцию, которая принимает идентификатор_юзера и удаляет всю информацию о нем из глобального словаря


-> В функции main должен постоянно идти опрос о команде, которую следует выполнить (while)  add/remove/show/exit
    при add добавляем юзера, remove  - удаляем, show - показать всех, exit - завершить опрос
"""

database = {}


def add_member():
    while True:
        try:
            user_nickname = str(input('Enter your nickname .\n'))
            if user_nickname.isdigit():  # Не получилось добавить условие ЕСЛИ СУЩЕСТВУЕТ В СЛОВАРЕ.
                raise ValueError  # пробовал через for user_nickname in database.items()
            break
        except ValueError:
            print('Please, input the str')
    while True:
        try:
            user_name = str(input("Enter your name.\n"))
            if user_name.isdigit():
                raise ValueError
            break
        except ValueError:
            print('Please, input the str')
    while True:
        try:
            user_age = int(input("Enter your age.\n"))
            break
        except ValueError:
            print("Oh,No! Please enter a number")
    user_email = str(input("Please enter your email.\n"))
    a = 0  # Email validation start
    y = len(user_email)
    dot, at = user_email.find("."), user_email.find("@")
    for i in range(0, at):
        if ('a' <= user_email[i] <= 'z') or ('A' <= user_email[i] <= 'Z'):
            a = a + 1
    if a > 0 and at > 0 and (dot - at) > 0 and (dot + 1) < y:
        print("Valid Email")
        new_member = {user_nickname: {'Name': user_name, 'Age': user_age, 'Email': user_email}}
        return database.update(new_member), print('Ok, you are added in database', database)
    else:
        print("Sorry. Invalid Email")


def main():
    while True:
        try:
            command = int(input('Which command need to do. 1- add, 2 - remove, 3- Show, 4- exit \n'))
            if 0 < command < 5:
                if command == 1:
                    add_member()
                elif command == 2:
                    delete_user = str(input("Enter your nickname which need to delete .\n"))
                    database.pop(delete_user, None)
                    print('You are deleted =(')
                    print('All users: \n', database)
                elif command == 3:
                    delete_user = str(input("Enter your nickname which need to delete .\n"))
                    database.pop(delete_user, None)
                    print('All users: \n', database)
                elif command == 4:
                    print("Exit. Have a nice day")
                    break
        except ValueError:
            print('Input the numbers!')
    pass


# это точка входа
if __name__ == '__main__':
    main()
