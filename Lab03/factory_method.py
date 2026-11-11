"""Factory Method: создание транспорта через подклассы фабрики."""


class Car:
    def drive(self):
        print("Едет автомобиль")


class Bike:
    def drive(self):
        print("Едет велосипед")


class TransportFactory:
    def create_transport(self):
        raise NotImplementedError


class CarFactory(TransportFactory):
    def create_transport(self):
        return Car()


class BikeFactory(TransportFactory):
    def create_transport(self):
        return Bike()


if __name__ == "__main__":
    for factory in (CarFactory(), BikeFactory()):
        transport = factory.create_transport()
        transport.drive()
