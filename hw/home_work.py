"""
№1

У нас есть база данных зверей - AnimalDataBase.
Так же есть записи в реестре про зверей - records.

У каждого зверя есть набор стандартных атрибутов (см. класс Animal) и некоторые уникальные.
У млекопитающий (Mammal):
    - потомство (число).
У рептилий (Reptile):
    - является ли ядовитым? (число 1 - Да, 0 - Нет)
У птиц (Bird):
    - размах крыльев (число)
    - умеет ли издавать звуки? (число 1 - Да, 0 - Нет)
    - если умеет издавать звуки, то какие? (строка)

Нужно пройтись по всем записям в реестре (records) и сохранить всех зверей в базу данных AnimalDataBase.

Последовательность слов в каждой записии в реестре == последовательность параметров для каждого животного (сначала
базовые, потом уникальные).
Нужно определить какое это животное (по второму слову каждой записи в реестре) и правильно его сохранить со всеми
параметрами,
для этого нужно изменить метод `_create_animal` в AnimalDataBase

№2
Запросить ввод имени животного - `input()`
Напечатать строку с предложением ввести первую букву атрибута животного (показывать все возможные атрибуты (9 шт.).
Пример - `query_choice`
После ввода нужной буквы, вывести значение данного атрибута у животного с данным именем, либо напечатать что такого
атрибута у животного нету.
"""


class Animal:
    def __init__(self, name, animal_type, species, mass):
        self.name = name
        self.animal_type = animal_type
        self.species = species
        self.mass = mass


class Mammal:
    """
    У млекопитающий (Mammal) есть потомство (число)
    """

    def __init__(self, progeny):
        self.progeny = progeny


class Reptile:
    """
    У рептилий (Reptile) - является ли ядовитым? (число 1 - Да, 0 - Нет)
    """

    def __init__(self, toxic):
        self.toxic = toxic


class Bird:
    """
    У птиц (Bird):
    - размах крыльев (число)
    - умеет ли издавать звуки? (число 1 - Да, 0 - Нет)
    - если умеет издавать звуки, то какие? (строка)
    """
    def __init__(self, wingspan, make_sounds, sounds=None):
        self.wingspan = wingspan
        self.make_sounds = make_sounds
        self.sounds = sounds


class AnimalDataBase:
    __animal_db = []

    def save_animal_to_db(self, animal):
        self.__animal_db.append(animal)

    def save_animals_from_records(self, records):
        for record in records:
            animal = self._create_animal(record)
            self.save_animal_to_db(animal)

    def _create_animal(self, record):
        global animal_to_db
        animal_args = record.split(' ')
        if animal_args[1] == "Mammal":
            animal_to_db = Animal(animal_args[0], Mammal(animal_args[4]), animal_args[2], animal_args[3])
        if animal_args[1] == 'Reptile':
            animal_to_db = Animal(animal_args[0], Reptile(animal_args[4]), animal_args[2], animal_args[3])
        if animal_args[1] == 'Bird':
            animal_to_db = Animal(animal_args[0], Bird(animal_args[4], animal_args[5]), animal_args[2],
                                  animal_args[3])
        return animal_to_db


records = [
    'Bob Mammal Bear 300 2',
    'Lucy Reptile Lizard 2 0',
    'Carl Reptile Cottonmouth 3 1',
    'Oliver Bird Ostrich 75 60 0',
    'Polly Bird Parrot 1 2 1 I want a cracker',
    'Doug Mammal Dog 20 4'
]

db = AnimalDataBase()
db.save_animals_from_records(records)
print(db._AnimalDataBase__animal_db)  # Возвращаю объекты, а нужна строка?

# ______________________ 2  ____________________________

query_choice = "[T] animal_type \n[SP] species \n[M] Mass \n" \
               "[P] Progeny \n[T] Toxic \n[W] Wingspan \n[MS] Make_sounds \n[S] Sounds "

while True:
    chose_animal = input("Enter animal name here \n")
    if chose_animal in db._AnimalDataBase__animal_db:  # как теперь пройтись по листу? так же через split?
        print(query_choice)
        input_property = input("Input letter of the property")
        if input_property == "T":  # Можно через словарь релизовать? что-то вроде {"W": _AnimalDataBase__animal_db[1]}
            print("Animal type is ")  # через split доставать значение?
        if input_property == "SP":
            print("Animal species is ")
        if input_property == "M":
            print("Animal mass is ")
        if input_property == "P":
            print("Animal progeny is ")
        if input_property == "T":
            print("")
        if input_property == "W":
            print("")
        if input_property == "MS":
            print("")
        if input_property == "S":
            print("")
        else:
            print("an animal does not have that attribute.")
    else:
        print("There's no such animal.")
