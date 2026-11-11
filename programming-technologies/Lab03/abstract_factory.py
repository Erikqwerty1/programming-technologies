"""Abstract Factory: создание семейств мебели одного стиля."""


class ModernChair:
    def sit(self):
        print("Современный стул")


class ClassicChair:
    def sit(self):
        print("Классический стул")


class ModernTable:
    def use(self):
        print("Современный стол")


class ClassicTable:
    def use(self):
        print("Классический стол")


class FurnitureFactory:
    def create_chair(self):
        raise NotImplementedError

    def create_table(self):
        raise NotImplementedError


class ModernFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_table(self):
        return ModernTable()


class ClassicFactory(FurnitureFactory):
    def create_chair(self):
        return ClassicChair()

    def create_table(self):
        return ClassicTable()


if __name__ == "__main__":
    for factory in (ModernFactory(), ClassicFactory()):
        factory.create_chair().sit()
        factory.create_table().use()
