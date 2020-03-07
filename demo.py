class Hero:
    def __init__(self, name):
        self.name = name


class Colobok(Hero):
    def roll(self):
        return print('Kolobok rolls')

    def rest(self):
        return print('Kolobok rests')



class Babka(Hero):
    def bake_colobok(self):
        print('Babka bake Kolobok')
        return Colobok('Kolobok')


class Tale:
    def __init__(self, Babka):
        self.Babka = Babka
        self.Colobok = None

    def babkin_dom(self):
        self.Colobok = self.Babka.bake_colobok()
        self.Colobok.roll()
        self.Colobok.rest()

    def end(self):
        return print('end of tail')

    def start(self):
        self.babkin_dom()
        self.end()


babushka = Babka('Babushka')
Tale(babushka).start()
