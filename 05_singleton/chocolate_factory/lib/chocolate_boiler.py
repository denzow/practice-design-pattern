# coding: utf-8


class ChocolateBoiler:

    def __init__(self):
        self._empty = True
        self._boiled = False

    def fill(self):
        if self.is_empty():
            self._empty = False
            self._boiled = True
            # TODO

    def drain(self):
        if self.is_empty() and self.is_boiled():
            # TODO
            self._empty = True

    def is_empty(self):
        return self._empty

    def is_boiled(self):
        return self._boiled




