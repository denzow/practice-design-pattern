# coding: utf-8


from abc import ABCMeta, abstractmethod

from .ingredient import *


class PizzaIngredientFactory:

    @abstractmethod
    def create_dough(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_cheese(self):
        pass

    @abstractmethod
    def create_veggies(self):
        pass

    @abstractmethod
    def create_pepperoni(self):
        pass

    @abstractmethod
    def create_clam(self):
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    """
    NYスタイルのピザ食材ファクトリ
    """

    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_veggies(self):
        veggies = [
            Garlic(),
            Onion(),
            Mushroom(),
            RedPepper(),
        ]
        return veggies

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    """
    シカゴスタイル
    """

    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlamTomatoSauce()

    def create_cheese(self):
        return Mozzarella()

    def create_veggies(self):
        veggies = [
            EggPlant(),
            Spinach(),
            BlackOlives(),
        ]
        return veggies

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FrozenClams()

