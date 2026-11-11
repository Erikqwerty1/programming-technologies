"""Bridge: отделение управления от способа выполнения."""


class TV:
    def turn_on(self):
        print("Телевизор включён")


class Radio:
    def turn_on(self):
        print("Радио включено")


class Remote:
    def __init__(self, device):
        self.device = device

    def press_power(self):
        self.device.turn_on()


if __name__ == "__main__":
    Remote(TV()).press_power()
    Remote(Radio()).press_power()
