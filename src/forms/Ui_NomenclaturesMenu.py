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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLayout,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_NomenclaturesMenu(object):
    def setupUi(self, NomenclaturesMenu):
        if not NomenclaturesMenu.objectName():
            NomenclaturesMenu.setObjectName(u"NomenclaturesMenu")
        NomenclaturesMenu.resize(800, 601)
        self.verticalLayout_2 = QVBoxLayout(NomenclaturesMenu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.centralwidget = QWidget(NomenclaturesMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(30)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.widget)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMaximumSize(QSize(90, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget_11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.backButton = QPushButton(self.widget_11)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.backButton)


        self.horizontalLayout_2.addWidget(self.widget_11, 0, Qt.AlignTop)

        self.widget_12 = QWidget(self.widget)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.line = QFrame(self.widget_12)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)


        self.horizontalLayout_2.addWidget(self.widget_12)


        self.horizontalLayout.addWidget(self.widget, 0, Qt.AlignLeft)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(255)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMaximumSize(QSize(700, 600))
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.dishesButton = QPushButton(self.widget_2)
        self.dishesButton.setObjectName(u"dishesButton")
        self.dishesButton.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dishesButton.sizePolicy().hasHeightForWidth())
        self.dishesButton.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(24)
        self.dishesButton.setFont(font)

        self.verticalLayout_5.addWidget(self.dishesButton)

        self.productsButton = QPushButton(self.widget_2)
        self.productsButton.setObjectName(u"productsButton")
        sizePolicy2.setHeightForWidth(self.productsButton.sizePolicy().hasHeightForWidth())
        self.productsButton.setSizePolicy(sizePolicy2)
        self.productsButton.setFont(font)

        self.verticalLayout_5.addWidget(self.productsButton)

        self.measuresButton = QPushButton(self.widget_2)
        self.measuresButton.setObjectName(u"measuresButton")
        sizePolicy2.setHeightForWidth(self.measuresButton.sizePolicy().hasHeightForWidth())
        self.measuresButton.setSizePolicy(sizePolicy2)
        self.measuresButton.setFont(font)

        self.verticalLayout_5.addWidget(self.measuresButton)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout_2.addWidget(self.centralwidget)


        self.retranslateUi(NomenclaturesMenu)

        QMetaObject.connectSlotsByName(NomenclaturesMenu)
    # setupUi

    def retranslateUi(self, NomenclaturesMenu):
        NomenclaturesMenu.setWindowTitle(QCoreApplication.translate("NomenclaturesMenu", u"MainWindow", None))
        self.backButton.setText(QCoreApplication.translate("NomenclaturesMenu", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.dishesButton.setText(QCoreApplication.translate("NomenclaturesMenu", u"\u0411\u043b\u044e\u0434\u0430", None))
        self.productsButton.setText(QCoreApplication.translate("NomenclaturesMenu", u"\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b", None))
        self.measuresButton.setText(QCoreApplication.translate("NomenclaturesMenu", u"\u0415\u0434\u0438\u043d\u0438\u0446\u044b \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
    # retranslateUi

