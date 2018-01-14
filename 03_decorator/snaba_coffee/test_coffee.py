# coding: utf-8

import sys
from io import StringIO

from unittest import TestCase
from lib.beverages import (
    Espresso,
    HouseBlend,
    DarkRoast
)
from lib.topings import (
    Mocha,
    Whip,
    Soy
)

"""
P.98
"""


class TestCoffee(TestCase):

    def test_espresso(self):
        """
        ドリンク単体での動作テスト
        :return:
        """

        drink = Espresso()
        self.assertEqual(drink.get_description(), 'エスプレッソ')
        self.assertEqual(drink.cost(), 1.99)

    def test_topping_1(self):
        """
        トッピングのテストケース1
        :return:
        """
        drink = DarkRoast()
        drink = Mocha(drink)
        drink = Mocha(drink)
        drink = Whip(drink)
        self.assertEqual(drink.get_description(), 'ダークローストコーヒー, モカ, モカ, ホイップ')
        self.assertEqual(drink.cost(), 1.49)

    def test_topping_2(self):
        """
        トッピングのテストケース2
        :return:
        """
        drink = HouseBlend()
        drink = Soy(drink)
        drink = Mocha(drink)
        drink = Whip(drink)
        self.assertEqual(drink.get_description(), 'ハウスブレンドコーヒー, 豆乳, モカ, ホイップ')
        self.assertEqual(drink.cost(), 1.34)
