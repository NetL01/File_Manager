# -*- coding: utf-8 -*-

# MainWindow implementation generated from reading ui file 'lst.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(990, 565)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)

        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(780, 320, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(530, 25, 55, 16))
        self.label.setObjectName("label")
        
        self.tableWidget2 = QtWidgets.QTableWidget(MainWindow)
        self.tableWidget2.setGeometry(QtCore.QRect(700, 360, 256, 192))
        self.tableWidget2.setObjectName("tableWidget2")
        self.tableWidget2.setColumnCount(0)
        self.tableWidget2.setRowCount(0)
        
        self.tableWidget = QtWidgets.QTableWidget(MainWindow)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 601, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.as_hilight = QtWidgets.QPushButton(MainWindow)
        self.as_hilight.setGeometry(QtCore.QRect(490, 40, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.as_hilight.setFont(font)
        self.as_hilight.setObjectName("as_hilight")
        self.Button_create = QtWidgets.QPushButton(MainWindow)
        self.Button_create.setGeometry(QtCore.QRect(360, 40, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Button_create.setFont(font)
        self.Button_create.setObjectName("Button_create")
        self.Button_del = QtWidgets.QPushButton(MainWindow)
        self.Button_del.setGeometry(QtCore.QRect(670, 70, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Button_del.setFont(font)
        self.Button_del.setObjectName("Button_del")
        self.Button_cut = QtWidgets.QPushButton(MainWindow)
        self.Button_cut.setGeometry(QtCore.QRect(830, 70, 121, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Button_cut.setFont(font)
        self.Button_cut.setObjectName("Button_cut")
        self.Button_paste = QtWidgets.QPushButton(MainWindow)
        self.Button_paste.setGeometry(QtCore.QRect(750, 120, 131, 41))
        self.Button_paste.setObjectName("Button_paste")
        self.select_all = QtWidgets.QPushButton(MainWindow)
        self.select_all.setGeometry(QtCore.QRect(670, 170, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_all.setFont(font)
        self.select_all.setObjectName("select_all")
        self.disable_all = QtWidgets.QPushButton(MainWindow)
        self.disable_all.setGeometry(QtCore.QRect(830, 170, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.disable_all.setFont(font)
        self.disable_all.setCheckable(False)
        self.disable_all.setObjectName("disable_all")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.as_hilight.setText(_translate("MainWindow", "Режим выделения"))
        self.Button_create.setText(_translate("MainWindow", "Создать"))
        self.Button_del.setText(_translate("MainWindow", "Удалить"))
        self.Button_cut.setText(_translate("MainWindow", "Вырезать"))
        self.Button_paste.setText(_translate("MainWindow", "Вставить"))
        self.select_all.setText(_translate("MainWindow", "Выбрать всё"))
        self.disable_all.setText(_translate("MainWindow", "Сбросить"))
        self.label_2.setText(_translate("MainWindow", "Выделенное"))
        self.label.setText(_translate("MainWindow", "OFF"))
