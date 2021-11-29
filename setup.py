import sys
from cx_Freeze import setup, Executable
import os

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
translate = os.path.join(os.path.dirname(__file__), "src", "messages", "hu_HU.qm")
build_exe_options = {"excludes": ["tkinter"], "include_files": [translate], "optimize": 2}
bdist_msi_options = {
    "all_users": True
}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="um3",
    version="0.2",
    description="User manager 3",
    options={"build_exe": build_exe_options,
             "bdist_msi": bdist_msi_options},
    executables=[Executable("main.py", base=base, shortcut_name="Nevező kezelő", shortcut_dir="DesktopFolder", )]
)
