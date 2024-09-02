from hero import *

def main():
    # hero
    hero = Hero('KIT', 100)
    hero.status()

    # Enum
    goblin = Enum('Goblin', 20)
    goblin.status()

    hero.attack_enum(goblin)

if __name__ == '__main__':
    main()