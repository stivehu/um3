import os
import sys

from PyQt5 import QtWidgets, QtCore

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


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    translator = QtCore.QTranslator(app)

    translator.load(QtCore.QLocale.system().name() + ".qm",
                    find_data_file(QtCore.QLocale.system().name() + ".qm"))
    app.installTranslator(translator)

    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
