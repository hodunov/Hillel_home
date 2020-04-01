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

    def cash_out(self, value):
        """Метод для снятия денег"""
        self.__curr_money += value
        return self.__curr_money

    def set_money(self, val):
        ""
        if val <= self.set_limit:
            self.__curr_money += val
        print('Set set limit is is low')

    # TODO: rename method+
    def check_money_limit(self, money):
        """Проверка лимита"""
        return all((self.get_limit > money, self.__curr_money))

    def __sub__(self, other):
        self.__curr_money -= other


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
                operation = input('Input operation:')
                if operation == 'get':
                    money = input('Input value to get')
                    self.bank.get_money(person_acc, money)
                elif operation == 'set':
                    money = input('Input value to set')
                    self.bank.set_money(person_acc, money)
                elif operation == 'balance':
                    self.bank.get_acc_balance(person_acc)
                elif operation == 'exit':
                    print('By-by')
                    break
        else:
            print('Login failed ')


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
        bank_side_acc = self.__accounts[person_acc.login]
        if bank_side_acc.password == person_acc.password:
            return True
        return False

    def get_money(self, person_acc, money):
        """
        Метод для снятия денег с аккаунта
        :return:
        """
        if person_acc.check_money_limit(money):
            person_acc.get_money(money)
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

    def del_back_ATM(self, del_ATM):
        """Удаление банкомата банка"""
        if del_ATM in self.__atm_list: self.__atm_list.remove(del_ATM)
        return self.__atm_list

    def del_acc(self, del_acc):
        """Удаление аккаунта"""
        if del_acc in self.__accounts:
            del self.__accounts[del_acc]
        return self.__accounts

    def save(self):
        """Сохранение данных в файл"""
        with open('ATM_backup.txt', 'w') as file:
            file.write(str(self.__atm_list))
        with open('Accounts_backup.txt', 'w') as file:
            file.write(str(self.__accounts))




class Main:
    """Написать функцию или класс, где создасться объект банка и банкомата этого банка, так же будет меню с выбором куда юзер хочет пойти.
    Если у него нет (обработка ошибок) аккауунта - соббщение о том, что нужно пойти сначала в банк и создать аккаунт.
    Если аккаунт есть -  у юзера есть выбор куда пойти банк или банкомат. При выборе банка - будет меню банка, если банкома - банкомата
Менять текущие методы можно по потребности"""
    def choose(self,Bank,BankATM):



Alpha = Bank("Alpha", 300000)

Alpha_atm = Alpha.add_atm('AlphaATM')

print("TEST")


