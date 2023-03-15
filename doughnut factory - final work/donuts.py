from abc import ABCMeta, abstractmethod


class Donut(ABCMeta):
    """Parent class (interface)"""

    @abstractmethod
    def eat(self):
        pass


# region donuts with different fillings
class CherryDonut(Donut):
    def eat(self):
        print("You're eating a cherry donut!")


class ChocolateDonut(Donut):
    def eat(self):
        print("You're eating a chocolate donut!")


class AlmondDonut(Donut):
    def eat(self):
        print("You're eating an almond donut!")
# endregion
