from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import *

try:
    from pandasgui import show
    from pandasgui.datasets import pokemon, mi_manufacturing
except:
    pass


class DemoWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.tabs = QTabWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)

        #########################
        # Reusable stuff
        icon = self.style().standardIcon(QtWidgets.QStyle.SP_VistaShield)
        scene = QGraphicsScene()
        scene.addEllipse(10, 10, 100, 100, QtGui.QPen(
            Qt.black), QtGui.QBrush(Qt.red))
        scene.addRect(-10, -10, 50, 50, QtGui.QPen(Qt.black),
                      QtGui.QBrush(Qt.green))

        #########################
        # Buttons (QRadioButton, QCheckBox, QPushButton, QToolButton, QCommandLinkButton)
        buttons_layout = QGridLayout()
        buttons_container = QWidget()
        buttons_container.setLayout(buttons_layout)
        self.tabs.addTab(buttons_container, "Buttons")
        buttons_layout.addWidget(QLabel("Enabled"), 0, 1)
        buttons_layout.addWidget(QLabel("Disabled"), 0, 2)
        buttons_layout.setRowStretch(999, 1)

        row = 1
        # QRadioButton (checked)
        buttons_layout.addWidget(QLabel("QRadioButton (checked)"), row, 0)

        x = QRadioButton("Lorem Ipsum")
        x.setEnabled(True)
        x.setChecked(True)
        buttons_layout.addWidget(x, row, 1)

        x = QRadioButton("Lorem Ipsum")
        x.setEnabled(False)
        x.setChecked(True)
        buttons_layout.addWidget(x, row, 2)

        row += 1
        # QRadioButton (unchecked)
        buttons_layout.addWidget(QLabel("QRadioButton (unchecked)"), row, 0)

        x = QRadioButton("Lorem Ipsum")
        x.setEnabled(True)
        x.setChecked(False)
        buttons_layout.addWidget(x, row, 1)

        x = QRadioButton("Lorem Ipsum")
        x.setEnabled(False)
        x.setChecked(False)
        buttons_layout.addWidget(x, row, 2)

        row += 1
        # QCheckBox (checked)
        buttons_layout.addWidget(QLabel("QCheckBox (checked)"), row, 0)

        x = QCheckBox("Lorem Ipsum")
        x.setEnabled(True)
        x.setChecked(True)
        buttons_layout.addWidget(x, row, 1)

        x = QCheckBox("Lorem Ipsum")
        x.setEnabled(False)
        x.setChecked(True)
        buttons_layout.addWidget(x, row, 2)

        row += 1
        # QCheckBox (unchecked)
        buttons_layout.addWidget(QLabel("QCheckBox (unchecked)"), row, 0)

        x = QCheckBox("Lorem Ipsum")
        x.setEnabled(True)
        x.setChecked(False)
        buttons_layout.addWidget(x, row, 1)

        x = QCheckBox("Lorem Ipsum")
        x.setEnabled(False)
        x.setChecked(False)
        buttons_layout.addWidget(x, row, 2)

        row += 1
        # QCheckBox (tristate)
        buttons_layout.addWidget(QLabel("QCheckBox (tristate)"), row, 0)

        x = QCheckBox("Lorem Ipsum")
        x.setEnabled(True)
        x.setCheckState(Qt.PartiallyChecked)
        buttons_layout.addWidget(x, row, 1)

        x = QCheckBox("Lorem Ipsum")
        x.setEnabled(False)
        x.setCheckState(Qt.PartiallyChecked)
        buttons_layout.addWidget(x, row, 2)

        row += 1
        # QPushButton
        buttons_layout.addWidget(QLabel("QPushButton"), row, 0)

        x = QPushButton("Lorem Ipsum")
        x.setEnabled(True)
        buttons_layout.addWidget(x, row, 1)

        x = QPushButton("Lorem Ipsum")
        x.setEnabled(False)
        buttons_layout.addWidget(x, row, 2)

        row += 1
        # QPushButton (checkable)
        buttons_layout.addWidget(QLabel("QPushButton (checkable)"), row, 0)

        x = QPushButton("Lorem Ipsum")
        x.setEnabled(True)
        x.setCheckable(True)
        x.setChecked(True)
        buttons_layout.addWidget(x, row, 1)

        x = QPushButton("Lorem Ipsum")
        x.setEnabled(False)
        x.setCheckable(True)
        x.setChecked(True)
        buttons_layout.addWidget(x, row, 2)

        #########################
        # Controls (QComboBox, QDial, QSlider, QScrollBar)

        controls_layout = QGridLayout()
        controls_container = QWidget()
        controls_container.setLayout(controls_layout)
        self.tabs.addTab(controls_container, "Controls")
        controls_layout.addWidget(QLabel("Enabled"), 0, 1)
        controls_layout.addWidget(QLabel("Disabled"), 0, 2)
        controls_layout.setRowStretch(999, 1)

        row = 1
        # QComboBox
        controls_layout.addWidget(QLabel("QComboBox"), row, 0)

        x = QComboBox()
        x.setEnabled(True)
        x.addItem("Lorem Ipsum 1")
        x.addItem("Lorem Ipsum 2")
        x.addItem(icon, "Lorem Ipsum 3 (icon)")
        controls_layout.addWidget(x, row, 1)

        x = QComboBox()
        x.setEnabled(False)
        x.addItem("Lorem Ipsum 1")
        x.addItem("Lorem Ipsum 2")
        x.addItem(icon, "Lorem Ipsum 3 (icon)")
        controls_layout.addWidget(x, row, 2)

        row += 1
        # QComboBox (editable)
        controls_layout.addWidget(QLabel("QComboBox (editable)"), row, 0)

        x = QComboBox()
        x.setEnabled(True)
        x.setEditable(True)
        x.addItem("Lorem Ipsum 1")
        x.addItem("Lorem Ipsum 2")
        x.addItem(icon, "Lorem Ipsum 3 (icon)")
        controls_layout.addWidget(x, row, 1)

        x = QComboBox()
        x.setEnabled(False)
        x.setEditable(True)
        x.addItem("Lorem Ipsum 1")
        x.addItem("Lorem Ipsum 2")
        x.addItem(icon, "Lorem Ipsum 3 (icon)")
        controls_layout.addWidget(x, row, 2)

        row += 1
        # QDial
        controls_layout.addWidget(QLabel("QDial"), row, 0)

        x = QDial()
        x.setEnabled(True)
        controls_layout.addWidget(x, row, 1)

        x = QDial()
        x.setEnabled(False)
        controls_layout.addWidget(x, row, 2)

        row += 1
        # QSlider (horizontal)
        controls_layout.addWidget(QLabel("QSlider (horizontal)"), row, 0)

        x = QSlider()
        x.setEnabled(True)
        x.setOrientation(Qt.Horizontal)
        x.setValue(50)
        controls_layout.addWidget(x, row, 1)

        x = QSlider()
        x.setEnabled(False)
        x.setOrientation(Qt.Horizontal)
        x.setValue(50)
        controls_layout.addWidget(x, row, 2)

        row += 1
        # QSlider (vertical)
        controls_layout.addWidget(QLabel("QSlider (vertical)"), row, 0)

        x = QSlider()
        x.setEnabled(True)
        x.setOrientation(Qt.Vertical)
        x.setValue(50)
        controls_layout.addWidget(x, row, 1)

        x = QSlider()
        x.setEnabled(False)
        x.setOrientation(Qt.Vertical)
        x.setValue(50)
        controls_layout.addWidget(x, row, 2)

        row += 1
        # QScrollBar (horizontal)
        controls_layout.addWidget(QLabel("QScrollBar (horizontal)"), row, 0)

        x = QScrollBar()
        x.setEnabled(True)
        x.setOrientation(Qt.Horizontal)
        x.setValue(50)
        controls_layout.addWidget(x, row, 1)

        x = QScrollBar()
        x.setEnabled(False)
        x.setOrientation(Qt.Horizontal)
        x.setValue(50)
        controls_layout.addWidget(x, row, 2)

        row += 1
        # QScrollBar (vertical)
        controls_layout.addWidget(QLabel("QScrollBar (vertical)"), row, 0)

        x = QScrollBar()
        x.setEnabled(True)
        x.setOrientation(Qt.Vertical)
        x.setValue(50)
        controls_layout.addWidget(x, row, 1)

        x = QScrollBar()
        x.setEnabled(False)
        x.setOrientation(Qt.Vertical)
        x.setValue(50)
        controls_layout.addWidget(x, row, 2)

        #########################
        # Inputs (QLineEdit, QTextEdit, QPlainTextEdit, QSpinBox, QDoubleSpinBox, TimeEdit, DateEdit, TimeDateEdit)

        inputs_layout = QGridLayout()
        inputs_container = QWidget()
        inputs_container.setLayout(inputs_layout)
        self.tabs.addTab(inputs_container, "Inputs")
        inputs_layout.addWidget(QLabel("Enabled"), 0, 1)
        inputs_layout.addWidget(QLabel("Disabled"), 0, 2)
        inputs_layout.setRowStretch(999, 1)

        row = 1
        # QLineEdit
        inputs_layout.addWidget(QLabel("QLineEdit"), row, 0)

        x = QLineEdit("Lorem Ipsum")
        x.setEnabled(True)
        inputs_layout.addWidget(x, row, 1)

        x = QLineEdit("Lorem Ipsum")
        x.setEnabled(False)
        inputs_layout.addWidget(x, row, 2)

        row += 1
        # QTextEdit
        inputs_layout.addWidget(QLabel("QTextEdit"), row, 0)

        x = QTextEdit("<h3>Lorem Ipsum</h3>")
        x.setEnabled(True)
        inputs_layout.addWidget(x, row, 1)

        x = QTextEdit("<h3>Lorem Ipsum<h3>")
        x.setEnabled(False)
        inputs_layout.addWidget(x, row, 2)

        row += 1
        # QPlainTextEdit
        inputs_layout.addWidget(QLabel("QPlainTextEdit"), row, 0)

        x = QPlainTextEdit("Lorem Ipsum")
        x.setEnabled(True)
        inputs_layout.addWidget(x, row, 1)

        x = QPlainTextEdit("Lorem Ipsum")
        x.setEnabled(False)
        inputs_layout.addWidget(x, row, 2)

        row += 1
        # QSpinBox
        inputs_layout.addWidget(QLabel("QSpinBox"), row, 0)

        x = QSpinBox()
        x.setEnabled(True)
        inputs_layout.addWidget(x, row, 1)

        x = QSpinBox()
        x.setEnabled(False)
        inputs_layout.addWidget(x, row, 2)

        row += 1
        # QDoubleSpinBox
        inputs_layout.addWidget(QLabel("QDoubleSpinBox"), row, 0)

        x = QDoubleSpinBox()
        x.setEnabled(True)
        inputs_layout.addWidget(x, row, 1)

        x = QDoubleSpinBox()
        x.setEnabled(False)
        inputs_layout.addWidget(x, row, 2)

        row += 1
        # QTimeEdit
        inputs_layout.addWidget(QLabel("QTimeEdit"), row, 0)

        x = QTimeEdit()
        x.setEnabled(True)
        inputs_layout.addWidget(x, row, 1)

        x = QTimeEdit()
        x.setEnabled(False)
        inputs_layout.addWidget(x, row, 2)

        row += 1
        # QDateEdit
        inputs_layout.addWidget(QLabel("QDateEdit"), row, 0)

        x = QDateEdit()
        x.setEnabled(True)
        inputs_layout.addWidget(x, row, 1)

        x = QDateEdit()
        x.setEnabled(False)
        inputs_layout.addWidget(x, row, 2)

        row += 1
        # QDateTimeEdit
        inputs_layout.addWidget(QLabel("QDateTimeEdit"), row, 0)

        x = QDateTimeEdit()
        x.setEnabled(True)
        inputs_layout.addWidget(x, row, 1)

        x = QDateTimeEdit()
        x.setEnabled(False)
        inputs_layout.addWidget(x, row, 2)

        #########################
        # Displays (QLabel, QTextBrowser, QGraphicsView, QLCDNumber, QProgressBar, QLine)

        displays_layout = QGridLayout()
        displays_container = QWidget()
        displays_container.setLayout(displays_layout)
        self.tabs.addTab(displays_container, "Displays")
        displays_layout.addWidget(QLabel("Enabled"), 0, 1)
        displays_layout.addWidget(QLabel("Disabled"), 0, 2)
        displays_layout.setRowStretch(999, 1)

        row = 1
        # QLabel
        displays_layout.addWidget(QLabel("QLabel"), row, 0)

        x = QLabel("Lorem Ipsum")
        x.setEnabled(True)
        displays_layout.addWidget(x, row, 1)

        x = QLabel("Lorem Ipsum")
        x.setEnabled(False)
        displays_layout.addWidget(x, row, 2)

        row += 1
        # QTextBrowser
        displays_layout.addWidget(QLabel("QTextBrowser"), row, 0)

        x = QTextBrowser()
        x.setEnabled(True)
        x.setFixedHeight(100)
        x.setHtml("<h3>Lorem Ipsum<h3>")
        displays_layout.addWidget(x, row, 1)

        x = QTextBrowser()
        x.setEnabled(False)
        x.setFixedHeight(100)
        x.setHtml("<h3>Lorem Ipsum<h3>")
        displays_layout.addWidget(x, row, 2)

        row += 1
        # QGraphicsView
        displays_layout.addWidget(QLabel("QGraphicsView"), row, 0)

        x = QGraphicsView()
        x.setEnabled(True)
        x.setFixedHeight(100)
        x.setScene(scene)
        displays_layout.addWidget(x, row, 1)

        x = QGraphicsView()
        x.setEnabled(False)
        x.setFixedHeight(100)
        x.setScene(scene)
        displays_layout.addWidget(x, row, 2)

        row += 1
        # QLCDNumber
        displays_layout.addWidget(QLabel("QLCDNumber"), row, 0)

        x = QLCDNumber()
        x.setEnabled(True)
        x.display(12345.6789)
        displays_layout.addWidget(x, row, 1)

        x = QLCDNumber()
        x.setEnabled(False)
        x.display(12345.6789)
        displays_layout.addWidget(x, row, 2)

        row += 1
        # QProgressBar
        displays_layout.addWidget(QLabel("QProgressBar"), row, 0)

        x = QProgressBar()
        x.setEnabled(True)
        x.setValue(50)
        displays_layout.addWidget(x, row, 1)

        x = QProgressBar()
        x.setEnabled(False)
        x.setValue(50)
        displays_layout.addWidget(x, row, 2)

        row += 1
        # QCalendarWidget
        displays_layout.addWidget(QLabel("QCalendarWidget"), row, 0)

        x = QCalendarWidget()
        x.setEnabled(True)
        displays_layout.addWidget(x, row, 1)

        x = QCalendarWidget()
        x.setEnabled(False)
        displays_layout.addWidget(x, row, 2)

        #########################
        # Containers

        containers_layout = QGridLayout()
        containers_container = QWidget()
        containers_container.setLayout(containers_layout)
        self.tabs.addTab(containers_container, "Containers")
        containers_layout.addWidget(QLabel("Enabled"), 0, 1)
        containers_layout.addWidget(QLabel("Disabled"), 0, 2)
        containers_layout.setRowStretch(999, 1)

        row = 1
        # QScrollArea
        containers_layout.addWidget(QLabel("QScrollArea"), row, 0)

        x = QScrollArea()
        x.setEnabled(True)
        x.setFixedSize(250, 150)
        x.setWidget(QLabel(("Lorem Ipsum " * 5 + "\n") * 20))
        containers_layout.addWidget(x, row, 1)

        x = QScrollArea()
        x.setEnabled(False)
        x.setFixedSize(250, 150)
        x.setWidget(QLabel(("Lorem Ipsum " * 5 + "\n") * 20))
        containers_layout.addWidget(x, row, 2)

        row += 1
        # QFrame
        containers_layout.addWidget(QLabel("QFrame"), row, 0)

        x = QLabel("Lorem Ipsum")
        x.setEnabled(True)
        x.setGeometry(QtCore.QRect(89, 403, 194, 40))
        x.setFrameShape(QtWidgets.QFrame.StyledPanel)
        x.setFrameShadow(QtWidgets.QFrame.Raised)
        containers_layout.addWidget(x, row, 1)

        x = QLabel("Lorem Ipsum")
        x.setEnabled(False)
        x.setFrameShape(QtWidgets.QFrame.StyledPanel)
        x.setFrameShadow(QtWidgets.QFrame.Raised)
        containers_layout.addWidget(x, row, 2)

        row += 1
        # QGroupBox
        containers_layout.addWidget(QLabel("QGroupBox"), row, 0)

        x = QGroupBox()
        x.setEnabled(True)
        l = QVBoxLayout()
        l.addWidget(QLabel("Lorem Ipsum"))
        x.setLayout(l)
        x.setTitle("Lorem Ipsum")
        containers_layout.addWidget(x, row, 1)

        x = QGroupBox()
        x.setEnabled(False)
        l = QVBoxLayout()
        l.addWidget(QLabel("Lorem Ipsum"))
        x.setLayout(l)
        x.setTitle("Lorem Ipsum")
        containers_layout.addWidget(x, row, 2)

        row += 1
        # QToolBox
        containers_layout.addWidget(QLabel("QToolBox"), row, 0)

        x = QToolBox()
        x.setEnabled(True)
        x.addItem(QLabel("Lorem Ipsum 1"), "Lorem Ipsum 1")
        x.addItem(QLabel("Lorem Ipsum 2"), "Lorem Ipsum 2")
        x.addItem(QLabel("Lorem Ipsum 3 (icon)"), icon, "Lorem Ipsum 3")
        containers_layout.addWidget(x, row, 1)

        x = QToolBox()
        x.setEnabled(False)
        x.addItem(QLabel("Lorem Ipsum 1"), "Lorem Ipsum 1")
        x.addItem(QLabel("Lorem Ipsum 2"), "Lorem Ipsum 2")
        x.addItem(QLabel("Lorem Ipsum 3"), icon, "Lorem Ipsum 3 (icon)")
        containers_layout.addWidget(x, row, 2)

        row += 1
        # QSplitter
        containers_layout.addWidget(QLabel("QSplitter"), row, 0)

        x = QSplitter()
        x.setEnabled(True)
        x.addWidget(QLabel("Lorem Ipsum 1"))
        x.addWidget(QLabel("Lorem Ipsum 2"))
        x.setFixedHeight(50)
        containers_layout.addWidget(x, row, 1)

        x = QSplitter()
        x.setEnabled(False)
        x.addWidget(QLabel("Lorem Ipsum 1"))
        x.addWidget(QLabel("Lorem Ipsum 2"))
        x.setFixedHeight(50)
        containers_layout.addWidget(x, row, 2)

        row += 1
        # QStackedWidget
        containers_layout.addWidget(QLabel("QStackedWidget"), row, 0)

        x = QStackedWidget()
        x.setEnabled(True)
        x.addWidget(QLabel("Lorem Ipsum 1"))
        x.addWidget(QLabel("Lorem Ipsum 2"))
        containers_layout.addWidget(x, row, 1)

        x = QStackedWidget()
        x.setEnabled(False)
        x.addWidget(QLabel("Lorem Ipsum 1"))
        x.addWidget(QLabel("Lorem Ipsum 2"))
        containers_layout.addWidget(x, row, 2)

        row += 1
        # QWidget
        containers_layout.addWidget(QLabel("QWidget"), row, 0)

        x = QWidget()
        x.setEnabled(True)
        QLabel("Lorem Ipsum", x)
        containers_layout.addWidget(x, row, 1)

        x = QWidget()
        x.setEnabled(False)
        QLabel("Lorem Ipsum", x)
        containers_layout.addWidget(x, row, 2)

        #########################
        # Tabs (QTabWidget)

        tabs_layout = QGridLayout()
        tabs_container = QWidget()
        tabs_container.setLayout(tabs_layout)
        self.tabs.addTab(tabs_container, "Tabs")
        tabs_layout.addWidget(QLabel("Enabled"), 0, 1)
        tabs_layout.addWidget(QLabel("Disabled"), 0, 2)
        tabs_layout.setRowStretch(999, 1)

        row = 1
        # QTabWidget (North)
        tabs_layout.addWidget(QLabel("QTabWidget (North)"), row, 0)

        x = QTabWidget()
        x.setEnabled(True)
        x.setTabsClosable(True)
        x.setTabPosition(QTabWidget.TabPosition.North)
        x.addTab(QLabel(("Lorem Ipsum " * 2 + "\n") * 4), "Tab 1")
        x.addTab(QLabel(("Lorem Ipsum " * 2 + "\n") * 4), "Tab 2")
        tabs_layout.addWidget(x, row, 1)

        x = QTabWidget()
        x.setEnabled(False)
        x.setTabsClosable(True)
        x.setTabPosition(QTabWidget.TabPosition.North)
        x.addTab(QLabel(("Lorem Ipsum " * 2 + "\n") * 4), "Tab 1")
        x.addTab(QLabel(("Lorem Ipsum " * 2 + "\n") * 4), "Tab 2")
        tabs_layout.addWidget(x, row, 2)

        row += 1
        # QTabWidget (West)
        tabs_layout.addWidget(QLabel("QTabWidget (West)"), row, 0)

        x = QTabWidget()
        x.setEnabled(True)
        x.setTabsClosable(True)
        x.setTabPosition(QTabWidget.TabPosition.West)
        x.addTab(QLabel(("Lorem Ipsum " * 2 + "\n") * 4), "Tab 1")
        x.addTab(QLabel(("Lorem Ipsum " * 2 + "\n") * 4), "Tab 2")
        tabs_layout.addWidget(x, row, 1)

        x = QTabWidget()
        x.setEnabled(False)
        x.setTabsClosable(True)
        x.setTabPosition(QTabWidget.TabPosition.West)
        x.addTab(QLabel(("Lorem Ipsum " * 2 + "\n") * 4), "Tab 1")
        x.addTab(QLabel(("Lorem Ipsum " * 2 + "\n") * 4), "Tab 2")
        tabs_layout.addWidget(x, row, 2)

        row += 1
        # QTabWidget (South)
        tabs_layout.addWidget(QLabel("QTabWidget (South)"), row, 0)

        x = QTabWidget()
        x.setEnabled(True)
        x.setTabsClosable(True)
        x.setTabPosition(QTabWidget.TabPosition.South)
        x.addTab(QLabel(("Lorem Ipsum " * 2 + "\n") * 4), "Tab 1")
        x.addTab(QLabel(("Lorem Ipsum " * 2 + "\n") * 4), "Tab 2")
        tabs_layout.addWidget(x, row, 1)

        x = QTabWidget()
        x.setEnabled(False)
        x.setTabsClosable(True)
        x.setTabPosition(QTabWidget.TabPosition.South)
        x.addTab(QLabel(("Lorem Ipsum " * 2 + "\n") * 4), "Tab 1")
        x.addTab(QLabel(("Lorem Ipsum " * 2 + "\n") * 4), "Tab 2")
        tabs_layout.addWidget(x, row, 2)

        row += 1
        # QTabWidget (East)
        tabs_layout.addWidget(QLabel("QTabWidget (East)"), row, 0)

        x = QTabWidget()
        x.setEnabled(True)
        x.setTabsClosable(True)
        x.setTabPosition(QTabWidget.TabPosition.East)
        x.addTab(QLabel(("Lorem Ipsum " * 2 + "\n") * 4), "Tab 1")
        x.addTab(QLabel(("Lorem Ipsum " * 2 + "\n") * 4), "Tab 2")
        tabs_layout.addWidget(x, row, 1)

        x = QTabWidget()
        x.setEnabled(False)
        x.setTabsClosable(True)
        x.setTabPosition(QTabWidget.TabPosition.East)
        x.addTab(QLabel(("Lorem Ipsum " * 2 + "\n") * 4), "Tab 1")
        x.addTab(QLabel(("Lorem Ipsum " * 2 + "\n") * 4), "Tab 2")
        tabs_layout.addWidget(x, row, 2)

        #########################
        # Widgets (QTreeWidget, QListWidget, QTableWidget)

        widgets_layout = QGridLayout()
        widgets_container = QWidget()
        widgets_container.setLayout(widgets_layout)
        self.tabs.addTab(widgets_container, "Widgets")
        widgets_layout.addWidget(QLabel("Enabled"), 0, 1)
        widgets_layout.addWidget(QLabel("Disabled"), 0, 2)
        widgets_layout.setRowStretch(999, 1)

        row = 1
        # QTableWidget
        widgets_layout.addWidget(QLabel("QTableWidget"), row, 0)

        x = QTableWidget()
        x.setAlternatingRowColors(True)
        x.setEnabled(True)
        x.setSortingEnabled(True)
        x.setRowCount(20)
        x.setColumnCount(20)
        for tr in range(20):
            for tc in range(20):
                x.setItem(tr, tc, QTableWidgetItem(f"Item-{tr}-{tc}"))
        item = QTableWidgetItem("Checkable")
        item.setCheckState(Qt.Checked)
        x.setItem(0, 0, item)
        widgets_layout.addWidget(x, row, 1)

        x = QTableWidget()
        x.setAlternatingRowColors(True)
        x.setEnabled(False)
        x.setSortingEnabled(True)
        x.setRowCount(20)
        x.setColumnCount(20)
        for tr in range(20):
            for tc in range(20):
                x.setItem(tr, tc, QTableWidgetItem(f"Item-{tr}-{tc}"))
        item = QTableWidgetItem("Checkable")
        item.setCheckState(Qt.Checked)
        x.setItem(0, 0, item)
        widgets_layout.addWidget(x, row, 2)

        row += 1
        # QTreeWidget
        widgets_layout.addWidget(QLabel("QTreeWidget"), row, 0)

        x = QTreeWidget()
        x.setEnabled(True)
        x.setHeaderLabels(['1', '2'])
        for a in range(10):
            item = QTreeWidgetItem(x, [f"Col1 Item-{a}", f"Col2 Item-{a}"])
            for b in range(5):
                QTreeWidgetItem(
                    item, [f"Col1 Item-{a}-{b}", f"Col2 Item-{a}-{b}"])
        x.itemAt(0, 0).setCheckState(0, Qt.Checked)
        widgets_layout.addWidget(x, row, 1)

        x = QTreeWidget()
        x.setEnabled(False)
        x.setHeaderLabels(['1', '2'])
        for a in range(10):
            item = QTreeWidgetItem(x, [f"Col1 Item-{a}", f"Col2 Item-{a}"])
            for b in range(5):
                QTreeWidgetItem(
                    item, [f"Col1 Item-{a}-{b}", f"Col2 Item-{a}-{b}"])
        x.itemAt(0, 0).setCheckState(0, Qt.Checked)
        widgets_layout.addWidget(x, row, 2)

        row += 1
        # QListWidget
        widgets_layout.addWidget(QLabel("QTreeWidget"), row, 0)

        x = QListWidget()
        x.setEnabled(True)
        for a in range(10):
            x.addItem(f"Item-{a}")
        x.itemAt(0, 0).setCheckState(Qt.Checked)
        for index in range(x.count()):
            item = x.item(index)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
        widgets_layout.addWidget(x, row, 1)

        x = QListWidget()
        x.setEnabled(False)
        for a in range(10):
            x.addItem(f"Item-{a}")
        x.itemAt(0, 0).setCheckState(Qt.Checked)
        widgets_layout.addWidget(x, row, 2)

        #########################
        # Main Window

        container = QWidget()
        layout = QVBoxLayout()
        container.setLayout(layout)
        main_window = QMainWindow()
        main_window.setCentralWidget(container)
        self.tabs.addTab(main_window, "Main Window")

        # QStatusBar
        status_bar = QStatusBar()
        status_bar.setEnabled(True)
        status_bar.setToolTip("Status bar tooltip")
        main_window.setStatusBar(status_bar)

        # QToolTip
        x = QPushButton("Hover Me")
        x.setEnabled(True)
        x.setStatusTip("This is text set by .setStatusTip")
        x.setToolTip("This is text set by .setToolTip")
        layout.addWidget(x)

        # QMenu / QMenuBar
        menu: QMenuBar = main_window.menuBar().addMenu('&Menu')

        disabled_menu: QMenuBar = main_window.menuBar().addMenu('&Disabled Menu')
        disabled_menu.setEnabled(False)

        action1 = menu.addAction("Action1")
        action2 = menu.addAction("Action2")
        action3 = menu.addAction(icon, "Action3 (icon)")
        menu.addSeparator()
        submenu = menu.addMenu("Submenu")
        subaction4 = submenu.addAction("Submenu Action 1")
        subaction5 = submenu.addAction("Submenu Action 2")
        subaction6 = submenu.addAction("Submenu Action 3")
        menu.addSection("Advanced")
        action4 = QAction("Action4 (checkable)", menu, checkable=True)
        menu.addAction(action4)
        action5 = QAction("Action5 (checkable)", menu, checkable=True)
        menu.addAction(action5)
        action5.setChecked(True)

        # QToolBar
        toolbar = QToolBar()
        toolbar.addAction(action1)
        toolbar.addAction(action2)
        toolbar.addAction(action3)
        toolbar.addAction(action4)
        toolbar.addAction(action5)
        main_window.addToolBar(toolbar)

        # QToolButton
        # QSizeGrip

        # QDockWidget (North tabs)
        main_window.dock1 = QtWidgets.QDockWidget("One")
        main_window.dock2 = QtWidgets.QDockWidget("Two")
        main_window.dock3 = QtWidgets.QDockWidget("Three")
        main_window.content1 = QtWidgets.QWidget()
        main_window.content1.setStyleSheet("background-color:#330000;")
        main_window.content1.setMinimumSize(QtCore.QSize(50, 50))
        main_window.content2 = QtWidgets.QWidget()
        main_window.content2.setStyleSheet("background-color:#770000;")
        main_window.content2.setMinimumSize(QtCore.QSize(50, 50))
        main_window.content3 = QtWidgets.QWidget()
        main_window.content3.setStyleSheet("background-color:#AA0000;")
        main_window.content3.setMinimumSize(QtCore.QSize(50, 50))
        main_window.dock1.setWidget(main_window.content1)
        main_window.dock2.setWidget(main_window.content2)
        main_window.dock3.setWidget(main_window.content3)
        main_window.addDockWidget(Qt.RightDockWidgetArea, main_window.dock1)
        main_window.tabifyDockWidget(main_window.dock1, main_window.dock2)
        main_window.addDockWidget(Qt.RightDockWidgetArea, main_window.dock3)
        main_window.setDockOptions(
            main_window.GroupedDragging | main_window.AllowTabbedDocks | main_window.AllowNestedDocks)
        main_window.setTabPosition(
            Qt.AllDockWidgetAreas, QtWidgets.QTabWidget.North)

        # QDockWidget (South tabs)
        main_window.south_dock1 = QtWidgets.QDockWidget("One")
        main_window.south_dock2 = QtWidgets.QDockWidget("Two")
        main_window.south_dock3 = QtWidgets.QDockWidget("Three")
        main_window.south_content1 = QtWidgets.QWidget()
        main_window.south_content1.setStyleSheet("background-color:#003300;")
        main_window.south_content1.setMinimumSize(QtCore.QSize(50, 50))
        main_window.south_content2 = QtWidgets.QWidget()
        main_window.south_content2.setStyleSheet("background-color:#007700;")
        main_window.south_content2.setMinimumSize(QtCore.QSize(50, 50))
        main_window.south_content3 = QtWidgets.QWidget()
        main_window.south_content3.setStyleSheet("background-color:#00AA00;")
        main_window.south_content3.setMinimumSize(QtCore.QSize(50, 50))
        main_window.south_dock1.setWidget(main_window.south_content1)
        main_window.south_dock2.setWidget(main_window.south_content2)
        main_window.south_dock3.setWidget(main_window.south_content3)
        main_window.addDockWidget(
            Qt.BottomDockWidgetArea, main_window.south_dock1)
        main_window.tabifyDockWidget(
            main_window.south_dock1, main_window.south_dock2)
        main_window.addDockWidget(
            Qt.BottomDockWidgetArea, main_window.south_dock3)
        main_window.setDockOptions(
            main_window.GroupedDragging | main_window.AllowTabbedDocks | main_window.AllowNestedDocks)
        main_window.setTabPosition(
            Qt.BottomDockWidgetArea, QtWidgets.QTabWidget.South)

        #########################
        # Modals

        # QMessageBox
        # QDialog
        # QDialogButtonBox

        #########################
        # Temp

        try:
            self.gui = show(pokemon, mi_manufacturing, settings={
                            'block': False, 'theme': 'classic'})
            self.tabs.addTab(self.gui, "PandasGUI")
        except:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    example = DemoWidget()
    example.show()
    app.exec_()
