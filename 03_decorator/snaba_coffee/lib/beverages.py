# coding: utf-8

from .base import Beverage, BeverageSize


class Espresso(Beverage):

    def __init__(self):
        super().__init__()
        self._description = 'エスプレッソ'

    def cost(self):
        if self._size == BeverageSize.TALL:
            return 1.79
        elif self._size == BeverageSize.GRANDE:
            return 1.99
        elif self._size == BeverageSize.VENTI:
            return 2.19


class HouseBlend(Beverage):

    def __init__(self):
        super().__init__()
        self._description = 'ハウスブレンドコーヒー'

    def cost(self):
        if self._size == BeverageSize.TALL:
            return 0.79
        elif self._size == BeverageSize.GRANDE:
            return 0.89
        elif self._size == BeverageSize.VENTI:
            return 0.99


class DarkRoast(Beverage):
    def __init__(self):
        super().__init__()
        self._description = 'ダークローストコーヒー'

    def cost(self):
        if self._size == BeverageSize.TALL:
            return 0.89
        elif self._size == BeverageSize.GRANDE:
            return 0.99
        elif self._size == BeverageSize.VENTI:
            return 1.09


