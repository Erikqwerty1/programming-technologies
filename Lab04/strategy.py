"""Strategy: выбор способа оплаты во время выполнения программы."""


class CardPayment:
    def pay(self, amount):
        print(f"Оплата картой: {amount} руб.")


class CashPayment:
    def pay(self, amount):
        print(f"Оплата наличными: {amount} руб.")


class Order:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        self.payment_strategy.pay(amount)


if __name__ == "__main__":
    order = Order(CardPayment())
    order.checkout(1000)

    order.payment_strategy = CashPayment()
    order.checkout(500)
