# coding: utf-8

import sys
from io import StringIO

from unittest import TestCase
from lib.pizza_store import NYPizzaStore, ChicagoPizzaStore


class TestWeather(TestCase):

    @staticmethod
    def _clear_stdout():
        sys.stdout.close()
        sys.stdout = StringIO()

    def _print(self):
        self.org_stdout.write(sys.stdout.getvalue())

    def setUp(self):
        """

        :return:
        """
        self.org_stdout, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        """
        :return:
        """
        # 退避していたsys.stdoutを戻す
        sys.stdout = self.org_stdout

    def test_pizza(self):

        ny_pizza_store = NYPizzaStore()
        chicago_pizza_store = ChicagoPizzaStore()

        ny_cheese_pizza = ny_pizza_store.order_pizza('チーズ')
        chicago_cheese_pizza = chicago_pizza_store.order_pizza('チーズ')
        expected_output = """\
NYスタイルチーズピザを下処理
350度で25分間焼く
ピザを扇型に切り分ける
PizzaStoreの正式な箱にピザを入れる
シカゴスタイルチーズピザを下処理
350度で25分間焼く
ピザを扇型に切り分ける
PizzaStoreの正式な箱にピザを入れる
"""
        self.assertEqual(sys.stdout.getvalue(), expected_output)

        self.assertEqual(ny_cheese_pizza.get_name(), 'NYスタイルチーズピザ')
        self.assertEqual(chicago_cheese_pizza.get_name(), 'シカゴスタイルチーズピザ')

