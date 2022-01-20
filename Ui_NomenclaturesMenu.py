# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_NomenclaturesMenu.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_NomenclaturesMenu(object):
    def setupUi(self, NomenclaturesMenu):
        if not NomenclaturesMenu.objectName():
            NomenclaturesMenu.setObjectName(u"NomenclaturesMenu")
        NomenclaturesMenu.resize(800, 600)
        self.centralwidget = QWidget(NomenclaturesMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setGeometry(QRect(0, 0, 791, 571))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(100, 20, 591, 531))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dishesButton = QPushButton(self.verticalLayoutWidget)
        self.dishesButton.setObjectName(u"dishesButton")
        self.dishesButton.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dishesButton.sizePolicy().hasHeightForWidth())
        self.dishesButton.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(24)
        self.dishesButton.setFont(font)

        self.verticalLayout.addWidget(self.dishesButton)

        self.productsButton = QPushButton(self.verticalLayoutWidget)
        self.productsButton.setObjectName(u"productsButton")
        sizePolicy.setHeightForWidth(self.productsButton.sizePolicy().hasHeightForWidth())
        self.productsButton.setSizePolicy(sizePolicy)
        self.productsButton.setFont(font)

        self.verticalLayout.addWidget(self.productsButton)

        self.measuresButton = QPushButton(self.verticalLayoutWidget)
        self.measuresButton.setObjectName(u"measuresButton")
        sizePolicy.setHeightForWidth(self.measuresButton.sizePolicy().hasHeightForWidth())
        self.measuresButton.setSizePolicy(sizePolicy)
        self.measuresButton.setFont(font)

        self.verticalLayout.addWidget(self.measuresButton)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(10, 10, 75, 31))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(80, 10, 20, 321))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.statusbar = QStatusBar(NomenclaturesMenu)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setGeometry(QRect(0, 0, 3, 21))

        self.retranslateUi(NomenclaturesMenu)

        QMetaObject.connectSlotsByName(NomenclaturesMenu)
    # setupUi

    def retranslateUi(self, NomenclaturesMenu):
        NomenclaturesMenu.setWindowTitle(QCoreApplication.translate("NomenclaturesMenu", u"MainWindow", None))
        self.dishesButton.setText(QCoreApplication.translate("NomenclaturesMenu", u"\u0411\u043b\u044e\u0434\u0430", None))
        self.productsButton.setText(QCoreApplication.translate("NomenclaturesMenu", u"\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b", None))
        self.measuresButton.setText(QCoreApplication.translate("NomenclaturesMenu", u"\u0415\u0434\u0438\u043d\u0438\u0446\u044b \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.backButton.setText(QCoreApplication.translate("NomenclaturesMenu", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

