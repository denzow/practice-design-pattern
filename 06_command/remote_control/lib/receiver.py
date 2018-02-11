# coding: utf-8


class Light:

    def __init__(self, light_name: str):

        self._light_name = light_name

    def on(self):
        print('{} 照明がついています'.format(self._light_name))

    def off(self):
        print('{} 照明が消えています'.format(self._light_name))


class CeilingFan:
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0

    def __init__(self, location):
        self._location = location
        self._speed = self.OFF

    def high(self):
        self._speed = self.HIGH
        self._display_status()

    def medium(self):
        self._speed = self.MEDIUM
        self._display_status()

    def low(self):
        self._speed = self.LOW
        self._display_status()

    def off(self):
        self._speed = self.OFF
        self._display_status()

    def _display_status(self):
        speed_map = {
            self.HIGH: '強',
            self.MEDIUM: '中',
            self.LOW: '低',
            self.OFF: 'オフ',
        }

        print('{location} 天井の扇風機の強さは「{speed}」です'.format(
            location=self._location,
            speed=speed_map[self.get_speed()]
        ))

    def get_speed(self):
        return self._speed

