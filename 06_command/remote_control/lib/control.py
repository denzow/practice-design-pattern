# coding: utf-8

from .command import NoCommand


class RemoteControl:

    def __init__(self):
        # 7つのスロットをNoCommandで初期化
        self._on_commands = [NoCommand() for _ in range(7)]
        self._off_commands = [NoCommand() for _ in range(7)]
        self._undo_command = NoCommand()

    def __str__(self):
        response = '\n------- リモコン -------\n'
        for i, (on, off) in enumerate(zip(self._on_commands, self._off_commands)):
            response += '[スロット {no}] {on_class_name} {off_class_name}\n'.format(
                no=i,
                on_class_name=on.__class__.__name__,
                off_class_name=off.__class__.__name__
            )
        response += '[アンドゥ] {undo_command}\n'.format(
            undo_command=self._undo_command.__class__.__name__
        )
        return response

    def set_command(self, slot_no: int, on_command, off_command):
        self._on_commands[slot_no] = on_command
        self._off_commands[slot_no] = off_command

    def on_button_was_pushed(self, slot_no: int):
        self._on_commands[slot_no].execute()
        self._undo_command = self._on_commands[slot_no]

    def off_button_was_pushed(self, slot_no: int):
        self._off_commands[slot_no].execute()
        self._undo_command = self._off_commands[slot_no]

    def undo_button_was_pushed(self):
        self._undo_command.undo()
