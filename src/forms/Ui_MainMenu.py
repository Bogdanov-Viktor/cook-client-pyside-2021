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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        if not MainMenu.objectName():
            MainMenu.setObjectName(u"MainMenu")
        MainMenu.resize(800, 600)
        self.verticalLayout_2 = QVBoxLayout(MainMenu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.centralwidget = QWidget(MainMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(30)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(255)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.widget_2.setMaximumSize(QSize(700, 600))
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.menuPlansButton = QPushButton(self.widget_2)
        self.menuPlansButton.setObjectName(u"menuPlansButton")
        self.menuPlansButton.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.menuPlansButton.sizePolicy().hasHeightForWidth())
        self.menuPlansButton.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setPointSize(24)
        self.menuPlansButton.setFont(font)

        self.verticalLayout.addWidget(self.menuPlansButton)

        self.warehouseButton = QPushButton(self.widget_2)
        self.warehouseButton.setObjectName(u"warehouseButton")
        sizePolicy3.setHeightForWidth(self.warehouseButton.sizePolicy().hasHeightForWidth())
        self.warehouseButton.setSizePolicy(sizePolicy3)
        self.warehouseButton.setFont(font)

        self.verticalLayout.addWidget(self.warehouseButton)

        self.nomenclaturesButton = QPushButton(self.widget_2)
        self.nomenclaturesButton.setObjectName(u"nomenclaturesButton")
        sizePolicy3.setHeightForWidth(self.nomenclaturesButton.sizePolicy().hasHeightForWidth())
        self.nomenclaturesButton.setSizePolicy(sizePolicy3)
        self.nomenclaturesButton.setFont(font)

        self.verticalLayout.addWidget(self.nomenclaturesButton)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout_2.addWidget(self.centralwidget)


        self.retranslateUi(MainMenu)

        QMetaObject.connectSlotsByName(MainMenu)
    # setupUi

    def retranslateUi(self, MainMenu):
        MainMenu.setWindowTitle(QCoreApplication.translate("MainMenu", u"MainWindow", None))
        self.menuPlansButton.setText(QCoreApplication.translate("MainMenu", u"\u041f\u043b\u0430\u043d\u044b \u043c\u0435\u043d\u044e", None))
        self.warehouseButton.setText(QCoreApplication.translate("MainMenu", u"\u0421\u043a\u043b\u0430\u0434", None))
        self.nomenclaturesButton.setText(QCoreApplication.translate("MainMenu", u"\u041d\u043e\u043c\u0435\u043d\u043a\u043b\u0430\u0442\u0443\u0440\u044b", None))
    # retranslateUi

