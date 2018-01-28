# coding: utf-8

import sys
from io import StringIO

from unittest import TestCase
from lib.chocolate_boiler import ChocolateBoiler


class TestChocolateBoiler(TestCase):

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

    def test_chocolate_boiler(self):
        boiler1 = ChocolateBoiler.get_instance()
        boiler1.fill()
        boiler1.drain()
        expected_value = """\
milk and chocolate into container!
milk and chocolate drain from container!
"""
        self.assertEqual(sys.stdout.getvalue(), expected_value)

    def test_chocolate_boiler2(self):
        boiler1 = ChocolateBoiler.get_instance()
        boiler2 = ChocolateBoiler.get_instance()
        self.assertEqual(boiler1, boiler2)

        boiler1.fill()
        boiler2.drain()
        expected_value = """\
milk and chocolate into container!
milk and chocolate drain from container!
"""
        self.assertEqual(sys.stdout.getvalue(), expected_value)

        self._clear_stdout()
        boiler2.fill()
        boiler1.drain()
        self.assertEqual(sys.stdout.getvalue(), expected_value)