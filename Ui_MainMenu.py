# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MainMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        if not MainMenu.objectName():
            MainMenu.setObjectName(u"MainMenu")
        MainMenu.resize(800, 600)
        self.centralwidget = QWidget(MainMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setGeometry(QRect(0, 0, 791, 571))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(100, 20, 591, 531))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menuPlansButton = QPushButton(self.verticalLayoutWidget)
        self.menuPlansButton.setObjectName(u"menuPlansButton")
        self.menuPlansButton.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuPlansButton.sizePolicy().hasHeightForWidth())
        self.menuPlansButton.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(24)
        self.menuPlansButton.setFont(font)

        self.verticalLayout.addWidget(self.menuPlansButton)

        self.warehouseButton = QPushButton(self.verticalLayoutWidget)
        self.warehouseButton.setObjectName(u"warehouseButton")
        sizePolicy.setHeightForWidth(self.warehouseButton.sizePolicy().hasHeightForWidth())
        self.warehouseButton.setSizePolicy(sizePolicy)
        self.warehouseButton.setFont(font)

        self.verticalLayout.addWidget(self.warehouseButton)

        self.nomenclaturesButton = QPushButton(self.verticalLayoutWidget)
        self.nomenclaturesButton.setObjectName(u"nomenclaturesButton")
        sizePolicy.setHeightForWidth(self.nomenclaturesButton.sizePolicy().hasHeightForWidth())
        self.nomenclaturesButton.setSizePolicy(sizePolicy)
        self.nomenclaturesButton.setFont(font)

        self.verticalLayout.addWidget(self.nomenclaturesButton)

        self.statusbar = QStatusBar(MainMenu)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setGeometry(QRect(0, 0, 3, 21))

        self.retranslateUi(MainMenu)

        QMetaObject.connectSlotsByName(MainMenu)
    # setupUi

    def retranslateUi(self, MainMenu):
        MainMenu.setWindowTitle(QCoreApplication.translate("MainMenu", u"MainWindow", None))
        self.menuPlansButton.setText(QCoreApplication.translate("MainMenu", u"\u041f\u043b\u0430\u043d\u044b \u043c\u0435\u043d\u044e", None))
        self.warehouseButton.setText(QCoreApplication.translate("MainMenu", u"\u0421\u043a\u043b\u0430\u0434", None))
        self.nomenclaturesButton.setText(QCoreApplication.translate("MainMenu", u"\u041d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u044b", None))
    # retranslateUi

