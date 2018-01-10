# coding: utf-8

import sys
from io import StringIO

from unittest import TestCase
from lib.wether_data import WeatherData
from lib.display import CurrentConditionDisplay


class TestWeather(TestCase):

    @staticmethod
    def _clear_stdout():
        sys.stdout.close()
        sys.stdout = StringIO()

    def _print(self):
        self.org_stdout.write(sys.stdout.getvalue())

    def setUp(self):
        self.org_stdout, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        """
        :return:
        """
        # 退避していたsys.stdoutを戻す
        sys.stdout = self.org_stdout

    def test_update(self):
        weather_data = WeatherData()
        current_condition_display = CurrentConditionDisplay(weather_data)
        weather_data.set_measurements(temperature=20, humidity=50, pressure=900)
        self.assertEqual(sys.stdout.getvalue(), 'CurrentConditionDisplay: 20, 50\n')
