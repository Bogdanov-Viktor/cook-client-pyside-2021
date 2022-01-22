from PySide6 import QtWidgets
from PySide6.QtWidgets import QVBoxLayout

from src.pages.Ui_MeasuresPage_func import Ui_MeasuresPage_func
from src.pages.Ui_NomenclaturesMenu_func import Ui_NomenclaturesMenu_func
from src.pages.Ui_MainMenu_func import Ui_MainMenu_func


class AppWindow(QtWidgets.QWidget):
    def addPage(self, page):
        var = page(self)
        var.hide()
        self.verticalLayout.addWidget(var)
        return var

    def __init__(self):
        super().__init__()

        self.verticalLayout = QVBoxLayout(self)

        self.measuresPage = self.addPage(Ui_MeasuresPage_func)
        self.nomenMenu = self.addPage(Ui_NomenclaturesMenu_func)
        self.mainMenu = self.addPage(Ui_MainMenu_func)

        widget = self.mainMenu

        desktopGeom = QtWidgets.QApplication.screens()[0].availableGeometry()
        self.setGeometry(
            (desktopGeom.width() - widget.geometry().width()) / 2,
            (desktopGeom.height() - widget.geometry().height()) / 2,
            widget.geometry().width(),
            widget.geometry().height()
        )

        widget.show()
        #self.showMaximized()
        self.show()

