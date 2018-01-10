# coding: utf-8

from .fly_behaviors import (
    FlyBehavior,
    FlyWithWings,
    FlyNoWay,
)
from .quack_behaviors import (
    QuackBehavior,
    Quack,
    Squeak,
)


class Duck:
    """
    Duck系基底クラス
    """

    def __init__(self):
        """
        実際のBehaviorはサブクラスで設定される
        """
        self.quack_behavior = None  # type: QuackBehavior
        self.fly_behavior = None    # type: FlyBehavior

    def swim(self):
        """
        共通
        :return:
        """
        print('{} is swimming.'.format(self.__class__.__name__))

    def display(self):
        """
        共通
        :return:
        """
        print('I am {}'.format(self.__class__.__name__))

    def perform_quack(self):
        """
        鳴き声。実際の処理はquack_behaviorに委ねる
        :return:
        """
        self.quack_behavior.quack()

    def perform_fly(self):
        """
        鳴き声。実際の処理はfly_behaviorに委ねる
        :return:
        """
        self.fly_behavior.fly()

    def set_quack_behavior(self, quack_behavior: QuackBehavior):
        """
        quack を差し替える
        :param quack_behavior:
        :return:
        """
        self.quack_behavior = quack_behavior

    def set_fly_behavior(self, fly_behavior: FlyBehavior):
        """
        fly を差し替える
        :param fly_behavior:
        :return:
        """
        self.fly_behavior = fly_behavior


class MallardDuck(Duck):
    """
    まがも
    とべるし、ぐぁぐぁする
    """
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print('I am magamo.')


class DecoyDuck(Duck):
    """
    デコイ
    とべないし、きゅーきゅーする
    """
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()

    def display(self):
        print('I am decoy.')
