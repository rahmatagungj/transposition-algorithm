# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(523, 551)
        MainWindow.setFixedSize(523, 551)
        MainWindow.setStyleSheet("background-color: rgb(0, 85, 127)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, -10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;\n"
"font-weight: 600;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 470, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: transparent;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"    border: 2px solid white;\n"
"    color: rgb(0, 85, 127);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 470, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Nunito")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: transparent;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: white;\n"
"    border: 2px solid white;\n"
"    color: rgb(0, 85, 127);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 70, 461, 321))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("border-radius: 5px;\n"
"background-color: rgba(0, 117, 171,100);\n"
"color: white;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(90, 410, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("color: white;\n"
"border: 2px solid white;\n"
"background-color: transparent;\n"
"border-radius: 5px;\n"
"text-align: center;")
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 410, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;\n"
"font-weight: 600;")
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.plainTextEdit.raise_()
        self.label_2.raise_()
        self.spinBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TRANSPOSITION ALGORITHM"))
        self.label.setText(_translate("MainWindow", "TRANSPOSITION ALGORITHM"))
        self.pushButton.setText(_translate("MainWindow", "NEXT"))
        self.pushButton_2.setText(_translate("MainWindow", "PREVIOUS"))
        self.label_2.setText(_translate("MainWindow", "STEP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
