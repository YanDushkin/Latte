# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 340)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.variety_lineedit = QtWidgets.QLineEdit(Form)
        self.variety_lineedit.setGeometry(QtCore.QRect(190, 10, 161, 31))
        self.variety_lineedit.setObjectName("variety_lineedit")
        self.variety_label = QtWidgets.QLabel(Form)
        self.variety_label.setGeometry(QtCore.QRect(20, 10, 161, 31))
        self.variety_label.setObjectName("variety_label")
        self.degree_of_roasting_label = QtWidgets.QLabel(Form)
        self.degree_of_roasting_label.setGeometry(QtCore.QRect(20, 60, 161, 31))
        self.degree_of_roasting_label.setObjectName("degree_of_roasting_label")
        self.degree_of_roasting_spinbox = QtWidgets.QSpinBox(Form)
        self.degree_of_roasting_spinbox.setGeometry(QtCore.QRect(190, 60, 161, 31))
        self.degree_of_roasting_spinbox.setMinimum(1)
        self.degree_of_roasting_spinbox.setMaximum(7)
        self.degree_of_roasting_spinbox.setProperty("value", 3)
        self.degree_of_roasting_spinbox.setObjectName("degree_of_roasting_spinbox")
        self.taste_description_label = QtWidgets.QLabel(Form)
        self.taste_description_label.setGeometry(QtCore.QRect(20, 150, 161, 31))
        self.taste_description_label.setObjectName("taste_description_label")
        self.ground_label = QtWidgets.QLabel(Form)
        self.ground_label.setGeometry(QtCore.QRect(20, 110, 151, 31))
        self.ground_label.setObjectName("ground_label")
        self.ground_checkbox = QtWidgets.QCheckBox(Form)
        self.ground_checkbox.setGeometry(QtCore.QRect(190, 110, 21, 23))
        self.ground_checkbox.setText("")
        self.ground_checkbox.setObjectName("ground_checkbox")
        self.taste_sescription_lineedit = QtWidgets.QLineEdit(Form)
        self.taste_sescription_lineedit.setGeometry(QtCore.QRect(190, 150, 161, 31))
        self.taste_sescription_lineedit.setObjectName("taste_sescription_lineedit")
        self.price_spinbox = QtWidgets.QSpinBox(Form)
        self.price_spinbox.setGeometry(QtCore.QRect(190, 200, 161, 31))
        self.price_spinbox.setMinimum(1)
        self.price_spinbox.setMaximum(10000)
        self.price_spinbox.setObjectName("price_spinbox")
        self.price_label = QtWidgets.QLabel(Form)
        self.price_label.setGeometry(QtCore.QRect(20, 200, 151, 31))
        self.price_label.setObjectName("price_label")
        self.volume_label = QtWidgets.QLabel(Form)
        self.volume_label.setGeometry(QtCore.QRect(20, 250, 161, 21))
        self.volume_label.setObjectName("volume_label")
        self.volum_spinbox = QtWidgets.QSpinBox(Form)
        self.volum_spinbox.setGeometry(QtCore.QRect(190, 250, 161, 31))
        self.volum_spinbox.setMinimum(1)
        self.volum_spinbox.setMaximum(10000)
        self.volum_spinbox.setObjectName("volum_spinbox")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 290, 171, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление нового кофе"))
        self.variety_label.setText(_translate("Form", "Сорт:"))
        self.degree_of_roasting_label.setText(_translate("Form", "Степень обжарки:"))
        self.taste_description_label.setText(_translate("Form", "Описание вкуса:"))
        self.ground_label.setText(_translate("Form", "Молотый"))
        self.price_label.setText(_translate("Form", "Цена:"))
        self.volume_label.setText(_translate("Form", "Объём упаковки:"))
        self.pushButton.setText(_translate("Form", "Добавить"))
