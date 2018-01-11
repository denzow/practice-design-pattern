# coding: utf-8

from .observable import Observer, Observable


class CurrentConditionDisplay(Observer):
    """
    Displayの実装その1
    """

    def __init__(self, observable: Observable):
        super().__init__()
        self._observable = observable
        # observableに自身を登録する
        self._observable.add_observer(self)
        self._temperature = None
        self._humidity = None

    def update(self, notified_observable: Observable, *args, **kwargs):
        # 温度情報等を更新して再表示
        self._temperature = notified_observable.get_temperature()
        self._humidity = notified_observable.get_humidity()
        self.display()

    def display(self):
        print('CurrentConditionDisplay: {}, {}'.format(self._temperature, self._humidity))


class StatisticsDisplay(Observer):
    """
    Displayの実装その2
    """

    def __init__(self, observable: Observable):
        super().__init__()
        self._observable = observable
        # observableに自身を登録する
        self._observable.add_observer(self)
        self._temperature = None
        self._pressure = None

    def update(self, notified_observable: Observable, *args, **kwargs):
        # 温度情報等を更新して再表示
        self._temperature = notified_observable.get_temperature()
        self._pressure = notified_observable.get_pressure()
        self.display()

    def display(self):
        print('StatisticsDisplay: {}, {}'.format(self._temperature, self._pressure))
