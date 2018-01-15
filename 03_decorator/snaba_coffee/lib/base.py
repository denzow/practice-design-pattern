# coding: utf-8

import enum
from abc import ABCMeta, abstractmethod


class BeverageSize(enum.Enum):

    TALL = 1
    GRANDE = 2
    VENTI = 3


class Beverage(metaclass=ABCMeta):

    def __init__(self):
        self._description = '不明な飲み物'
        self._size = BeverageSize.GRANDE

    def get_description(self):
        return self._description

    def get_size(self):
        return self._size

    def set_size(self, size):
        """

        :param BeverageSize size:
        :return:
        """
        self._size = size

    @abstractmethod
    def cost(self):
        pass


class CondimentDecorator(Beverage):

    def __init__(self, beverage):
        """
        :param Beverage beverage:
        """
        self._beverage = beverage

    @abstractmethod
    def get_description(self):
        pass

    def get_size(self):
        return self._beverage.get_size()

    def set_size(self, size):
        return self._beverage.set_size(size)

