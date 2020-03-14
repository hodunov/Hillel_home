"""
Реализовать класс Person, у которого должно быть два атрибута: age и name.
Также у него должен быть следующий набор методов:
def know(self, another_person_object)
который позволяет добавить другого человека в список знакомых (лист __friends (обязательно приватный атрибут)).
И метод
def is_known(self, another_person_object)
который возвращает знакомы ли два человека (True/False)
"""


class Person:
    """
    Main Person Class
    """
    __friends = []

    def know(self, another_person_object):
        """
        add person to your friends list
        """
        self.__friends.append(another_person_object)
        return another_person_object

    def is_known(self, another_person_object):
        """
        check if the person knows another person
        """
        if another_person_object in self.__friends:
            return True
        else:
            return False


def main():
    """
    Displays inheritance methods
    """
    print(f"add {Person().know('Artem')} to friends list")
    print(f"add {Person().know('Anna')} to friends list")
    print(f"check if the person knows = {Person().is_known('Artem')}")
    print(f"check if the person knows = {Person().is_known('Darya')}")


if __name__ == '__main__':
    main()




