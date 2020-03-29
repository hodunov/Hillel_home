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


class Mammal(Animal):
    """
    У млекопитающий (Mammal) есть потомство (число)
    """

    def __init__(self, name, animal_type, species, mass, progeny):
        super().__init__(name, animal_type, species, mass)
        self.progeny = progeny


class Reptile(Animal):
    """
    У рептилий (Reptile) - является ли ядовитым? (число 1 - Да, 0 - Нет)
    """

    def __init__(self, name, animal_type, species, mass, toxic):
        super().__init__(name, animal_type, species, mass)
        self.toxic = toxic


class Bird(Animal):
    """
    У птиц (Bird):
    - размах крыльев (число)
    - умеет ли издавать звуки? (число 1 - Да, 0 - Нет)
    - если умеет издавать звуки, то какие? (строка)
    """

    def __init__(self, name, animal_type, species, mass, wingspan, make_sounds, sounds=None):
        super().__init__(name, animal_type, species, mass)
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
            animal_to_db = Mammal(animal_args[0], animal_args[1], animal_args[2], animal_args[3], animal_args[4])
        if animal_args[1] == 'Reptile':
            animal_to_db = Reptile(animal_args[0], animal_args[1], animal_args[2], animal_args[3], animal_args[4])
        if animal_args[1] == 'Bird':
            if len(animal_args) <= 6:
                animal_to_db = Bird(animal_args[0], animal_args[1], animal_args[2], animal_args[3], animal_args[4],
                                    animal_args[5])
            else:
                try:
                    sound_str = str(animal_args[6] + " " + animal_args[7] + " " + animal_args[8] + " " + animal_args[9])
                    animal_to_db = Bird(animal_args[0], animal_args[1], animal_args[2], animal_args[3], animal_args[4],
                                        animal_args[5], sound_str)
                except IndexError:
                    pass
        return animal_to_db

    def show_db(self):
        return self.__animal_db


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

max_length = len(db.show_db())

print(db.show_db())

for i in range(0, max_length):
    print(f" === Animal #{i} === ")
    print(db.show_db()[i].name), print(db.show_db()[i].animal_type), print(db.show_db()[i].species)
    print(db.show_db()[i].mass)
    try:
        print(db.show_db()[i].progeny)
    except AttributeError as e:
        pass
    try:
        print(db.show_db()[i].toxic)
    except AttributeError as e:
        pass
    try:
        print(db.show_db()[i].wingspan)
    except AttributeError as e:
        pass
    try:
        print(db.show_db()[i].make_sounds)
    except AttributeError as e:
        pass
    try:
        if db.show_db()[i].sounds is not None:
            print(db.show_db()[i].sounds)
    except AttributeError as e:
        pass

# ______________________ 2  ____________________________


print("=================================================\nTASK 2\n=================================================")

query_choice = "[T] animal_type \n[SP] species \n[M] Mass \n" \
               "[P] Progeny \n[T] Toxic \n[W] Wingspan \n[MS] Make_sounds \n[S] Sounds "

max_length = len(db.show_db())


class Search:
    def name(self, name):
        global max_length
        for i in range(0, max_length):
            if name in db.show_db()[i].name:
                return db.show_db()[i].name

    def animal_type(self, name):
        for i in range(0, max_length):
            if name in db.show_db()[i].name:
                return db.show_db()[i].animal_type

    def species(self, name):
        for i in range(0, max_length):
            if name in db.show_db()[i].name:
                return db.show_db()[i].species

    def mass(self, name):
        for i in range(0, max_length):
            if name in db.show_db()[i].name:
                return db.show_db()[i].mass

    def progeny(self, name):
        for i in range(0, max_length):
            if name in db.show_db()[i].name:
                return db.show_db()[i].progeny

    def toxic(self, name):
        for i in range(0, max_length):
            if name in db.show_db()[i].name:
                return db.show_db()[i].toxic

    def wingspan(self, name):
        for i in range(0, max_length):
            if name in db.show_db()[i].name:
                return db.show_db()[i].wingspan

    def make_sounds(self, name):
        for i in range(0, max_length):
            if name in db.show_db()[i].name:
                return db.show_db()[i].make_sounds

    def sounds(self, name):
        for i in range(0, max_length):
            if name in db.show_db()[i].name:
                return db.show_db()[i].sounds


while True:
    chose_animal = input("Enter animal name here \n")
    for i in range(0, max_length):
        if chose_animal in db.show_db()[i].name:
            print(query_choice)
            input_property = input("Enter the first letter of an animal attribute.\n")
            try:
                if input_property == "T":
                    print("Animal Type = ", Search().animal_type(chose_animal))
                if input_property == "SP":
                    print("Species = ", Search().species(chose_animal))
                if input_property == "M":
                    print("Mass =", Search().mass(chose_animal))
                if input_property == "P":
                    print("Progeny =", Search().progeny(chose_animal))
                if input_property == "T":
                    print("Toxic =", Search().toxic(chose_animal))
                if input_property == "W":
                    print("Wingspan =", Search().wingspan(chose_animal))
                if input_property == "MS":
                    print("Make sounds =", Search().make_sounds(chose_animal))
                if input_property == "S":
                    print("Sounds =", Search().sounds(chose_animal))
            except AttributeError:
                print("SORRY! An animal has no attribute!")
