import sublime
import sublime_plugin
import time

class InsertCurrentTime(sublime_plugin.TextCommand):
  def run(self, edit, fmt="%Y-%m-%d %H:%M"):
    formattedTime = time.strftime(fmt, time.localtime())
    for reg in self.view.sel():
      self.view.insert(edit, reg.a, formattedTime)
