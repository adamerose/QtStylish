from qtstylish import DemoWidget, ThemeSwitcher
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import os

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    dw = DemoWidget()
    dw.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    ts = ThemeSwitcher(dw, hot_reload=True)

    ts.resize(1000, 700)
    app.exec_()
