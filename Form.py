# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from CezarCipher import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = UiMainWindow(self)
        self.ui.setupUi(self)
        self.show()
        self.setupSignals()

    def setupSignals(self):
        self.ui.key_lineEdit.textChanged.connect(self.shiftChanged)

        self.ui.encrypt_btn.clicked.connect(self.encrypt_BtnClicked)

        self.ui.key_lineEdit_2.textChanged.connect(self.shift_2Changed)

        self.ui.decrypt_btn.clicked.connect(self.decrypt_BtnPressed)

    def shiftChanged(self):
        self.ui.text_textEdit.setEnabled(True)
        self.ui.ciphertext_textEdit.setEnabled(True)
        self.ui.encrypt_btn.setEnabled(True)

    def shift_2Changed(self):
        self.ui.text_textEdit_2.setEnabled(True)
        self.ui.ciphertext_textEdit_2.setEnabled(True)
        self.ui.decrypt_btn.setEnabled(True)

    def get_error(self, widget: QtWidgets, error: bool):
        if error:
            self.ui.statusbar.addWidget(self.ui.error_label)
            widget.setStyleSheet('border: 1px solid red;')
            widget.setFocus()
        else:
            self.ui.statusbar.removeWidget(self.ui.error_label)
            widget.setStyleSheet('border: 1px solid black;')

    def encrypt_BtnClicked(self):
        if self.ui.key_lineEdit.text().isalpha():
            self.get_error(self.ui.key_lineEdit, False)
            key = self.ui.key_lineEdit.text()

            if self.ui.text_textEdit.toPlainText() != "":
                self.get_error(self.ui.text_textEdit, False)
                text = self.ui.text_textEdit.toPlainText()
                cipher = encrypt(key, text)
                self.ui.ciphertext_textEdit.setText(cipher)
            else:
                self.ui.error_label.setText('Ошибка: введите текст')
                self.get_error(self.ui.text_textEdit, True)
        else:
            self.ui.error_label.setText('Ошибка: ключом может быть только текст')
            self.get_error(self.ui.key_lineEdit, True)

    def decrypt_BtnPressed(self):
        if self.ui.key_lineEdit_2.text().isalpha():
            self.get_error(self.ui.key_lineEdit_2, False)
            key = self.ui.key_lineEdit_2.text()

            if self.ui.ciphertext_textEdit_2.toPlainText() != "":
                self.get_error(self.ui.ciphertext_textEdit_2, False)
                cipher = self.ui.ciphertext_textEdit_2.toPlainText()
                text = decrypt(key, cipher)
                self.ui.text_textEdit_2.setText(text)
            else:
                self.ui.error_label.setText('Ошибка: введите текст')
                self.get_error(self.ui.text_textEdit_2, True)
        else:
            self.ui.error_label.setText('Ошибка: ключом может быть только текст')
            self.get_error(self.ui.key_lineEdit_2, True)


class UiMainWindow(object):
    def __init__(self, mainwindow):
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_1 = QtWidgets.QWidget()
        self.text_textEdit = QtWidgets.QTextEdit(self.tab_1)
        self.encrypt_btn = QtWidgets.QPushButton(self.tab_1)
        self.text_label = QtWidgets.QLabel(self.tab_1)
        self.ciphertext_textEdit = QtWidgets.QTextEdit(self.tab_1)
        self.ciphertext_label = QtWidgets.QLabel(self.tab_1)
        self.key_lineEdit = QtWidgets.QLineEdit(self.tab_1)
        self.shift_label = QtWidgets.QLabel(self.tab_1)
        self.tab_2 = QtWidgets.QWidget()
        self.shift_label_2 = QtWidgets.QLabel(self.tab_2)
        self.key_lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.text_label_2 = QtWidgets.QLabel(self.tab_2)
        self.decrypt_btn = QtWidgets.QPushButton(self.tab_2)
        self.text_textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.ciphertext_textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.ciphertext_label_2 = QtWidgets.QLabel(self.tab_2)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.error_label = QtWidgets.QLabel(self.tab_1)

    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(332, 335)
        mainwindow.setMinimumSize(QtCore.QSize(332, 335))
        mainwindow.setMaximumSize(QtCore.QSize(332, 335))
        mainwindow.setWindowIcon((QtGui.QIcon('salad.ico')))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)

        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 541, 321))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")

        self.tab_1.setObjectName("tab_1")

        self.text_textEdit.setGeometry(QtCore.QRect(10, 40, 301, 91))
        self.text_textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.text_textEdit.setObjectName("text_textEdit")
        self.text_textEdit.setEnabled(False)
        self.text_textEdit.setTabChangesFocus(True)

        self.encrypt_btn.setGeometry(QtCore.QRect(116, 138, 75, 23))
        self.encrypt_btn.setObjectName("encrypt_btn")

        self.text_label.setGeometry(QtCore.QRect(140, 15, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.text_label.setFont(font)
        self.text_label.setObjectName("text_label")

        self.ciphertext_textEdit.setGeometry(QtCore.QRect(10, 190, 301, 91))
        self.ciphertext_textEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ciphertext_textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ciphertext_textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ciphertext_textEdit.setReadOnly(True)
        self.ciphertext_textEdit.setObjectName("ciphertext_textEdit")
        self.ciphertext_textEdit.setEnabled(False)

        self.ciphertext_label.setGeometry(QtCore.QRect(122, 165, 61, 16))
        self.ciphertext_label.setObjectName("ciphertext_label")

        self.key_lineEdit.setGeometry(QtCore.QRect(250, 10, 61, 20))
        self.key_lineEdit.setObjectName("key_lineEdit")

        self.shift_label.setGeometry(QtCore.QRect(220, 10, 31, 16))
        self.shift_label.setObjectName("shift_label")

        self.tabWidget.addTab(self.tab_1, "")

        self.tab_2.setObjectName("tab_2")

        self.shift_label_2.setGeometry(QtCore.QRect(220, 10, 31, 16))
        self.shift_label_2.setObjectName("shift_label_2")

        self.key_lineEdit_2.setGeometry(QtCore.QRect(250, 10, 61, 20))
        self.key_lineEdit_2.setObjectName("key_lineEdit_2")

        self.text_label_2.setGeometry(QtCore.QRect(140, 165, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)

        self.text_label_2.setFont(font)
        self.text_label_2.setObjectName("text_label_2")

        self.decrypt_btn.setGeometry(QtCore.QRect(116, 138, 75, 23))
        self.decrypt_btn.setObjectName("decrypt_btn")

        self.text_textEdit_2.setGeometry(QtCore.QRect(10, 190, 301, 91))
        self.text_textEdit_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_textEdit_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.text_textEdit_2.setReadOnly(True)
        self.text_textEdit_2.setObjectName("text_textEdit_2")
        self.text_textEdit_2.setEnabled(False)
        self.text_textEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)

        self.ciphertext_textEdit_2.setGeometry(QtCore.QRect(10, 40, 301, 91))
        self.ciphertext_textEdit_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.ciphertext_textEdit_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ciphertext_textEdit_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ciphertext_textEdit_2.setReadOnly(False)
        self.ciphertext_textEdit_2.setObjectName("ciphertext_textEdit_2")
        self.ciphertext_textEdit_2.setEnabled(False)
        self.ciphertext_textEdit_2.setTabChangesFocus(True)

        self.ciphertext_label_2.setGeometry(QtCore.QRect(122, 15, 61, 16))
        self.ciphertext_label_2.setObjectName("ciphertext_label_2")

        self.tabWidget.addTab(self.tab_2, "")

        mainwindow.setCentralWidget(self.centralwidget)

        self.statusbar.setStatusTip("")
        self.statusbar.setObjectName("statusbar")

        mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainwindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

        self.error_label.setStyleSheet('color: red;')

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "Modified Cezar cipher"))
        self.text_textEdit.setStatusTip(_translate("mainwindow", "Text input box for encryption"))
        self.encrypt_btn.setText(_translate("mainwindow", "Encrypt"))
        self.text_label.setText(_translate("mainwindow", "Text"))
        self.ciphertext_textEdit.setStatusTip(_translate("mainwindow", "Ciphertext Output Window"))
        self.ciphertext_label.setText(_translate("mainwindow", "Ciphertext"))
        self.key_lineEdit.setStatusTip(_translate("mainwindow", "Key input field"))
        self.shift_label.setText(_translate("mainwindow", "Key"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("mainwindow", "Encrypt"))
        self.shift_label_2.setText(_translate("mainwindow", "Key"))
        self.key_lineEdit_2.setStatusTip(_translate("mainwindow", "Key input field"))
        self.text_label_2.setText(_translate("mainwindow", "Text"))
        self.decrypt_btn.setText(_translate("mainwindow", "Decrypt"))
        self.text_textEdit_2.setStatusTip(_translate("mainwindow", "Decrypted text output window"))
        self.ciphertext_textEdit_2.setStatusTip(_translate("mainwindow", "Decryption input window"))
        self.ciphertext_label_2.setText(_translate("mainwindow", "Ciphertext"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainwindow", "Decrypt"))
