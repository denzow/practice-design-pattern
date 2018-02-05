# coding: utf-8

from abc import ABC, abstractmethod


class Pizza(ABC):

    def __init__(self, ingredient_factory):
        """
        :param lib.pizza_factory.PizzaIngredientFactory ingredient_factory:
        """
        self._ingredient_factory = ingredient_factory
        self._name = None
        self._dough = None
        self._sauce = None
        self._veggies = []
        self._cheese = None
        self._pepperoni = None
        self._clam = None

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print('350度で25分間焼く')

    def cut(self):
        print('ピザを扇型に切り分ける')

    def box(self):
        print('PizzaStoreの正式な箱にピザを入れる')

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


class CheesePizza(Pizza):

    def prepare(self):
        print('{}を下処理'.format(self._name))
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()


class ClamPizza(Pizza):

    def prepare(self):
        print('{}を下処理'.format(self._name))
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._clam = self._ingredient_factory.create_clam()

