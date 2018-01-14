# coding: utf-8

from .base import Beverage


class Espresso(Beverage):

    def __init__(self):
        super().__init__()
        self._description = 'エスプレッソ'

    def cost(self):
        return 1.99


class HouseBlend(Beverage):

    def __init__(self):
        super().__init__()
        self._description = 'ハウスブレンドコーヒー'

    def cost(self):
        return 0.89


class DarkRoast(Beverage):
    def __init__(self):
        super().__init__()
        self._description = 'ダークローストコーヒー'

    def cost(self):
        return 0.99


