# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hw2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from sklearn.datasets import fetch_lfw_people
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(50, 30, 200, 250))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.classification = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.classification.setContentsMargins(0, 0, 0, 0)
        self.classification.setObjectName("PCA")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox.setObjectName("groupBox")
        self.model = QtWidgets.QPushButton(self.groupBox)
        self.model.setGeometry(QtCore.QRect(10, 30, 185, 23))
        self.model.setObjectName("model")
        self.tensor = QtWidgets.QPushButton(self.groupBox)
        self.tensor.setGeometry(QtCore.QRect(10, 70, 185, 23))
        self.tensor.setObjectName("tensor")
        self.test = QtWidgets.QPushButton(self.groupBox)
        self.test.setGeometry(QtCore.QRect(10, 110, 185, 23))
        self.test.setObjectName("test")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 150, 185, 23))
        self.lineEdit_2.setObjectName("lineEdit")
        self.erasing = QtWidgets.QPushButton(self.groupBox)
        self.erasing.setGeometry(QtCore.QRect(10, 190, 185, 23))
        self.erasing.setObjectName("erasing")
        
        self.classification.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.modelstructure = ModelStructure()
        self.model.clicked.connect(self.modelstructure.show)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Classification"))
        self.model.setText(_translate("MainWindow", " 1. Show Model Structure "))
        self.tensor.setText(_translate("MainWindow", " 2. Show TensorBoard "))
        self.test.setText(_translate("MainWindow", " 3. Test "))
        self.lineEdit_2.setText("")
        self.erasing.setText(_translate("MainWindow", " 4. Random-Erasing "))



class  ModelStructure(QtWidgets.QWidget):
    def __init__(self):
         super(ModelStructure, self).__init__()
         self.resize(400, 300)

         # Label
         self.label = QtWidgets.QLabel(self)
         self.label.setGeometry(0, 0, 400, 300)
         self.label.setText('Sub Window')
         self.label.setAlignment(QtCore.Qt.AlignCenter)
         self.label.setStyleSheet('font-size:40px')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    a= input()
    print(a)
    sys.exit(app.exec_())


