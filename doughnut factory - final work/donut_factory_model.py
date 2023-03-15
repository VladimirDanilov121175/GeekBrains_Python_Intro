from random import randint

from fillings_enum import Flavor
from donuts import *


class DonutFactory:

    def __init__(self):
        self.cherryCount = 0
        self.chocolateCount = 0
        self.almondCount = 0

    def createDonut(self, filling):
        match filling:
            case Flavor.CHERRY:
                self.cherryCount += 1
                return CherryDonut
            case Flavor.ALMOND:
                self.almondCount += 1
                return AlmondDonut
            case Flavor.CHOCOLATE:
                self.chocolateCount += 1
                return ChocolateDonut
            case Flavor.RANDOM:
                random_flavor = Flavor(randint(1, len(Flavor) - 1))
                return self.createDonut(random_flavor)
            case _:
                raise Exception("No such flavor available (((")

    def countDonuts(self):
        print("""Totally produced donuts:
        {} cherry donuts
        {} almond donuts
        {} chocolate donuts"""
              .format(self.cherryCount, self.almondCount, self.chocolateCount))
