from abc import ABCMeta, abstractmethod

import controller as c
from fillings_enum import Flavor


class ViewInterface(ABCMeta):
    """Interface for ConsoleView and WinView classes"""

    @abstractmethod
    def orderDonuts(self):
        pass


class ConsoleView(ViewInterface):

    def orderDonuts(self):
        print("Choose your flavor:")
        for flavor in Flavor:
            print("{:15} - {}".format(flavor.value, flavor.name))

        flavor = int(input(">>> "))
        amount = int(input("Set the amount >>> "))

        for i in range(amount):
            c.eatDonut(Flavor(flavor))

        c.countDonuts()


class WinView(ViewInterface):
    def orderDonuts(self):
        # TODO: realize window view
        pass
