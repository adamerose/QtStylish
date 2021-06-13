import os
import sys
from PyQt5 import QtWidgets
import qtstylish

sys.path.append(os.path.dirname(__file__))
dirname = os.path.dirname(__file__)

DARK = None
LIGHT = None
with open(os.path.join(dirname, "compiled/dark.qss")) as f:
    DARK = f.read()
with open(os.path.join(dirname, "compiled/light.qss")) as f:
    LIGHT = f.read()


# Return QSS stylesheet for dark theme
def dark(hot_reload=False):
    from compiled import qtstylish_rc
    if hot_reload:
        compile()
    return DARK


# Return QSS stylesheet for light theme
def light(hot_reload=False):
    from compiled import qtstylish_rc
    if hot_reload:
        compile()
    return LIGHT


def compile():
    import qtsass
    # Compile SCSS into QSS
    qtsass.compile_filename(os.path.join(dirname, "stylesheets/dark.scss"),
                            os.path.join(dirname, "compiled/dark.qss"))
    qtsass.compile_filename(os.path.join(dirname, "stylesheets/light.scss"),
                            os.path.join(dirname, "compiled/light.qss"))
    # Compile resources defined by style.qrc into a python module
    os.system(f"pyrcc5 {dirname}/stylesheets/main.qrc -o {dirname}/compiled/qtstylish_rc.py")
    # This part is for hot reload
    with open(os.path.join(dirname, "compiled/dark.qss")) as f:
        global DARK
        DARK = f.read()
    with open(os.path.join(dirname, "compiled/light.qss")) as f:
        global LIGHT
        LIGHT = f.read()


class ThemeSwitcher(QtWidgets.QWidget):
    def __init__(self, contents, widget_to_style=None, hot_reload=False):
        super().__init__()

        if widget_to_style is None:
            self.widget_to_style = self
        else:
            self.widget_to_style = widget_to_style

        layout = QtWidgets.QVBoxLayout()
        btn_layout = QtWidgets.QHBoxLayout()

        btn = QtWidgets.QPushButton("Unstyled")
        btn.clicked.connect(lambda: self.widget_to_style.setStyleSheet(""))
        btn_layout.addWidget(btn)

        btn = QtWidgets.QPushButton("Light")
        btn.clicked.connect(lambda: self.widget_to_style.setStyleSheet(qtstylish.light(hot_reload=hot_reload)))
        btn_layout.addWidget(btn)

        btn = QtWidgets.QPushButton("Dark")
        btn.clicked.connect(lambda: self.widget_to_style.setStyleSheet(qtstylish.dark(hot_reload=hot_reload)))
        btn_layout.addWidget(btn)

        ##################

        theme_btn_layout = QtWidgets.QHBoxLayout()
        for style in QtWidgets.QStyleFactory().keys():
            btn = QtWidgets.QPushButton(style)
            btn.clicked.connect(lambda _, s=style: [QtWidgets.QApplication.instance().setStyle(QtWidgets.QStyleFactory.create(s)),
                                                    print(f"Setting style to {s}")])
            theme_btn_layout.addWidget(btn)
        layout.addLayout(theme_btn_layout)

        layout.addLayout(btn_layout)
        layout.addWidget(contents)
        self.setLayout(layout)


if __name__ == "__main__":
    compile()
