"""Proxy: контроль доступа к настоящему объекту."""


class Document:
    def read(self):
        print("Содержимое документа")


class DocumentProxy:
    def __init__(self, is_admin):
        self.is_admin = is_admin
        self.document = Document()

    def read(self):
        if self.is_admin:
            self.document.read()
        else:
            print("Доступ запрещён")


if __name__ == "__main__":
    DocumentProxy(is_admin=False).read()
    DocumentProxy(is_admin=True).read()
