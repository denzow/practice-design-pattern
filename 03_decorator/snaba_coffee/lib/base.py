# coding: utf-8

from abc import ABCMeta, abstractmethod


class Beverage(metaclass=ABCMeta):

    def __init__(self):
        self._description = '不明な飲み物'
        self._cost = 0

    def get_description(self):
        return self._description

    @abstractmethod
    def cost(self):
        pass


class CondimentDecorator(Beverage):

    @abstractmethod
    def get_description(self):
        pass
