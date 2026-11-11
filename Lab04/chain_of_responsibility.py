"""Chain of Responsibility: последовательная обработка запроса."""


class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, amount):
        if self.next_handler is not None:
            self.next_handler.handle(amount)
        else:
            print("Запрос не обработан")


class Manager(Handler):
    def handle(self, amount):
        if amount <= 1000:
            print("Менеджер одобрил запрос")
        else:
            super().handle(amount)


class Director(Handler):
    def handle(self, amount):
        if amount <= 10000:
            print("Директор одобрил запрос")
        else:
            super().handle(amount)


if __name__ == "__main__":
    handler = Manager(Director())
    handler.handle(500)
    handler.handle(5000)
    handler.handle(20000)
