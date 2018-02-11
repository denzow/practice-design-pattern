# coding: utf-8

import abc


class Command(abc.ABC):

    @abc.abstractmethod
    def execute(self):
        pass

    @abc.abstractmethod
    def undo(self):
        pass


class NoCommand(Command):
    """
    NULLオブジェクト
    """
    def execute(self):
        print('NoCommand execute')

    def undo(self):
        print('NoCommand undo')


class LightOnCommand(Command):

    def __init__(self, light):
        """
        :param lib.receiver.Light light:
        """
        self._light = light

    def execute(self):
        self._light.on()

    def undo(self):
        self._light.off()


class LightOffCommand(Command):

    def __init__(self, light):
        """
        :param lib.receiver.Light light:
        """
        self._light = light

    def execute(self):
        self._light.off()

    def undo(self):
        self._light.on()


class CeilingFanCommand(Command):
    """
    CeilingFanは高中低、OFFの4種のコマンドを持つので
    そのベースクラスを設ける
    """

    def __init__(self, ceiling_fan):
        """
        :param lib.receiver.CeilingFan ceiling_fan:
        """
        self._ceiling_fan = ceiling_fan
        self._prev_speed = None

    @abc.abstractmethod
    def execute(self):
        pass

    def undo(self):
        action_map = {
            self._ceiling_fan.HIGH: self._ceiling_fan.high,
            self._ceiling_fan.MEDIUM: self._ceiling_fan.medium,
            self._ceiling_fan.LOW: self._ceiling_fan.low,
            self._ceiling_fan.OFF: self._ceiling_fan.off,
        }
        action_map[self._prev_speed]()


class CeilingFanHighCommand(CeilingFanCommand):

    def execute(self):
        self._prev_speed = self._ceiling_fan.get_speed()
        self._ceiling_fan.high()


class CeilingFanMediumCommand(CeilingFanCommand):

    def execute(self):
        self._prev_speed = self._ceiling_fan.get_speed()
        self._ceiling_fan.medium()


class CeilingFanLowCommand(CeilingFanCommand):

    def execute(self):
        self._prev_speed = self._ceiling_fan.get_speed()
        self._ceiling_fan.low()


class CeilingFanOffCommand(CeilingFanCommand):

    def execute(self):
        self._prev_speed = self._ceiling_fan.get_speed()
        self._ceiling_fan.off()



