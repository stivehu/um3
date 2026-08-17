import sys
from cx_Freeze import setup, Executable

try:
    from cx_Freeze.hooks import get_qt_plugins_paths
except ImportError:
    get_qt_plugins_paths = None

import os

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
translate = os.path.join(os.path.dirname(__file__), "src", "messages", "hu_HU.qm")
include_files = [translate]
if get_qt_plugins_paths:
    # Inclusion of extra plugins (since cx_Freeze 6.8b2)
    # cx_Freeze imports automatically the following plugins depending of the
    # use of some modules:
    # imageformats, platforms, platformthemes, styles - QtGui
    # mediaservice - QtMultimedia
    # printsupport - QtPrintSupport
    for plugin_name in (
         "accessible",
         "iconengines",
         "webview",
        # "platforminputcontexts",
        # "xcbglintegrations",
        # "egldeviceintegrations",
        "wayland-decoration-client",
        "wayland-graphics-integration-client",
        # "wayland-graphics-integration-server",
        "wayland-shell-integration",
    ):
        include_files += get_qt_plugins_paths("PyQt6", plugin_name)
        print (include_files)
include_files = [
    (os.path.join(os.path.dirname(sys.executable), 'Library', 'plugins'), 'plugins')
]        


build_exe_options = {"excludes": ["tkinter"], "include_files": [include_files], "optimize": 2}
bdist_msi_options = {
    "all_users": True
}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="um3",
    version="0.6",
    description="User manager 3",
    options={"build_exe": build_exe_options,
             "bdist_msi": bdist_msi_options},
    executables=[Executable("main.py", base=base, shortcut_name="Nevező kezelő", shortcut_dir="DesktopFolder", )]
)
