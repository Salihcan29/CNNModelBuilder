# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QLineEdit, QMessageBox, QFileDialog, QDialog

class Main_ui(QMainWindow):
    def setupUi(self):
        self.setObjectName("Form")
        self.resize(540, 360)
        self.setMinimumSize(QtCore.QSize(540, 360))
        self.setMaximumSize(QtCore.QSize(540, 360))
        self.setBaseSize(QtCore.QSize(480, 360))
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 10, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.newmdl = QtWidgets.QPushButton(self)
        self.newmdl.setGeometry(QtCore.QRect(430, 60, 101, 41))
        self.newmdl.setObjectName("newmdl")
        self.loadmdl = QtWidgets.QPushButton(self)
        self.loadmdl.setGeometry(QtCore.QRect(430, 110, 101, 41))
        self.loadmdl.setObjectName("loadmdl")
        self.exit = QtWidgets.QPushButton(self)
        self.exit.setGeometry(QtCore.QRect(430, 260, 101, 61))
        self.exit.setObjectName("exit")
        self.mdltable = QtWidgets.QTableWidget(self)
        self.mdltable.setGeometry(QtCore.QRect(10, 60, 411, 261))
        self.mdltable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mdltable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mdltable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.mdltable.setAutoScroll(True)
        self.mdltable.setRowCount(0)
        self.mdltable.setColumnCount(4)
        self.mdltable.setObjectName("mdltable")
        item = QtWidgets.QTableWidgetItem()
        self.mdltable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.mdltable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.mdltable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.mdltable.setHorizontalHeaderItem(3, item)
        self.selectinp = QtWidgets.QPushButton(self)
        self.selectinp.setGeometry(QtCore.QRect(430, 210, 101, 41))
        self.selectinp.setObjectName("selectinp")
        self.savemdl = QtWidgets.QPushButton(self)
        self.savemdl.setEnabled(False)
        self.savemdl.setGeometry(QtCore.QRect(430, 160, 101, 41))
        self.savemdl.setObjectName("savemdl")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.selectinp.clicked.connect(self.choose_file)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Model View"))
        self.newmdl.setText(_translate("Form", "New Model"))
        self.loadmdl.setText(_translate("Form", "Load Model"))
        self.exit.setText(_translate("Form", "Exit"))
        item = self.mdltable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.mdltable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Type"))
        item = self.mdltable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Count"))
        item = self.mdltable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Activation"))
        self.selectinp.setText(_translate("Form", "Select Inputs"))
        self.savemdl.setText(_translate("Form", "Save Model"))
        
    def choose_file(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        _translate = QtCore.QCoreApplication.translate
        if file != "":
            self.label.setText(_translate("CNNModelBuilder",  "Folder selected"))
        print(file)