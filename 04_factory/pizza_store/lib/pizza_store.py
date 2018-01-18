# coding: utf-8

from abc import ABCMeta, abstractmethod

class PizzaStore:

    def __init__(self):
        self._pizza = None
        self._pizza_ingredient_factory = None
