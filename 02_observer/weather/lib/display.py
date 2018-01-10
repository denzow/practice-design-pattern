# coding: utf-8

from .observable import Observer, Observable


class CurrentConditionDisplay(Observer):

    def __init__(self, observable: Observable):
        super().__init__()
        self._observable = observable
        self._observable.add_observer(self)
        self._temperature = None
        self._humidity = None

    def update(self, notified_observable: Observable, *args, **kwargs):
        self._temperature = notified_observable.get_temperature()
        self._humidity = notified_observable.get_humidity()
        self.display()

    def display(self):
        print('CurrentConditionDisplay: {}, {}'.format(self._temperature, self._humidity))
