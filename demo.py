class Hero:
    def __init__(self, name):
        self.name = name


class Colobok(Hero):
    pass


class Babka(Hero):
    def bake_colobok(self):
        return Colobok('Kolobok')


class Tale:
    def __init__(self, babka, ded):
        self.babka = babka
        self.ded = ded
        self.colobok = None

    def babkin_dom(self):
        self.colobok = self.babka.bake_colobok()

    def start(self):
        self.babkin_dom()


Tale.start(self)
