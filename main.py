class Player:
    max_health = 100

    def __init__(self, health):
        self.health = health
    def check_status(self):
        if self.health <= 0:
            print('end game')
        print(self.health)

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
    def attack(self, hero):
        self.damage - hero.health


def main():
    # weapon
    sword = Weapon('Sword', 5)
    axe = Weapon('Axe', 30)

    # hero 1
    hero = Player(100)
    hero.check_status()

    # monster
    goblin = Player(10)
    goblin.check_status()

    #
    axe.attack(goblin)
    goblin.check_status()


if __name__ == '__main__':
    main()