import json
import configparser
import os

from PySide6 import QtWidgets, QtNetwork
from PySide6.QtCore import Slot, Qt, QSize, QUrl, QByteArray, QSignalMapper
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QPushButton, QHBoxLayout, QWidget, QLineEdit

from src.forms.Ui_MeasuresPage import Ui_MeasuresPage


class Ui_MeasuresPage_func(QtWidgets.QWidget, Ui_MeasuresPage):

    def __init__(self, parent):
        super().__init__(parent)

        self.setupUi(self)
        self.addMeasureButton.clicked.connect(self.addMeasureButtonClicked)
        self.verticalLayout.setAlignment(Qt.AlignTop)

        self.deletedMapper = QSignalMapper(self)
        self.deletedMapper.mappedObject.connect(self.deleted)

        self.editedMapper = QSignalMapper(self)
        self.editedMapper.mappedObject.connect(self.edited)

        self.updateHttp = QtNetwork.QNetworkAccessManager()
        self.updateHttp.finished.connect(self.updateAllMeasureWidgets)

        self.deleteHttp = QtNetwork.QNetworkAccessManager()
        self.deleteHttp.finished.connect(self.updateIfCorrect)

        self.addHttp = QtNetwork.QNetworkAccessManager()
        self.addHttp.finished.connect(self.updateIfCorrect)

        self.editHttp = QtNetwork.QNetworkAccessManager()
        self.editHttp.finished.connect(self.updateIfCorrect)

        path = "settings.ini"
        self.crudConfig(path)

        # config = configparser.ConfigParser()
        # config.read('FILE.INI')
        # print(config['DEFAULT']['path'])  # -> "/path/name/"
        # config['DEFAULT']['path'] = '/var/shared/'  # update
        # config['DEFAULT']['default_message'] = 'Hey! help me!!'  # create
        #
        # with open('FILE.INI', 'w') as configfile:  # save
        #     config.write(configfile)

    # HTTP

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

    @Slot()
    def updateIfCorrect(self, reply):
        er = reply.error()

        if er == QtNetwork.QNetworkReply.NoError:
            responseBody, responseCharset = self.decodeJson(reply)
            if (responseBody["status"]):
                self.updateAllMeasure()

        else:
            print("Error occured: ", er)
            print(reply.errorString())

    #   "delete" request
    @Slot()
    def deleted(self, widget):
        index = int(widget.objectName()[widget.objectName().find('_') + 1:])
        url = f'{self.servAddr}measure.delete?id={index}&access_token={self.access_token}'
        req = QtNetwork.QNetworkRequest(QUrl(url))

        self.deleteHttp.get(req)

        # widget.deleteLater()

        # widget = QObject.sender(self).parent()
        #   QObject.sender в случае с несколькими потоками дает ошибку widget==None, поэтому не подходит

    #   "edit" request
    @Slot()
    def edited(self, textEdit):
        index = int(textEdit.parent().objectName()[textEdit.parent().objectName().find('_') + 1:])
        name = textEdit.text()
        url = f'{self.servAddr}measure.edit?id={index}&set_name={name}&access_token={self.access_token}'
        req = QtNetwork.QNetworkRequest(QUrl(url))

        print("editRequest")

        self.editHttp.get(req)
        # widget = QObject.sender(self).parent()
        # index = int(widget.objectName()[widget.objectName().find('_') + 1:])
        # print(f"edited {index}{widget}")

    #   "getAll" request
    @Slot()
    def updateAllMeasure(self):
        url = f'{self.servAddr}measure.getAll?access_token={self.access_token}'
        req = QtNetwork.QNetworkRequest(QUrl(url))

        self.updateHttp.get(req)

    #   "add" request
    @Slot()
    def addMeasureButtonClicked(self):
        # print("планы меню", checked )
        newMeasureName = ""
        url = f'{self.servAddr}measure.add?set_name={newMeasureName}&access_token={self.access_token}'
        req = QtNetwork.QNetworkRequest(QUrl(url))

        self.addHttp.get(req)

    # Widgets

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

        self.editedMapper.setMapping(textEdit, textEdit)
        textEdit.editingFinished.connect(self.editedMapper.map)

        # self.widget_5.setObjectName(u"widget_5")

    def clearMeasureWidgets(self):
        # self.verticalLayout.count()
        # self.verticalLayout.itemAt(i)
        item = self.verticalLayout.takeAt(0)
        while item is not None:
            # print(item.widget().objectName())
            item.widget().deleteLater()
            item = self.verticalLayout.takeAt(0)

    @Slot()   # "getAll" response
    def updateAllMeasureWidgets(self, reply):

        er = reply.error()

        if er == QtNetwork.QNetworkReply.NoError:
            responseBody, responseCharset = self.decodeJson(reply)
            if(responseBody["status"]):
                self.clearMeasureWidgets()
                for el in responseBody["value"]:
                    self.addMeasureWidget(el["id"], el["name"])

        else:
            print("Error occured: ", er)
            print(reply.errorString())

    # Config

    def createConfigIfNotExists(self, path):
        """
        Create a config file
        """
        if not os.path.exists(path):
            config = configparser.ConfigParser()
        else:
            config = configparser.ConfigParser()
            config.read(path)

        if not config.has_section('Server'):
            config.add_section("Server")
        if not config.has_option("Server", "url"):
            config.set("Server", "url", "http://localhost:8080/")
        if not config.has_option("Server", "access_token"):
            config.set("Server", "access_token", "9h9er798")

        with open(path, "w") as config_file:
            config.write(config_file)

    def crudConfig(self, path):
        """
        Create, read, update, delete config
        """
        self.createConfigIfNotExists(path)

        config = configparser.ConfigParser()
        config.read(path)

        # Читаем некоторые значения из конфиг. файла.
        self.servAddr = config.get("Server", "url")
        self.access_token = config.get("Server", "access_token")

        # try:
        #     conf.add_section("new_section_name")
        # except DuplicateSectionError:
        #     # такая секция уже существует
        #     pass
        # try:
        #     OPTION = config.get('Options', 'myoption')
        # except ConfigParser.NoOptionError:
        #     pass
        # # Меняем значения из конфиг. файла.
        # config.set("Settings", "font_size", "12")
        # # Удаляем значение из конфиг. файла.
        # config.remove_option("Settings", "font_style")
        # # Вносим изменения в конфиг. файл.
        # with open(path, "w") as config_file:
        #     config.write(config_file)
