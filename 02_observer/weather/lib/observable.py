# coding: utf-8
"""
Observerパターンに必要な基底クラスの定義
"""


from abc import abstractmethod


class Observer:

    def __init__(self, observable: Observable):
        self._observable = observable
        self._observable.add_observer(self)

    @abstractmethod
    def update(self, notified_observable: Observable, *args, **kwargs):
        """
        need implement by subClasses.
        """


class Observable:
    """
    オブザーバル(パブリッシャ)側の基底クラス
    """

    def __init__(self):
        self._is_changed = False
        self._observer_list = []  # type: [Observer, ]

    def add_observer(self, observer: Observer):
        """
        オブザーバの登録
        :param observer:
        :return:
        """
        self._observer_list.append(observer)

    def del_observer(self, observer: Observer):
        """
        オブザーバの解除
        :param observer:
        :return:
        """
        if observer in self._observer_list:
            self._observer_list.remove(observer)

    def set_changed(self):
        """
        変更状態の設定
        :return:
        """
        self._is_changed = True

    def has_changed(self):
        return self._is_changed

    def notify_observers(self):
        """
        変更下であれば各オブザーバに通知する
        :return:
        """
        if self._is_changed:
            self._is_changed = False
            for observer in self._observer_list:
                observer.update()



