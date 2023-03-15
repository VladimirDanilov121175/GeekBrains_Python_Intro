from donut_factory_model import DonutFactory

factory = DonutFactory()


def eatDonut(filling):
    donut = factory.createDonut(filling)
    donut.eat(donut)


def countDonuts():
    factory.countDonuts()
