# coding: utf-8


class Beverage:

    def __init__(self):
        self._description = None
        self._cost = 0

    def get_description(self):
        return self._description

    def cost(self):
        return self._cost

