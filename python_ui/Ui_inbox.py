# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/nikita/Documents/network/project_aiosmtpd/project_aiosmtpd/inbox.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(451, 382)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 2, 1, 1)
        self.showButton = QtWidgets.QPushButton(self.centralwidget)
        self.showButton.setObjectName("showButton")
        self.gridLayout.addWidget(self.showButton, 1, 3, 1, 1)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 2, 0, 1, 4)
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setObjectName("quitButton")
        self.gridLayout.addWidget(self.quitButton, 3, 0, 1, 1)
        self.expandButton = QtWidgets.QPushButton(self.centralwidget)
        self.expandButton.setObjectName("expandButton")
        self.gridLayout.addWidget(self.expandButton, 3, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 451, 22))
        self.menubar.setObjectName("menubar")
        self.menuNew_mail = QtWidgets.QMenu(self.menubar)
        self.menuNew_mail.setObjectName("menuNew_mail")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_mail = QtWidgets.QAction(MainWindow)
        self.action_mail.setObjectName("action_mail")
        self.action_Inbox = QtWidgets.QAction(MainWindow)
        self.action_Inbox.setObjectName("action_Inbox")
        self.actionOutbox = QtWidgets.QAction(MainWindow)
        self.actionOutbox.setObjectName("actionOutbox")
        self.actionSource_code = QtWidgets.QAction(MainWindow)
        self.actionSource_code.setObjectName("actionSource_code")
        self.actionPresentation = QtWidgets.QAction(MainWindow)
        self.actionPresentation.setObjectName("actionPresentation")
        self.actionLogout = QtWidgets.QAction(MainWindow)
        self.actionLogout.setObjectName("actionLogout")
        self.menuNew_mail.addSeparator()
        self.menuNew_mail.addAction(self.action_mail)
        self.menuNew_mail.addSeparator()
        self.menuNew_mail.addAction(self.action_Inbox)
        self.menuNew_mail.addAction(self.actionOutbox)
        self.menuNew_mail.addSeparator()
        self.menuNew_mail.addAction(self.actionLogout)
        self.menuAbout.addAction(self.actionSource_code)
        self.menuAbout.addAction(self.actionPresentation)
        self.menubar.addAction(self.menuNew_mail.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Username Inbox"))
        self.label.setText(_translate("MainWindow", "Select amount of most recent messages to be shown:"))
        self.showButton.setText(_translate("MainWindow", "Show"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))
        self.expandButton.setText(_translate("MainWindow", "Expand"))
        self.menuNew_mail.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.action_mail.setText(_translate("MainWindow", "New mail"))
        self.action_Inbox.setText(_translate("MainWindow", "Inbox"))
        self.actionOutbox.setText(_translate("MainWindow", "Outbox"))
        self.actionSource_code.setText(_translate("MainWindow", "Source code"))
        self.actionPresentation.setText(_translate("MainWindow", "Presentation"))
        self.actionLogout.setText(_translate("MainWindow", "Logout"))

