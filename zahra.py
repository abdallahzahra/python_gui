# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '__main__.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_btn(object):
    def setupUi(self, btn):
        btn.setObjectName("btn")
        btn.resize(358, 502)
        btn.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.centralwidget = QtWidgets.QWidget(btn)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.player_name = QtWidgets.QLabel(self.centralwidget)
        self.player_name.setObjectName("player_name")
        self.gridLayout_2.addWidget(self.player_name, 3, 2, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 3, 1, 1)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setObjectName("start_button")
        self.gridLayout_2.addWidget(self.start_button, 2, 1, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ptn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_5.setMinimumSize(QtCore.QSize(100, 100))
        self.ptn_5.setMaximumSize(QtCore.QSize(100, 100))
        self.ptn_5.setText("")
        self.ptn_5.setObjectName("ptn_5")
        self.gridLayout.addWidget(self.ptn_5, 1, 1, 1, 1)
        self.ptn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_9.setMinimumSize(QtCore.QSize(100, 100))
        self.ptn_9.setMaximumSize(QtCore.QSize(100, 100))
        self.ptn_9.setText("")
        self.ptn_9.setObjectName("ptn_9")
        self.gridLayout.addWidget(self.ptn_9, 2, 2, 1, 1)
        self.ptn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_4.setMinimumSize(QtCore.QSize(100, 100))
        self.ptn_4.setMaximumSize(QtCore.QSize(100, 100))
        self.ptn_4.setText("")
        self.ptn_4.setObjectName("ptn_4")
        self.gridLayout.addWidget(self.ptn_4, 1, 0, 1, 1)
        self.ptn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_6.setMinimumSize(QtCore.QSize(100, 100))
        self.ptn_6.setMaximumSize(QtCore.QSize(100, 100))
        self.ptn_6.setText("")
        self.ptn_6.setObjectName("ptn_6")
        self.gridLayout.addWidget(self.ptn_6, 1, 2, 1, 1)
        self.ptn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_3.setMinimumSize(QtCore.QSize(100, 100))
        self.ptn_3.setMaximumSize(QtCore.QSize(100, 100))
        self.ptn_3.setText("")
        self.ptn_3.setObjectName("ptn_3")
        self.gridLayout.addWidget(self.ptn_3, 0, 2, 1, 1)
        self.ptn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_8.setMinimumSize(QtCore.QSize(100, 100))
        self.ptn_8.setMaximumSize(QtCore.QSize(100, 100))
        self.ptn_8.setText("")
        self.ptn_8.setObjectName("ptn_8")
        self.gridLayout.addWidget(self.ptn_8, 2, 1, 1, 1)
        self.ptn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_7.setMinimumSize(QtCore.QSize(100, 100))
        self.ptn_7.setMaximumSize(QtCore.QSize(100, 100))
        self.ptn_7.setText("")
        self.ptn_7.setObjectName("ptn_7")
        self.gridLayout.addWidget(self.ptn_7, 2, 0, 1, 1)
        self.ptn = QtWidgets.QPushButton(self.centralwidget)
        self.ptn.setMinimumSize(QtCore.QSize(100, 100))
        self.ptn.setMaximumSize(QtCore.QSize(100, 100))
        self.ptn.setText("")
        self.ptn.setObjectName("ptn")
        self.gridLayout.addWidget(self.ptn, 0, 0, 1, 1)
        self.ptn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.ptn_2.setMinimumSize(QtCore.QSize(100, 100))
        self.ptn_2.setMaximumSize(QtCore.QSize(100, 100))
        self.ptn_2.setText("")
        self.ptn_2.setObjectName("ptn_2")
        self.gridLayout.addWidget(self.ptn_2, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.o_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.o_radio.setObjectName("o_radio")
        self.horizontalLayout.addWidget(self.o_radio)
        self.x_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.x_radio.setObjectName("x_radio")
        self.horizontalLayout.addWidget(self.x_radio)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 3, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        btn.setCentralWidget(self.centralwidget)

        self.retranslateUi(btn)
        QtCore.QMetaObject.connectSlotsByName(btn)

    def retranslateUi(self, btn):
        _translate = QtCore.QCoreApplication.translate
        btn.setWindowTitle(_translate("btn", "tictactoo"))
        self.player_name.setText(_translate("btn", "player 1"))
        self.start_button.setText(_translate("btn", "start"))
        self.label.setText(_translate("btn", "select"))
        self.o_radio.setText(_translate("btn", "O"))
        self.x_radio.setText(_translate("btn", "X"))
