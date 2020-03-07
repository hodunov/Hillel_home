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
        self.grandpa = Grandpa
        self.grandma = Grandma
        self.kolobok = None
        self.bunny = Bunny
        self.wolf = Wolf
        self.fox = Fox

    def grandmas_house(self):
        print("|||Grandma's house|||\nGrandpa says:")
        self.grandpa.beg_grendma()
        self.kolobok = self.grandma.bake_kolobok()
        self.kolobok.rest()

    def wood(self):
        print("|||Wood|||")
        self.kolobok.roll()
        print("Bunny says:")
        self.bunny.talk()
        print("Kolobok says:")
        self.kolobok.sing_song()
        self.kolobok.roll()
        print("Wolf says:")
        self.wolf.talk()
        print("Kolobok says:")
        self.kolobok.sing_song()
        self.kolobok.roll()
        print("Fox says:")
        self.fox.talk()
        print("Kolobok says:")
        self.kolobok.sing_song()
        print("Fox says:")
        self.fox.praise()
        self.fox.request()
        print("Kolobok says:")
        self.kolobok.sing_song()
        self.kolobok.die()

    def start(self):
        self.grandmas_house()
        self.wood()


Grandpa_1, Grandma_1, Bunny_1, Wolf_1, Fox_1 = Grandpa('Ded'), Grandma('Babka'), Bunny("Bunny"), Wolf('Wolk'), Fox(
    'Lisa'),

Tale(Grandpa_1, Grandma_1, Bunny_1, Wolf_1, Fox_1).start()
