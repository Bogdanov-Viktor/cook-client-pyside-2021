from PySide6 import QtWidgets

from src.forms.Ui_NomenclaturesMenu import Ui_NomenclaturesMenu

class Ui_NomenclaturesMenu_func(QtWidgets.QWidget, Ui_NomenclaturesMenu):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        self.measuresButton.clicked.connect(parent.measuresPage.show)
        self.measuresButton.clicked.connect(self.hide)
        self.measuresButton.clicked.connect(parent.measuresPage.updateAllMeasure)
        parent.measuresPage.backButton.clicked.connect(self.show)
        parent.measuresPage.backButton.clicked.connect(parent.measuresPage.hide)