# coding: utf-8

import sys
from io import StringIO

from unittest import TestCase
from lib.ducks import DecoyDuck, MallardDuck
from lib.fly_behaviors import FlyWithWings


class TestDucks(TestCase):

    @staticmethod
    def _clear_stdout():
        sys.stdout.close()
        sys.stdout = StringIO()

    def setUp(self):
        self.org_stdout, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        """
        :return:
        """
        # 退避していたsys.stdoutを戻す
        sys.stdout = self.org_stdout

    def test_perform_quack(self):
        """
        鳴き声のテスト
        :return:
        """
        decoy_duck = DecoyDuck()
        decoy_duck.perform_quack()
        self.assertEqual(sys.stdout.getvalue(), 'キューキュー\n')

        self._clear_stdout()

        mallard_duck = MallardDuck()
        mallard_duck.perform_quack()
        self.assertEqual(sys.stdout.getvalue(), 'くぁっくぁ\n')

    def test_perform_fly(self):
        """
        飛ぶテスト
        :return:
        """
        decoy_duck = DecoyDuck()
        decoy_duck.perform_fly()
        self.assertEqual(sys.stdout.getvalue(), '飛べない豚\n')

        self._clear_stdout()

        mallard_duck = MallardDuck()
        mallard_duck.perform_fly()
        self.assertEqual(sys.stdout.getvalue(), 'ばっさばっさ\n')

    def test_decoy_2_wing(self):
        """
        デコイダックに動的に翼を授ける。
        :return:
        """
        decoy_duck = DecoyDuck()
        decoy_duck.perform_fly()
        # 最初は飛べない
        self.assertEqual(sys.stdout.getvalue(), '飛べない豚\n')
        self._clear_stdout()
        decoy_duck.set_fly_behavior(FlyWithWings())

        decoy_duck.perform_fly()
        # 翼を授かった
        self.assertEqual(sys.stdout.getvalue(), 'ばっさばっさ\n')

