# coding: utf-8

from abc import ABCMeta, abstractmethod

from .pizza_factory import NYPizzaIngredientFactory
from .pizza import (
    CheesePizza,
    ClamPizza
)

class PizzaStore:

    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self, item):
        """
        :param item:
        :return:
        :rtype: lib.pizza.Pizza
        """
        pass


class NYPizzaStore(PizzaStore):

    def create_pizza(self, item):
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()
        if item == 'チーズ':
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name('NYスタイル野菜ピザ')
        elif item == 'クラム':
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name('NYスタイルクラムピザ')

        return pizza

