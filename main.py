from PyQt5 import QtWidgets
from Form import MainWindow
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = MainWindow()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
