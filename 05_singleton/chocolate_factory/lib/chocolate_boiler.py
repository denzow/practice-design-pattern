# coding: utf-8

from threading import Lock


class ChocolateBoiler:

    _unique_chocolate_boiler = None
    _lock = Lock()
    _empty = True
    _boiled = False

    def __new__(cls):
        raise NotImplementedError('ChocolateBoiler cannot initialize via Constructor')

    @classmethod
    def __internal_new__(cls):
        return super().__new__(cls)

    @classmethod
    def get_instance(cls):
        if not cls._unique_chocolate_boiler:
            with cls._lock:
                if not cls._unique_chocolate_boiler:
                    cls._unique_chocolate_boiler = cls.__internal_new__()

        return cls._unique_chocolate_boiler

    def fill(self):
        if self.is_empty():
            self._empty = False
            self._boiled = True
            print('milk and chocolate into container!')

    def drain(self):
        if (not self.is_empty()) and self.is_boiled():
            print('milk and chocolate drain from container!')
            self._empty = True

    def is_empty(self):
        return self._empty

    def is_boiled(self):
        return self._boiled




