# Aero snap still doesn't work https://bugreports.qt.io/browse/QTBUG-84466


from typing import Union

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt


class TitleBarIcon(QtWidgets.QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

        self.setStyleSheet("margin: 0;"
                           "padding: 0px;"
                           "font-size: 24px;"
                           "width: 58px;"
                           "height: 36px;")

        self.setContentsMargins(0, 0, 0, 0)


class CustomTitleBar(QtWidgets.QFrame):
    def __init__(self, window_widget: QtWidgets.QWidget):
        super().__init__(window_widget)

        self.window_widget = window_widget
        self.minimize_button = TitleBarIcon("🗕")
        self.maximize_button = TitleBarIcon("🗖")
        self.exit_button = TitleBarIcon("✕")

        self.minimize_button.clicked.connect(lambda: window_widget.setWindowState(Qt.WindowMinimized))
        self.maximize_button.clicked.connect(lambda: (window_widget.showNormal()
                                                      if window_widget.isMaximized()
                                                      else window_widget.showMaximized()))
        self.exit_button.clicked.connect(window_widget.close)

        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)

        self.layout.addSpacerItem(QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding))
        for widget in [
            self.minimize_button,
            self.maximize_button,
            self.exit_button,
        ]:
            self.layout.addWidget(widget)

        self.setStyleSheet("width: 100%;"
                           "padding: 0;"
                           "margin: 0;")
        self.setContentsMargins(0, 0, 0, 0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.window_widget.windowHandle().startSystemMove()


class ModernWindow(QtWidgets.QWidget):
    gripSize = 6

    def __init__(self, widget: QtWidgets.QWidget):
        super().__init__()

        # Remove window title bar and frame
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)

        self.title_bar = CustomTitleBar(self)
        self.main_widget = widget

        # Set up layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.title_bar)
        self.main_layout.addWidget(self.main_widget)

        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.grip_layout = QtWidgets.QGridLayout()

        self.grip_layout.addLayout(self.main_layout, 1, 1)
        self.grip_layout.addWidget(EdgeGrip(Qt.TopEdge), 0, 1)
        self.grip_layout.addWidget(EdgeGrip(Qt.RightEdge), 1, 2)
        self.grip_layout.addWidget(EdgeGrip(Qt.BottomEdge), 2, 1)
        self.grip_layout.addWidget(EdgeGrip(Qt.LeftEdge), 1, 0)
        self.grip_layout.addWidget(EdgeGrip(Qt.TopEdge | Qt.LeftEdge), 0, 0)
        self.grip_layout.addWidget(EdgeGrip(Qt.TopEdge | Qt.RightEdge), 0, 2)
        self.grip_layout.addWidget(EdgeGrip(Qt.BottomEdge | Qt.LeftEdge), 2, 0)
        self.grip_layout.addWidget(EdgeGrip(Qt.BottomEdge | Qt.RightEdge), 2, 2)

        self.grip_layout.setContentsMargins(0, 0, 0, 0)
        self.grip_layout.setSpacing(0)
        self.setLayout(self.grip_layout)


class EdgeGrip(QtWidgets.QWidget):
    def __init__(self, edges: Union[Qt.Edges, Qt.Edge], grip_size=6, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.edges = edges
        self.grip_size = grip_size
        # Sides
        if edges == Qt.TopEdge:
            self.setCursor(Qt.SizeVerCursor)
            self.setFixedHeight(self.grip_size)
        elif edges == Qt.RightEdge:
            self.setCursor(Qt.SizeHorCursor)
            self.setFixedWidth(self.grip_size)
        elif edges == Qt.BottomEdge:
            self.setCursor(Qt.SizeVerCursor)
            self.setFixedHeight(self.grip_size)
        elif edges == Qt.LeftEdge:
            self.setCursor(Qt.SizeHorCursor)
            self.setFixedWidth(self.grip_size)
        # Corners
        elif edges == Qt.TopEdge | Qt.LeftEdge:
            self.setCursor(Qt.SizeFDiagCursor)
        elif edges == Qt.TopEdge | Qt.RightEdge:
            self.setCursor(Qt.SizeBDiagCursor)
        elif edges == Qt.BottomEdge | Qt.LeftEdge:
            self.setCursor(Qt.SizeBDiagCursor)
        elif edges == Qt.BottomEdge | Qt.RightEdge:
            self.setCursor(Qt.SizeFDiagCursor)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.parent().windowHandle().startSystemResize(self.edges)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    main = QtWidgets.QMainWindow()

    content = QtWidgets.QTextEdit("Lorem Ipsum")
    main.setCentralWidget(content)

    window = ModernWindow(main)
    window.resize(900, 900)
    window.show()

    app.exec_()
