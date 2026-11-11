"""Singleton: один экземпляр настроек приложения."""


class Settings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == "__main__":
    first = Settings()
    second = Settings()
    print("Один и тот же объект:", first is second)
