# coding: utf-8

from abc import ABCMeta, abstractmethod


class QuackBehavior(metaclass=ABCMeta):

    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):

    def quack(self):
        print('くぁっくぁ')


class Squeak(QuackBehavior):

    def quack(self):
        print('キューキュー')
