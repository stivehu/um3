from PyQt5 import QtWidgets
from src.controller.ApplicationWindow import ApplicationWindow
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

