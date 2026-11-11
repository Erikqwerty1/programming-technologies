"""Adapter: согласование несовместимых интерфейсов."""


class OldPrinter:
    def print_old(self, text):
        print(f"Старый принтер: {text}")


class PrinterAdapter:
    def __init__(self, printer):
        self.printer = printer

    def print_text(self, text):
        self.printer.print_old(text)


if __name__ == "__main__":
    printer = PrinterAdapter(OldPrinter())
    printer.print_text("Привет, мир!")
