class Hero:
    def __init__(self, name):
        self.name = name

    def talk(self):
        return print("-I'll eat you, Kolobok")


class Grandpa(Hero):
    def beg_grendma(self):
        return print('-Dear grandma, I\'m hungry! =( Please bake a kolobok!')


class Grandma(Hero):
    def bake_kolobok(self):
        print("~~~ Grandma Bake Kolobok ~~~ \n~~~ Kolobok created ~~~")
        return Kolobok('Kolobok')


class Kolobok(Hero):
    def rest(self):
        return print('~~~ Kolobok rests ~~~')

    def roll(self):
        return print('~~~ Kolobok rolls ~~~')

    def sing_song(self):
        return print("-HO HO HO, I'LL GO")

    def die(self):
        return print("~~~ Kolobok died ='( ~~~")


class Bunny(Hero):
    pass


class Wolf(Hero):
    pass


class Fox(Hero):
    def praise(self):
        return print("You're a good singer!")

    def request(self):
        return print("I can't hear well, please sit on my tongue and sing again.")


class Tale:
    def __init__(self, Grandpa, Grandma, Bunny, Wolf, Fox):
        self.Grandpa = Grandpa
        self.Grandma = Grandma
        self.Kolobok = None
        self.Bunny = Bunny
        self.Wolf = Wolf
        self.Fox = Fox

    def grandmas_house(self):
        print("|||Grandma's house|||\nGrandpa says:")
        self.Grandpa.beg_grendma()
        self.Kolobok = self.Grandma.bake_kolobok()
        self.Kolobok.rest()

    def wood(self):
        print("|||Wood|||")
        self.Kolobok.roll()
        print("Bunny says:")
        self.Bunny.talk()
        print("Kolobok says:")
        self.Kolobok.sing_song()
        self.Kolobok.roll()
        print("Wolf says:")
        self.Wolf.talk()
        print("Kolobok says:")
        self.Kolobok.sing_song()
        self.Kolobok.roll()
        print("Fox says:")
        self.Fox.talk()
        print("Kolobok says:")
        self.Kolobok.sing_song()
        print("Fox says:")
        self.Fox.praise()
        self.Fox.request()
        print("Kolobok says:")
        self.Kolobok.sing_song()
        self.Kolobok.die()

    def start(self):
        self.grandmas_house()
        self.wood()


Grandpa_1, Grandma_1, Bunny_1, Wolf_1, Fox_1 = Grandpa('Ded'), Grandma('Babka'), Bunny("Bunny"), Wolf('Wolk'), Fox(
    'Lisa'),

Tale(Grandpa_1, Grandma_1, Bunny_1, Wolf_1, Fox_1).start()
