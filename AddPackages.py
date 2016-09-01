
import sys
import json
from pathlib import *

extraPackages = [
  "Alignment",
  "CMakeEditor",
  "EditorConfig",
  "FileDiffs",
  "Git",
  "GitGutter",
  "HexViewer",
  "IDL-Syntax",
  "Indent XML",
  "LaTeXTools",
  "Markdown Preview",
  "Monokai Extended",
  "Package Control",
  "PowerShell",
  "RevertFontSize",
  "SDLang",
  "SideBarEnhancements",
  "Theme - SoDaReloaded"
]

def main():
  thisDir = Path(__file__).parent.resolve()
  targetFile = thisDir.parent / "User" / "Package Control.sublime-settings"

  content = {}

  if targetFile.exists() and targetFile.is_file():
    # If the file already exists, load the content.
    with targetFile.open("r") as targetFileHandle:
      content = dict(json.load(targetFileHandle))
  else:
    # Otherwise create an empty list of "installed_packages"
    content["installed_packages"] = []

  # Add packages.
  content["installed_packages"].extend(extraPackages)

  # Remove duplicates.
  content["installed_packages"] = list(set(content["installed_packages"]))

  # Write the content back to file.
  with targetFile.open("w") as targetFileHandle:
    json.dump(content, targetFileHandle, indent=2)


if __name__ == '__main__':
  if len(sys.argv) > 1 and (sys.argv[1].startswith("-help") or sys.argv[1].startswith("--help")):
    print("Adds some package names to the \"installed_packages\" in `../User/Package Control.sublime-settings`")
    exit(1)
  main()
