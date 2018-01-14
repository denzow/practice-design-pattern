# coding: utf-8

from .base import CondimentDecorator


class Mocha(CondimentDecorator):

    def __init__(self, beverage):
        """
        :param .base.Beverage beverage:
        """

        super().__init__()
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ', モカ'

    def cost(self):
        return 0.2 + self._beverage.cost()


class Soy(CondimentDecorator):

    def __init__(self, beverage):
        """
        :param .base.Beverage beverage:
        """

        super().__init__()
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ', 豆乳'

    def cost(self):
        return 0.15 + self._beverage.cost()


class Whip(CondimentDecorator):

    def __init__(self, beverage):
        """
        :param .base.Beverage beverage:
        """

        super().__init__()
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ', ホイップ'

    def cost(self):
        return 0.1 + self._beverage.cost()

