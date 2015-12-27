import sublime, sublime_plugin
from functools import reduce

class AddSpaceInplaceCommand(sublime_plugin.TextCommand):
  """
  Adds a space character to the right of all carets without
  moving the cursor.
  """

  def run(self, edit):
    v = self.view

    # Cannot do `regions = v.sel()` directly because v.sel() returns an instance
    # of `sublime.Selection` .
    regions = [ region for region in v.sel() ]
    v.sel().clear()

    for region in reversed(regions):
      # Replace selections with a single space character. Empty regions will
      # simply insert a space character.
      v.replace(edit, region, " ")

      caret = sublime.Region(region.begin(), region.begin())
      v.sel().add(caret)
