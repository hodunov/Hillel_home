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


def main():
    while True:
        try:
            command = int(input('Which command need to do. 1- add, 2 - remove, 3- Show, 4- exit \n'))
            if 0 < command < 5:
                database = {
                    'user_id': {
                        'name': 'Имя',
                        'age': 'возраст',
                        'email': 'емейл',
                    }
                }
                if command == 1:
                    username = str(input("Enter your username.\n"))
                    while True:
                        try:
                            user_age = int(input("Enter your age.\n"))
                            break
                        except ValueError:
                            print("Oh,No! Please enter a number")
                    user_email = str(input("Please enter your email.\n"))
                    database.update(name=username)
                    database.update(age=user_age)
                    database.update(email=user_email)
                    print('Ok, you are added in database', database)
                if command == 2:
                    print('Not yet')
                if command == 3:
                    print('All users: \n', database)
                if command == 4:
                    print('God')
            else:
                print('Thanks for all!')
                break
        except ValueError:
            print('Input the numbers!')
    pass


# это точка входа
if __name__ == '__main__':
    main()
