# coding: utf-8

import sys
from io import StringIO

from unittest import TestCase
from lib.wether_data import WeatherData
from lib.display import CurrentConditionDisplay, StatisticsDisplay


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
        statistics_display = StatisticsDisplay(weather_data)
        weather_data.set_measurements(temperature=20, humidity=50, pressure=900)
        result = sys.stdout.getvalue()
        # 2つのDisplayの結果が含まれているか
        self.assertIn('CurrentConditionDisplay: 20, 50', result)
        self.assertIn('StatisticsDisplay: 20, 900', result)
        self._clear_stdout()

        # 更新後の結果で再表示されているか
        weather_data.set_measurements(temperature=30, humidity=60, pressure=910)
        result = sys.stdout.getvalue()
        self.assertIn('CurrentConditionDisplay: 30, 60', result)
        self.assertIn('StatisticsDisplay: 30, 910', result)
        self._clear_stdout()

