import sublime, sublime_plugin

class AddSpaceInplaceCommand(sublime_plugin.TextCommand):
  """
  Adds a space character to the right of all carets without
  moving the cursor. Selections will be left untouched.
  """

  def run(self, edit):
    for region in self.view.sel():
      if region.empty():
        self.view.insert(edit, region.begin(), " ")
