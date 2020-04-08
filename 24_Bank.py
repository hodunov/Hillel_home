"""
ЧТО СДЕЛАНО
Реализован класс банкомата (вероятно, нужно будет добавить методов или атрибутов)
Реализован класс аккаунта (вероятно, нужно будет добавить методов или атрибутов)
Реализован (не полностью) класс банка
ЧТО НУЖНО СДЕЛАТЬ
Дописать класс банка:
у банка должны быть сервисные методы
удаления банкомата из списка (вероятно, прийдется переделать его на словарь для простоты) банка
Аварийное сохранение данных о банкоматах и аккаунтах (в разные файлы)
Удаление аккаунтов из списка аккаунтов
А так же менюшка - перевод стредств между аккаунтами и создание аккаунта (если будет муза - можно добавить что-то свое)
2 Написать функцию или класс, где создасться объект банка и банкомата этого банка, так же будет меню с выбором куда юзер хочет пойти.
Если у него нет (обработка ошибок) аккауунта - соббщение о том, что нужно пойти сначала в банк и создать аккаунт.
Если аккаунт есть -  у юзера есть выбор куда пойти банк или банкомат. При выборе банка - будет меню банка, если банкома - банкомата
Менять текущие методы можно по потребности
"""

# _____BANKOMAT/ACC______
import json


class PersonACC:
    """
    Потом будет создаваться в классе БАНК
    А так это аккаунт человека в банке
    """

    # TODO: убрать пустое изменяемое из дефолтов +
    def __init__(self, inn, limit, set_limit, passport_data):
        self.inn = inn
        self.passport_data = passport_data
        self.__person_id = self.__generate_id()
        self.__login = f'{self.passport_data["full_name"]}'
        self.__pwd = f'{self.__person_id}pwd'
        self.get_limit = limit
        self.set_limit = set_limit
        self.__curr_money = 0

    def __generate_id(self):
        """Генератор идентификатора пользователя"""
        return f'{self.inn + self.passport_data["number"]}'

    @property
    def login(self):
        """вход в систему"""
        return self.__login

    @property
    def password(self):
        """Ввод пароля"""
        return self.__pwd

    @property
    def cur_money(self):
        """Информация о текущем состоянии счёта"""
        return self.__curr_money

    # TODO: добавить метод для снятия денег с аккаунта +

    def set_money(self, val):
        ""
        if val <= self.set_limit:
            self.__curr_money += val
            return
        print('Set set limit is is low')

    # TODO: rename method+
    def check_money_limit(self, money):
        """Проверка лимита"""
        return all((self.get_limit > int(money), self.__curr_money))

    def cash_out(self, amount):
        self.__curr_money -= int(amount)

    def to_dict(self):
        """
        Method to convert obj attrs to dict
        :param self: ссылка на объект
        :return:
        """
        return {
            'inn': self.inn,
            'limit': self.get_limit,
            'set_limit': self.set_limit,
            'passport_data': self.passport_data,
        }


class ATM:
    def __init__(self, bank):
        self.bank = bank
        self.bank.add_atm(self)

    def __check_bank(self):
        """
        Проверка рабочий ли банкомат
        :return: bool
        """
        return self in self.bank.atm_list

    def __connect_to_bank(self, person_acc):
        """
        Метод проверяет рабочий ли банкомат и визывает логин аккаунта в банке, иначе возвращает фолс
        :param person_acc: аккаунт человека
        :return: буль
        """
        if self.__check_bank():
            return self.bank.login(person_acc)
        return False

    def main(self, person_acc):
        """
        Метод проверяет коннект к банку,если все гуд - заходит в меню банкомата
        :param person_acc: аккаунт человека
        :return: None
        """
        if self.__connect_to_bank(person_acc):
            while True:
                operation = input('Input operation: (get/set/balance/exit)\n')
                if operation == 'get':
                    money = input('Input value to get')
                    self.bank.get_money(person_acc, money)
                    print("Take your money")
                elif operation == 'set':
                    money = input('Input value to set')
                    self.bank.set_money(person_acc, money)
                    print("Set success")
                elif operation == 'balance':
                    self.bank.get_acc_balance(person_acc)
                elif operation == 'exit':
                    print('By-by')
                    break
        else:
            print('Login failed\nFirst, you need to go to the bank and create an account. ')


class Bank:
    def __init__(self, name, start_money):
        self.name = name
        self.start_money = start_money
        self.__atm_list = []
        self.__accounts = {}

    @property
    def atm_list(self):
        """Список банкоматов"""
        return self.__atm_list

    def add_atm(self, new_atm):
        """
        Метод для добавления нового банкомата в список банкоматов банка
        :return:
        """
        self.__atm_list.append(new_atm)
        return self.__atm_list

    def delete_atm(self, old_atm):
        self.__atm_list.remove(old_atm)

    def create_person_acc(self, *args, **kwargs):
        """
        Метод создает аккаунт в банке,добавляя его в хранилище аккаунтов банка
        :param args:
        :param kwargs:
        :return:
        """
        person_acc = PersonACC(args[0], args[1], args[2], **kwargs)
        self.__accounts[person_acc.login] = person_acc

    def login(self, person_acc):
        """
        Метод для логина, сравнивает пароли аккаунта и банка, если гуд - вернет тру
        :return: буль
        """
        try:
            bank_side_acc = self.__accounts[person_acc.login]
            if bank_side_acc.password == person_acc.password:
                return True
            return False
        except KeyError:
            return False

    def get_money(self, person_acc, money):
        """
        Метод для снятия денег с аккаунта
        :return:
        """
        if person_acc.check_money_limit(money):
            person_acc.cash_out(money)
            print(person_acc.cur_money)

    def set_money(self, person_acc, money):
        """
        Метод для добавления денег
        :return:
        """
        person_acc.set_money(int(money))
        print(person_acc.cur_money)

    def get_acc_balance(self, person_acc):
        """
        Метод для показывания текущего баланса
        :return:
        """
        print(person_acc.cur_money)

    def del_bank_ATM(self, del_ATM):
        """Удаление банкомата банка"""
        if del_ATM in self.__atm_list: self.__atm_list.remove(del_ATM)
        return

    def del_acc(self, del_acc):
        """Удаление аккаунта"""
        if del_acc in self.__accounts:
            del self.__accounts[del_acc]
        return self.__accounts

    def save_person(self):
        with open("Person.txt", 'w') as file:
            data = []
            for v in self.__accounts.values():
                data.append(v.to_dict())
            json.dump(data, file)

    def save_ATM(self):
        """Сохранение данных в файл"""
        with open('ATM_backup.txt', 'w') as file:
            file.write(str(len(self.__atm_list)))

    def main(self, person_acc):
        while True:
            operation = input('Input operation: (atm_list/create_acc/balance/set/exit)\n')
            if operation == 'atm_list':
                print(self.atm_list)
            elif operation == 'create_acc':
                print("Wait a second... we're creating your account.")
                inn = int(input("input inn\n"))
                limit = int(input("input limit\n"))
                set_limit = int(input("input set_limit\n"))
                full_name = input("Enter your full_name")
                number = int(input("Enter your number"))
                return self.create_person_acc(inn, limit, set_limit,
                                              passport_data={"full_name": full_name, "number": number})
            elif operation == 'balance':
                if self.login(person_acc):
                    print(self.get_acc_balance(person_acc))
                print("No account. First, create an account.")
            elif operation == 'set':
                if self.login(person_acc):
                    self.set_money(person_acc, int(input("Enter money value\n")))
                    return
                print("No account. First, create an account.")
            elif operation == 'exit':
                print('By-by')
                break


"""Написать функцию или класс, где создасться объект банка и банкомата этого банка, так же будет меню с выбором куда юзер хочет пойти.
Если у него нет (обработка ошибок) аккауунта - соббщение о том, что нужно пойти сначала в банк и создать аккаунт.
Если аккаунт есть -  у юзера есть выбор куда пойти банк или банкомат. При выборе банка - будет меню банка, если банкома - банкомата
Менять текущие методы можно по потребности"""


def main():
    Monobank = Bank("Monobank", 1000000)
    my_Atm = ATM(Monobank)
    Monobank.add_atm('IBOX')
    Monobank.create_person_acc(123, 30000, 20000, passport_data={"full_name": "MORTY", "number": 666})
    RICK = PersonACC(1, 2, 3, passport_data={"full_name": "RICK", "number": 1})
    Monobank.save_ATM()
    Monobank.save_person()
    try:
        while True:
            go_to = input("Where you go? (ATM/BANK) \n")
            if go_to == "ATM":
                my_Atm.main(RICK)
            if go_to == "BANK":
                Monobank.main(RICK)
    except Exception:
        Monobank.save_person()
        Monobank.save_ATM()
        print(f"An unforeseen error has occurred ({e})"
              "The data has been saved.")


main()
