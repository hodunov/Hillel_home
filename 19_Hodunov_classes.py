class Hero:
    def __init__(self, name):
        self.name = name


class Grandpa(Hero):
    def beg_grendma(self):
        return 'Dear grandma, I\'m hungry! =( Please bake a kolobok!'


class Grandma(Hero):
    def bake_kolobok(self):
        return Kolobok('Kolobok is created')


class Kolobok(Hero):
    def rest(self):
        return 'Kolobok rests'

    def roll(self):
        return 'Kolobok rolls'

    def sing_song(self):
        return "HO HO HO, I'LL GO"

    def die(self):
        return "Kolobok died ='("


class Bunny(Hero):
    def talk(self):
        return "I'll eat you, Kolobok"


class Wolf(Hero):
    def talk(self):
        return "I'll eat you, Kolobok"


class Fox(Hero):
    def talk(self):
        return "I'll eat you, Kolobok"

    def praise(self):
        return "You're a good singer!"

    def request(self):
        return "I can't hear well, please sit on my tongue and sing again."


class Tale:
    def __init__(self, Grandpa, Grandma, Kolobok, Bunny, Wolf, Fox):
        self.grandpa = Grandpa
        self.grandma = Grandma
        self.kolobok = Kolobok
        self.bunny = Bunny
        self.wolf = Wolf
        self.fox = Fox

    def grandmas_house(self):
        self.grandpa = self.grandpa.beg_grendma()
        self.kolobok = self.grandma.bake_kolobok()
        self.kolobok = self.kolobok.rest()

    def wood(self):
        self.kolobok = self.kolobok.roll()
        self.bunny = self.bunny.talk()
        self.kolobok = self.kolobok.sing_song()
        self.kolobok = self.kolobok.roll()
        self.wolf = self.wolf.talk()
        self.kolobok = self.kolobok.sing_song()
        self.kolobok = self.kolobok.roll()
        self.fox = self.fox.talk()
        self.kolobok = self.kolobok.sing_song()
        self.fox = self.fox.praise()
        self.fox = self.fox.request()
        self.kolobok = self.kolobok.sing_song()
        self.kolobok = self.kolobok.die()

    def start(self):
        self.grandmas_house()
        self.wood()


Tale.start()
