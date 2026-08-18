import os
import sys

from PyQt6 import QtWidgets, QtCore, QtGui

from src.controller.ApplicationWindow import ApplicationWindow


def find_data_file(filename):
    if getattr(sys, "frozen", False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.join(os.path.dirname(__file__), "src", "messages")

    return datadir


def find_resource_file(filename):
    if getattr(sys, "frozen", False):
        datadir = os.path.dirname(sys.executable)
    else:
        datadir = os.path.join(os.path.dirname(__file__), "src", "resources")

    return os.path.join(datadir, filename)


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    app.setWindowIcon(QtGui.QIcon(find_resource_file("icon.png")))
    translator = QtCore.QTranslator(app)

    translator.load(QtCore.QLocale.system().name() + ".qm",
                    find_data_file(QtCore.QLocale.system().name() + ".qm"))
    app.installTranslator(translator)

    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
