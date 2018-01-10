# coding: utf-8

from abc import ABCMeta, abstractmethod


class FlyBehavior(metaclass=ABCMeta):

    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):

    def fly(self):
        print('ばっさばっさ')


class FlyNoWay(FlyBehavior):

    def fly(self):
        print('飛べない豚')
