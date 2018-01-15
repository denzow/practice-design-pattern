# coding: utf-8

from unittest import TestCase
from lib.base import BeverageSize
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

TODO
サイズも追加する

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
        drink = DarkRoast()   # 0.99
        drink = Mocha(drink)  # 0.2
        drink = Mocha(drink)  # 0.2
        drink = Whip(drink)   # 0.1
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

    def test_size(self):
        """
        size変更時の場合の価格
        :return:
        """
        drink = HouseBlend()  # 0.99
        drink = Soy(drink)    # 0.2
        drink = Mocha(drink)  # 0.25
        drink = Whip(drink)   # 0.15
        drink.set_size(BeverageSize.VENTI)
        self.assertEqual(drink.get_description(), 'ハウスブレンドコーヒー, 豆乳, モカ, ホイップ')
        # float 加算でずれたので・・
        self.assertTrue(1.58 <= drink.cost() <= 1.59)

        drink.set_size(BeverageSize.TALL)
        # 0.79 + 0.10 + 0.15 + 0.05
        self.assertTrue(drink.cost(), 1.09)
