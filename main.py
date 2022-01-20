# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication

from Ui_MainMenu import Ui_MainMenu
from Ui_NomenclaturesMenu import Ui_NomenclaturesMenu


class Ui_NomenclaturesMenu_func(QtWidgets.QWidget, Ui_NomenclaturesMenu):

    # @Slot(bool)
    # def menuPlansButtonClicked(self, checked):
    #     print("планы меню", checked )
    #     self.close()
    #
    # @Slot(bool)
    # def warehouseButtonClicked(self, checked):
    #     print("склад", checked)
    #
    # @Slot(bool)
    # def nomenclaturesButtonClicked(self, checked):
    #     print("номенклатуры", checked)

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        # self.menuPlansButton.clicked.connect(self.menuPlansButtonClicked)
        # self.warehouseButton.clicked.connect(self.warehouseButtonClicked)
        # self.nomenclaturesButton.clicked.connect(self.nomenclaturesButtonClicked)


class Ui_MainMenu_func(QtWidgets.QWidget, Ui_MainMenu):

    # @Slot(bool)
    # def menuPlansButtonClicked(self, checked):
    #     print("планы меню", checked )
    #     self.close()
    #
    # @Slot(bool)
    # def warehouseButtonClicked(self, checked):
    #     print("склад", checked)
    #
    # @Slot(bool)
    # def nomenclaturesButtonClicked(self, checked):
    #     print("номенклатуры", checked)

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        self.nomenMenu = Ui_NomenclaturesMenu_func(parent)
        self.nomenMenu.hide()

        # self.menuPlansButton.clicked.connect(self.nomenMenu.)
        # self.warehouseButton.clicked.connect(self.nomenMenu.ButtonClicked)
        self.nomenclaturesButton.clicked.connect(self.nomenMenu.show)
        self.nomenclaturesButton.clicked.connect(self.hide)

        self.nomenMenu.backButton.clicked.connect(self.show)
        self.nomenMenu.backButton.clicked.connect(self.nomenMenu.hide)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication([])
    window = QtWidgets.QMainWindow()
    widget = Ui_MainMenu_func(window)

    desktopGeom = QtWidgets.QApplication.screens()[0].availableGeometry()
    window.setGeometry(
        (desktopGeom.width() - widget.geometry().width()) / 2,
        (desktopGeom.height() - widget.geometry().height()) / 2,
        widget.geometry().width(),
        widget.geometry().height()
    )

    window.show()

    sys.exit(app.exec())
