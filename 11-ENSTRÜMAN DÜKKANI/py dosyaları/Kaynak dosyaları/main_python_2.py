# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(938, 475)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 251, 161))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.ara_horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.ara_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ara_horizontalLayout.setObjectName("ara_horizontalLayout")
        self.label_ara = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_ara.setObjectName("label_ara")
        self.ara_horizontalLayout.addWidget(self.label_ara)
        self.arama_yap = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.arama_yap.setObjectName("arama_yap")
        self.ara_horizontalLayout.addWidget(self.arama_yap)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(300, 40, 591, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 220, 251, 251))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.enstr_ekle_buton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.enstr_ekle_buton.setObjectName("enstr_ekle_buton")
        self.verticalLayout_3.addWidget(self.enstr_ekle_buton)
        self.musteri_bilgi_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.musteri_bilgi_button.setObjectName("musteri_bilgi_button")
        self.verticalLayout_3.addWidget(self.musteri_bilgi_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "SATIŞ TAKİP SAYFASI"))
        self.label_ara.setText(_translate("Form", "<html><head/><body><p align=\"center\">ARA</p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "ENSTRÜMAN ADI"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "FİYAT"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "STOK SAYISI"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "SATIŞ SAYISI"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "İŞLEM"))
        self.enstr_ekle_buton.setText(_translate("Form", "ENSTRÜMAN EKLE"))
        self.musteri_bilgi_button.setText(_translate("Form", "MÜŞTERİ BİLGİLERİ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
