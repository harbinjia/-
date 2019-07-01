# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_classification(object):
    def setupUi(self, classification):
        classification.setObjectName("classification")
        classification.resize(409, 505)
        self.centralwidget = QtWidgets.QWidget(classification)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 110, 101, 31))
        font = QtGui.QFont()
        font.setFamily("方正楷体_GBK")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(140, 110, 221, 31))
        font = QtGui.QFont()
        font.setFamily("方正楷体_GBK")
        self.text.setFont(font)
        self.text.setObjectName("text")
        self.sub = QtWidgets.QPushButton(self.centralwidget)
        self.sub.setGeometry(QtCore.QRect(130, 180, 80, 26))
        font = QtGui.QFont()
        font.setFamily("方正楷体_GBK")
        font.setPointSize(12)
        self.sub.setFont(font)
        self.sub.setObjectName("sub")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(260, 180, 80, 26))
        font = QtGui.QFont()
        font.setFamily("方正楷体_GBK")
        font.setPointSize(12)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 220, 81, 31))
        font = QtGui.QFont()
        font.setFamily("方正楷体_GBK")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 40, 221, 31))
        font = QtGui.QFont()
        font.setFamily("方正楷体_GBK")
        font.setPointSize(18)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.result = QtWidgets.QTextBrowser(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(100, 251, 261, 171))
        self.result.setObjectName("result")
        classification.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(classification)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 409, 28))
        self.menubar.setObjectName("menubar")
        classification.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(classification)
        self.statusbar.setObjectName("statusbar")
        classification.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(classification)
        self.toolBar.setObjectName("toolBar")
        classification.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.label.setBuddy(self.text)

        self.retranslateUi(classification)
        self.clear.clicked.connect(self.text.clear)
        QtCore.QMetaObject.connectSlotsByName(classification)
        classification.setTabOrder(self.text, self.sub)
        classification.setTabOrder(self.sub, self.clear)

    def retranslateUi(self, classification):
        _translate = QtCore.QCoreApplication.translate
        classification.setWindowTitle(_translate("classification", "MainWindow"))
        self.label.setText(_translate("classification", "输入测试文本:"))
        self.sub.setText(_translate("classification", "查询"))
        self.clear.setText(_translate("classification", "清空"))
        self.label_2.setText(_translate("classification", "结果显示："))
        self.label_3.setText(_translate("classification", "极短文本分析-hoho"))
        self.toolBar.setWindowTitle(_translate("classification", "toolBar"))

if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtGui.MainWindow()
    ui = Ui_classification()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
