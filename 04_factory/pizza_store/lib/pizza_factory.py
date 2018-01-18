# coding: utf-8


from abc import ABCMeta, abstractmethod


class PizzaIngredientFactory:

    @abstractmethod
    def create_dough(self):
        pass

    @abstractmethod
    def create_source(self):
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


    def create_dough(self):
        return