"""Builder: пошаговая сборка компьютера."""


class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def build(self):
        computer = self.computer
        self.computer = Computer()
        return computer


if __name__ == "__main__":
    builder = ComputerBuilder()
    computer = builder.set_cpu("Intel Core i5").set_ram("16 GB").build()
    print("Процессор:", computer.cpu)
    print("Оперативная память:", computer.ram)
