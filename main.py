# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Slot, Qt, QRect, QMetaObject, QSize, QObject
from PySide6.QtGui import QFont, QTextOption
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QSizePolicy, QLayout, QHBoxLayout, QWidget, \
    QTextEdit, QLineEdit

from Ui_MainMenu import Ui_MainMenu
from Ui_MeasuresPage import Ui_MeasuresPage
from Ui_NomenclaturesMenu import Ui_NomenclaturesMenu

class Ui_MeasuresPage_func(QtWidgets.QWidget, Ui_MeasuresPage):
    @Slot(bool)
    def deleted(self, checked):
        widget = QObject.sender(self).parent()
        index = int(widget.objectName()[widget.objectName().find('_') + 1:])
        print(f"deleted {index}{widget}")
        widget.deleteLater()

    @Slot()
    def edited(self):
        widget = QObject.sender(self).parent()
        index = int(widget.objectName()[widget.objectName().find('_') + 1:])
        print(f"edited {index}{widget}")

    @Slot(bool)
    def addMeasureButtonClicked(self, checked):
        # print("планы меню", checked )

        widget = QWidget(self.scrollAreaWidgetContents)
        widget.setObjectName(u"measure_331")
        widget.setMinimumSize(QSize(420, 60))
        widget.setMaximumSize(QSize(16777215, 60))

        horizontalLayout = QHBoxLayout(widget)
        # horizontalLayout_3.setAlignment(Qt.AlignLeft)
        #horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        textEdit = QLineEdit(widget)
        #textEdit_2000000000.setObjectName(u"textEdit_2000000000")
        textEdit.setMinimumSize(QSize(315, 0))
        textEdit.setMaximumSize(QSize(315, 60))
        textEdit.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        font = QFont()
        font.setPointSize(18)
        #font.setStyleHint(QFont.Monospace)
        textEdit.setFont(font)
        # textEdit.setWordWrapMode(QTextOption.NoWrap)

        horizontalLayout.addWidget(textEdit)

        deleteButton = QPushButton("Удалить", widget)
        # pushButton_2000000000.setObjectName(u"pushButton_2000000000")

        horizontalLayout.addWidget(deleteButton)

        self.verticalLayout.addWidget(widget, 0, Qt.AlignLeft)
        textEdit.editingFinished.connect(self.edited)
        deleteButton.clicked.connect(self.deleted)
        # self.widget_5.setObjectName(u"widget_5")


    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.addMeasureButton.clicked.connect(self.addMeasureButtonClicked)
        self.verticalLayout.setAlignment(Qt.AlignTop)




class Ui_NomenclaturesMenu_func(QtWidgets.QWidget, Ui_NomenclaturesMenu):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        self.measuresButton.clicked.connect(parent.measuresPage.show)
        self.measuresButton.clicked.connect(self.hide)
        parent.measuresPage.backButton.clicked.connect(self.show)
        parent.measuresPage.backButton.clicked.connect(parent.measuresPage.hide)



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
        self.showMaximized()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication([])
    window = AppWindow()
    sys.exit(app.exec())
