# coding: utf-8

from .observable import Observable


class WeatherData(Observable):

    def __init__(self):
        super().__init__()
        self._temperature = 0
        self._humidity = 0
        self._pressure = 0

    def get_temperature(self):
        return self._temperature

    def get_humidity(self):
        return self._humidity

    def get_pressure(self):
        return self._pressure
