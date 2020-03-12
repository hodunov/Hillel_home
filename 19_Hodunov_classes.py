class Hero:
    """description of all heroes"""
    def __init__(self, name):
        """Names of all heroes"""
        self.name = name

    def talk(self):
        """Speech of bad heroes"""
        return print("-I'll eat you, Kolobok")


class Grandpa(Hero):
    """Grandpa info"""
    def beg_grendma(self):
        """Speech to Grandma"""
        return print('-Dear grandma, I\'m hungry! =( Please bake a kolobok!')


class Grandma(Hero):
    """Grandma info"""
    def bake_kolobok(self):
        """Baking"""
        print("~~~ Grandma Bake Kolobok ~~~ \n~~~ Kolobok created ~~~")
        return Kolobok('Kolobok')


class Kolobok(Hero):
    """Grandma info"""
    def rest(self):
        """Func for rest"""
        return print('~~~ Kolobok rests ~~~')

    def roll(self):
        """Func for roll"""
        return print('~~~ Kolobok rolls ~~~')

    def sing_song(self):
        """Func for sing"""
        return print("-HO HO HO, I'LL GO")

    def die(self):
        """Func for die"""
        return print("~~~ Kolobok died ='( ~~~")


class Bunny(Hero):
    pass


class Wolf(Hero):
    pass


class Fox(Hero):
    """Fox info"""
    def praise(self):
        """First speech"""
        return print("You're a good singer!")

    def request(self):
        """Second speech"""
        return print("I can't hear well, "
                     "please sit on my tongue and sing again.")


class Tale:
    def __init__(self, grandpa_tale, grandma_tale, bunny_tale, wolf_tale, fox_tale):
        """Names of all heroes"""
        self.grandpa = grandpa_tale
        self.grandma = grandma_tale
        self.kolobok = None
        self.bunny = bunny_tale
        self.wolf = wolf_tale
        self.fox = fox_tale

    def grandmas_house(self):
        """Story begin"""
        print("|||Grandma's house|||\nGrandpa says:")
        self.grandpa.beg_grendma()
        self.kolobok = self.grandma.bake_kolobok()
        self.kolobok.rest()

    def wood(self):
        """Story in wood"""
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
        """Main story"""
        self.grandmas_house()
        self.wood()


GRANDPA, GRANDMA = Grandpa('Ded'), Grandma('Grandma')
BUNNY, WOLF, FOX = Bunny("Bunny"), Wolf('Wolk'), Fox('Fox')

Tale(GRANDPA, GRANDMA, BUNNY, WOLF, FOX).start()
