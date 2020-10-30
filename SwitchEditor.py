import sublime
import sublime_plugin
import subprocess
from shutil import which
import sys


settings_key = 'switch-editor.last'
VSCODE = 'vscode'

CREATE_NO_WINDOW = 134217728
DETACHED_PROCESS = 8


class SwitchEditor(sublime_plugin.TextCommand):
    def run(self, edit, ask=False):
        if not self.view.file_name():
            return

        settings = self.view.window().settings()
        last_editor = settings.get(settings_key, None)
        if not last_editor or ask:
            choices = [VSCODE]
            def callback(selected_index):
                if selected_index < 0:
                    return # was cancelled
                choice = choices[selected_index]
                if self.do_switch_editor(choice):
                    settings.set(settings_key, choice)
            self.view.window().show_quick_panel([VSCODE], callback)
            return

        self.do_switch_editor(last_editor)

    def do_switch_editor(self, editor_type):
        file = self.view.file_name()
        cursor_point = self.view.sel()[0].b
        line, column = self.view.rowcol(cursor_point)

        result = True
        if editor_type == VSCODE:
            cmd = [
                which('code'),
                '-g', '{}:{}:{}'.format(file, line + 1, column + 1)
            ]
            subprocess.call(cmd, creationflags=CREATE_NO_WINDOW|DETACHED_PROCESS)
        else:
            print('Unknown editor to switch to:', editor_type)
            result = False

        return result
