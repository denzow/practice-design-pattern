# coding: utf-8

from .base import CondimentDecorator, BeverageSize


class Mocha(CondimentDecorator):

    def get_description(self):
        return self._beverage.get_description() + ', モカ'

    def cost(self):
        size = self.get_size()
        additional_cost = 0
        if size == BeverageSize.TALL:
            additional_cost = 0.15
        elif size == BeverageSize.GRANDE:
            additional_cost = 0.2
        elif size == BeverageSize.VENTI:
            additional_cost = 0.25

        return additional_cost + self._beverage.cost()


class Soy(CondimentDecorator):

    def get_description(self):
        return self._beverage.get_description() + ', 豆乳'

    def cost(self):
        size = self.get_size()
        additional_cost = 0
        if size == BeverageSize.TALL:
            additional_cost = 0.10
        elif size == BeverageSize.GRANDE:
            additional_cost = 0.15
        elif size == BeverageSize.VENTI:
            additional_cost = 0.20

        return additional_cost + self._beverage.cost()


class Whip(CondimentDecorator):

    def get_description(self):
        return self._beverage.get_description() + ', ホイップ'

    def cost(self):
        size = self.get_size()
        additional_cost = 0
        if size == BeverageSize.TALL:
            additional_cost = 0.05
        elif size == BeverageSize.GRANDE:
            additional_cost = 0.1
        elif size == BeverageSize.VENTI:
            additional_cost = 0.15

        return additional_cost + self._beverage.cost()
