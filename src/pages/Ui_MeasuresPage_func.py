import json

from PySide6 import QtWidgets, QtNetwork
from PySide6.QtCore import Slot, Qt, QSize, QUrl, QByteArray, QSignalMapper
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QPushButton, QHBoxLayout, QWidget, QLineEdit

from src.forms.Ui_MeasuresPage import Ui_MeasuresPage


class Ui_MeasuresPage_func(QtWidgets.QWidget, Ui_MeasuresPage):
    @Slot()
    def deleted(self, widget):
        widget.deleteLater()
        # widget = QObject.sender(self).parent()
        #   QObject.sender в случае с несколькими потоками дает ошибку widget==None, поэтому не подходит
        # index = int(widget.objectName()[widget.objectName().find('_') + 1:])

    @Slot()
    def edited(self):
        print()
        # widget = QObject.sender(self).parent()
        # index = int(widget.objectName()[widget.objectName().find('_') + 1:])
        # print(f"edited {index}{widget}")

    def addMeasureWidget(self, measureId, measureName):
        widget = QWidget(self.scrollAreaWidgetContents)
        widget.setObjectName(f"measure_{measureId}")
        widget.setMinimumSize(QSize(420, 60))
        widget.setMaximumSize(QSize(16777215, 60))

        horizontalLayout = QHBoxLayout(widget)
        # horizontalLayout_3.setAlignment(Qt.AlignLeft)
        # horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        textEdit = QLineEdit(widget)
        textEdit.setText(measureName)
        # textEdit_2000000000.setObjectName(u"textEdit_2000000000")
        textEdit.setMinimumSize(QSize(315, 0))
        textEdit.setMaximumSize(QSize(315, 60))
        textEdit.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        font = QFont()
        font.setPointSize(18)
        # font.setStyleHint(QFont.Monospace)
        textEdit.setFont(font)
        # textEdit.setWordWrapMode(QTextOption.NoWrap)

        horizontalLayout.addWidget(textEdit)

        deleteButton = QPushButton("Удалить", widget)
        # pushButton_2000000000.setObjectName(u"pushButton_2000000000")

        horizontalLayout.addWidget(deleteButton)

        self.verticalLayout.addWidget(widget, 0, Qt.AlignLeft)


        self.deletedMapper.setMapping(deleteButton, deleteButton.parent())
        deleteButton.clicked.connect(self.deletedMapper.map)

        #deleteButton.clicked.connect()

        textEdit.editingFinished.connect(self.edited)

        # self.widget_5.setObjectName(u"widget_5")

    def decodeJson(self, reply):
        # заголовок с кодировкой
        content_type_header = str(reply.rawHeader(QByteArray('content-type')), 'ASCII')
        start_index = content_type_header.find('charset') + len('charset') + 1
        end_index_pl_1 = len(content_type_header)
        body_charset = content_type_header[start_index:end_index_pl_1]  # срез строки
        print(body_charset)

        # тело HTTP ответа
        decoded_response = json.loads(str(reply.readAll(), body_charset))
        print(str(decoded_response))

        return decoded_response, body_charset

    def clearMeasureWidgets(self):
        # self.verticalLayout.count()
        # self.verticalLayout.itemAt(i)
        item = self.verticalLayout.takeAt(0)
        while item is not None:
            print(item.widget().objectName())
            item.widget().deleteLater()
            item = self.verticalLayout.takeAt(0)

    def updateAllMeasureWidgets(self, reply):

        er = reply.error()

        if er == QtNetwork.QNetworkReply.NoError:
            responseBody, responseCharset = self.decodeJson(reply)
            bytes_string = reply.readAll()
            print(str(bytes_string, 'utf-8'))
            if(responseBody["status"]):
                self.clearMeasureWidgets()
                for el in responseBody["value"]:
                    self.addMeasureWidget(el["id"], el["name"])

            self.addMeasureWidget(33, "")

        else:
            print("Error occured: ", er)
            print(reply.errorString())

    def updateAllMeasure(self):
        url = 'http://localhost:8080/measure.getAll?access_token=9'
        req = QtNetwork.QNetworkRequest(QUrl(url))

        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.finished.connect(self.updateAllMeasureWidgets)
        self.nam.get(req)

    @Slot(bool)
    def addMeasureButtonClicked(self, checked):
        # print("планы меню", checked )
        self.addMeasureWidget(33, "")

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.addMeasureButton.clicked.connect(self.addMeasureButtonClicked)
        self.verticalLayout.setAlignment(Qt.AlignTop)

        self.deletedMapper = QSignalMapper(self)
        self.deletedMapper.mappedObject.connect(self.deleted)
