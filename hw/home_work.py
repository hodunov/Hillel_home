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
    pass


class Reptile:
    pass


class Bird:
    pass


class AnimalDataBase:
    __animal_db = []

    def save_animal_to_db(self, animal):
        self.__animal_db.append(animal)

    def save_animals_from_records(self, records):
        for record in records:
            animal = self._create_animal(record)
            self.save_animal_to_db(animal)

    def _create_animal(self, record):
        animal_args = record.split(' ')
        return Animal(animal_args[0], animal_args[1], animal_args[2], animal_args[3])


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
print(db._AnimalDataBase__animal_db)

query_choice = """
Query animal 
[s] species
[m] mass
[l] ...
[v] ...
[w] ...
[t] ...
"""
print(query_choice)
