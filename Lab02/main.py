from abc import ABC, abstractmethod


class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass


class Moveable(ABC):
    @abstractmethod
    def move(self, x, y):
        pass


class GameObject:
    def __init__(self, object_id, name, x, y):
        self._id = object_id
        self._name = name
        self._x = x
        self._y = y

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


class Unit(GameObject):
    def __init__(self, object_id, name, x, y, hp):
        super().__init__(object_id, name, x, y)
        self._hp = hp

    def is_alive(self):
        return self._hp > 0

    def get_hp(self):
        return self._hp

    def receive_damage(self, damage):
        if damage < 0:
            raise ValueError("Урон не может быть отрицательным")

        self._hp = max(0, self._hp - damage)


class Archer(Unit, Attacker, Moveable):
    def attack(self, unit):
        if self.is_alive() and unit.is_alive():
            unit.receive_damage(10)

    def move(self, x, y):
        self._x = x
        self._y = y


class Building(GameObject):
    def __init__(self, object_id, name, x, y, built=False):
        super().__init__(object_id, name, x, y)
        self._built = built

    def is_built(self):
        return self._built


class Fort(Building, Attacker):
    def attack(self, unit):
        if self.is_built() and unit.is_alive():
            unit.receive_damage(20)


class MobileHouse(Building, Moveable):
    def move(self, x, y):
        self._x = x
        self._y = y


if __name__ == "__main__":
    # Создаём двух юнитов
    archer = Archer(1, "Archer", 0, 0, 100)
    enemy = Unit(2, "Enemy", 10, 10, 50)

    print("=== Проверка лучника ===")
    print("Имя:", archer.get_name())
    print("Здоровье:", archer.get_hp())
    print("Жив:", archer.is_alive())

    archer.attack(enemy)
    print("Здоровье врага после атаки:", enemy.get_hp())

    archer.move(5, 7)
    print("Новые координаты лучника:", archer.get_x(), archer.get_y())

    # Создаём крепость
    fort = Fort(3, "Fort", 20, 20, True)
    fort.attack(enemy)
    print("Здоровье врага после атаки крепости:", enemy.get_hp())

    # Создаём мобильный дом
    house = MobileHouse(4, "Mobile House", 30, 30, True)
    house.move(40, 50)
    print("Новые координаты дома:", house.get_x(), house.get_y())

    print("Крепость построена:", fort.is_built())
    print("Дом построен:", house.is_built())
