from abc import ABC, abstractmethod
from random import randint, choice


class Item(ABC):

    def __init__(self, name, health=300):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self, another):
        pass


class Sword(Item):

    def __init__(self, name, attack_power):
        super().__init__(name)

        self.__attack_power = attack_power
        self._sharp = 0

    def attack(self, another):
        damage = self.__attack_power + self._sharp + randint(0, 10)

        another.health -= damage

        return f"⚔️ Меч {self.name} наніс {damage} шкоди"

    def sharpening(self):
        self._sharp += 1


class Axe(Item):

    def __init__(self, name, attack_power):
        super().__init__(name)

        self.__attack_power = attack_power

    def attack(self, another):
        damage = self.__attack_power + randint(0, 20)

        another.health -= damage

        return f"🪓 Сокира {self.name} нанесла {damage} шкоди"

    def strengthen(self):
        self.__attack_power += 2


class Bow(Item):

    def __init__(self, name, attack_power, range_power):
        super().__init__(name)

        self.__attack_power = attack_power
        self.range_power = range_power

    def attack(self, another):
        damage = self.__attack_power + randint(5, 15) + self.range_power

        another.health -= damage

        return f"🏹 Лук {self.name} наніс {damage} шкоди"

    def reload(self):
        self.range_power += 1


# Створюємо зброю
weapons = [
    Sword("Ескалібур", 90),
    Axe("Кратос", 85),
    Bow("Мисливець", 80, 10)
]

# Випадковий вибір зброї
player = choice(weapons)

enemy = choice([
    Sword("Ворог-Меч", 90),
    Axe("Ворог-Сокира", 85),
    Bow("Ворог-Лук", 80, 10)
])

print("=" * 40)
print("ПОЧАТОК ГРИ")
print("=" * 40)

print(f"Ваша зброя: {player.name}")
print(f"Зброя ворога: {enemy.name}")

while player.health > 0 and enemy.health > 0:

    print("\nВаше здоров'я:", player.health)
    print("Здоров'я ворога:", enemy.health)

    print("\n1 - Атакувати")
    print("2 - Підсилити зброю")

    action = input("Оберіть дію: ")

    if action == "1":
        print(player.attack(enemy))

    elif action == "2":

        if isinstance(player, Sword):
            player.sharpening()
            print("⚔️ Меч заточено!")

        elif isinstance(player, Axe):
            player.strengthen()
            print("🪓 Сокиру підсилено!")

        elif isinstance(player, Bow):
            player.reload()
            print("🏹 Лук перезаряджено!")

    else:
        print("Невірна команда!")
        continue

    if enemy.health <= 0:
        print("\n🎉 Перемога гравця!")
        break

    print(enemy.attack(player))

    if player.health <= 0:
        print("\n💀 Переміг ворог!")
        break

print("\nГру завершено.")
