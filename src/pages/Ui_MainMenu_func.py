from PySide6 import QtWidgets

from src.forms.Ui_MainMenu import Ui_MainMenu


class Ui_MainMenu_func(QtWidgets.QWidget, Ui_MainMenu):

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        # self.menuPlansButton.clicked.connect(self.nomenMenu.)
        # self.warehouseButton.clicked.connect(self.nomenMenu.ButtonClicked)

        self.nomenclaturesButton.clicked.connect(parent.nomenMenu.show)
        self.nomenclaturesButton.clicked.connect(self.hide)

        parent.nomenMenu.backButton.clicked.connect(self.show)
        parent.nomenMenu.backButton.clicked.connect(parent.nomenMenu.hide)