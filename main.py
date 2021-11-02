import os
import sys

from PyQt5 import QtWidgets, QtCore

from src.controller.ApplicationWindow import ApplicationWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    translator = QtCore.QTranslator(app)
    translator.load(QtCore.QLocale.system().name() + ".qm",
                    os.path.dirname(os.path.realpath(__file__)) + "/src/messages")
    app.installTranslator(translator)

    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
