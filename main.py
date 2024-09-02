from hero import *

# Выборка героев
def select_hero():
    print('1. KIT')
    while True:
        hero = input("Выбери героя: ")
        if hero == '1':
            return Hero('KIT', 100)
# Старт битвы
def start_battle(hero, enum):
    while hero.live and enum.live:
        hero.attack_enum(enum)


def start_game(hero):
    goblin = Enum('Dmitry', 20)
    goblin2 = Enum('Sanya', 40)
    start_battle(hero, goblin)
    start_battle(hero, goblin2)

def main():

    hero = select_hero()
    start_game(hero)

if __name__ == '__main__':
    main()