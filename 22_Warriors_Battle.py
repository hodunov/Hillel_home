"""
Создать класс воина, создать 2 или больше объектов воина с соответствующими воину атрибутами.
Реализовать методы, которые позволять добавить силы воину, улучшить оружие.
Реализовать возможность драки 2х воинов с потерей здоровья,
приобретения опыта (можно магические методы, можно кастомные).
"""
from termcolor import cprint


class Warrior:
    def __init__(self, name):
        self.name = name
        self.max_health = 100
        self.health = self.max_health
        self.base_attack = 10
        self.experience = 0

    def show_status(self):
        return f"{self.name} status:\n  ❤ Health= {self.health}% \n" \
               f"  ✔ Experience= {self.experience} \n ↯ Base attack = {self.base_attack}"

    def improve_attack(self):
        self.base_attack += 10
        cprint(f"=== {self.name} Attack Improved! ===", color='blue')
        return self.base_attack

    def _reduce_health(self):
        self.health -= self.base_attack
        return self.health

    def fight(self):
        self._reduce_health()
        cprint(f"=== {self.name}  is under attack! ===", color='cyan')
        return self.health

    def add_power(self, amount):
        self.base_attack += amount
        cprint(f"=== {self.name}  increased power! ===", color='cyan')
        return self.base_attack

    def up_experience(self):
        self.experience += self.base_attack
        cprint(f"=== {self.name}  experience increased! ===", color='magenta')
        return self.experience

    def give_up(self):
        cprint(f"=== {self.name}  gives up! ===", color='magenta')


def main():
    """
    Display battle
    """
    print('||| START BATTLE |||')
    hero = Warrior("GoodBoy")
    enemy = Warrior("Badboy")
    cprint(hero.show_status(), color='green')
    cprint(enemy.show_status(), color='red')
    enemy.fight()
    cprint(enemy.show_status(), color='red')
    enemy.improve_attack()
    cprint(enemy.show_status(), color='red')
    hero.fight()
    cprint(hero.show_status(), color='green')
    enemy.fight()
    if enemy.health < 80:
        enemy.give_up()
    hero.up_experience()


if __name__ == '__main__':
    main()
