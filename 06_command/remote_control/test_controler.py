# coding: utf-8

import sys
from io import StringIO

from unittest import TestCase
from lib.control import RemoteControl
from lib.receiver import *
from lib.command import *


class TestRemoteControl(TestCase):

    @staticmethod
    def _clear_stdout():
        sys.stdout.close()
        sys.stdout = StringIO()

    def _print(self):
        self.org_stdout.write(sys.stdout.getvalue())

    def setUp(self):
        """

        :return:
        """
        self.org_stdout, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        """
        :return:
        """
        # 退避していたsys.stdoutを戻す
        sys.stdout = self.org_stdout

    def test_fan(self):
        remote_control = RemoteControl()
        ceiling_fan = CeilingFan('リビングルーム')
        ceiling_fan_medium_command = CeilingFanMediumCommand(ceiling_fan)
        ceiling_fan_high_command = CeilingFanHighCommand(ceiling_fan)
        ceiling_fan_off_command = CeilingFanOffCommand(ceiling_fan)

        remote_control.set_command(
            slot_no=0,
            on_command=ceiling_fan_medium_command,
            off_command=ceiling_fan_off_command,
        )
        remote_control.set_command(
            slot_no=1,
            on_command=ceiling_fan_high_command,
            off_command=ceiling_fan_off_command,
        )
        remote_control.on_button_was_pushed(0)
        remote_control.off_button_was_pushed(0)
        print(remote_control)
        self.assertEqual(sys.stdout.getvalue(), """\
リビングルーム 天井の扇風機の強さは「中」です
リビングルーム 天井の扇風機の強さは「オフ」です

------- リモコン -------
[スロット 0] CeilingFanMediumCommand CeilingFanOffCommand
[スロット 1] CeilingFanHighCommand CeilingFanOffCommand
[スロット 2] NoCommand NoCommand
[スロット 3] NoCommand NoCommand
[スロット 4] NoCommand NoCommand
[スロット 5] NoCommand NoCommand
[スロット 6] NoCommand NoCommand
[アンドゥ] CeilingFanOffCommand

""")
        self._clear_stdout()
        remote_control.undo_button_was_pushed()
        remote_control.on_button_was_pushed(1)
        print(remote_control)
        self.assertEqual(sys.stdout.getvalue(), """\
リビングルーム 天井の扇風機の強さは「中」です
リビングルーム 天井の扇風機の強さは「強」です

------- リモコン -------
[スロット 0] CeilingFanMediumCommand CeilingFanOffCommand
[スロット 1] CeilingFanHighCommand CeilingFanOffCommand
[スロット 2] NoCommand NoCommand
[スロット 3] NoCommand NoCommand
[スロット 4] NoCommand NoCommand
[スロット 5] NoCommand NoCommand
[スロット 6] NoCommand NoCommand
[アンドゥ] CeilingFanHighCommand

""")
        self._clear_stdout()
        remote_control.undo_button_was_pushed()
        self.assertEqual(sys.stdout.getvalue(), """\
リビングルーム 天井の扇風機の強さは「中」です
""")





