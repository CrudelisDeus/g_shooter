import random

# Hero
class Player:
    def __init__(self, name, health, damage, lvl):
        self.name = name
        self.health = health
        self.damage = damage
        self.lvl = lvl

    def attack(self, monster):
        damage = random.randint(self.damage - self.damage, self.damage)
        if damage == 0:
            print(self.name, 'shamefully missed')
        else:
            print(self.name, 'deals', damage, 'damage', monster.name)
        monster.health -= damage
        if monster.health <= 0:
            monster.health = 0
            self.lvl += monster.lvl
            print('Screams in pain and dies')
            print(self.name, 'kill', monster.name)

# Enum
class Enumy(Player):
    pass

def select_hero():
    print('1. Dmitry\n')
    while True:
        if input('select a hero: ') == '1':
            hero = Player('Dmitry', 100, 10, 0)
            return hero

def start_battle(hero, enum):
    while hero.health >= 1 and enum.health >= 1:
        hero.attack(enum)
        if enum.health >= 1:
            enum.attack(hero)

def select_location():
    print('1. ')


def main():
    sanya = Enumy('Sanya', 100, 10, 1)
    hero = select_hero()
    start_battle(hero, sanya)


if __name__ == '__main__':
    main()