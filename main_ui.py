# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QCheckBox, QComboBox,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(741, 420)
        MainWindow.setMinimumSize(QSize(741, 420))
        MainWindow.setMaximumSize(QSize(741, 420))
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        MainWindow.setStyleSheet(u"QWidget{\n"
"background: #e9f5f5;\n"
"font: 12pt \"Calibri\";\n"
"}\n"
"QLineEdit{\n"
"background: #fcfcf7;\n"
"}\n"
"QPlainTextEdit{\n"
"font-size:10pt;\n"
"background: #fcfcf7;\n"
"}\n"
"QPushButton{\n"
"background:#fcfcf7;\n"
"}\n"
"QPushButton{\n"
"	border-radius: 0px;\n"
"    color: white;\n"
"    transition: .2s linear;\n"
"    background: #6a61c7;\n"
"}\n"
"QPushButton:pressed{\n"
"	box-shadow:0px -6px 0 #003CC5 inset;\n"
"	background: #534c9c;\n"
"}")
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(400, 120, 331, 20))
        self.checkBox.setChecked(True)
        self.shipperLine = QPlainTextEdit(self.centralwidget)
        self.shipperLine.setObjectName(u"shipperLine")
        self.shipperLine.setGeometry(QRect(10, 30, 201, 71))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.shipperLine.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 10, 121, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 10, 161, 16))
        self.driverLine = QPlainTextEdit(self.centralwidget)
        self.driverLine.setObjectName(u"driverLine")
        self.driverLine.setGeometry(QRect(520, 30, 201, 71))
        self.driverLine.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(590, 10, 71, 16))
        self.vehicleName = QLineEdit(self.centralwidget)
        self.vehicleName.setObjectName(u"vehicleName")
        self.vehicleName.setGeometry(QRect(520, 180, 201, 22))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(540, 160, 161, 20))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(520, 210, 221, 20))
        self.vehicleNumber = QLineEdit(self.centralwidget)
        self.vehicleNumber.setObjectName(u"vehicleNumber")
        self.vehicleNumber.setGeometry(QRect(520, 230, 201, 22))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(290, 160, 181, 20))
        self.driverName = QLineEdit(self.centralwidget)
        self.driverName.setObjectName(u"driverName")
        self.driverName.setGeometry(QRect(290, 180, 201, 22))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(290, 210, 181, 20))
        self.mppName = QLineEdit(self.centralwidget)
        self.mppName.setObjectName(u"mppName")
        self.mppName.setGeometry(QRect(290, 230, 201, 22))
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(10, 170, 261, 171))
        self.calendarWidget.setStyleSheet(u"background: #ffecbd;\n"
"color: black;\n"
"")
        self.ValueSpinBox = QSpinBox(self.centralwidget)
        self.ValueSpinBox.setObjectName(u"ValueSpinBox")
        self.ValueSpinBox.setGeometry(QRect(390, 280, 61, 31))
        self.ValueSpinBox.setStyleSheet(u"background:#fcfcf7;")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(290, 270, 91, 41))
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"font: 700 12pt \"Calibri\";")
        self.label_9.setTextFormat(Qt.TextFormat.AutoText)
        self.CLink = QLabel(self.centralwidget)
        self.CLink.setObjectName(u"CLink")
        self.CLink.setGeometry(QRect(10, 390, 161, 21))
        self.CLink.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.CLink.setOpenExternalLinks(True)
        self.CLink.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextSelectableByMouse)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(520, 260, 201, 22))
        self.comboBox.setStyleSheet(u"background:#fcfcf7;")
        self.SavePrintBtn = QPushButton(self.centralwidget)
        self.SavePrintBtn.setObjectName(u"SavePrintBtn")
        self.SavePrintBtn.setGeometry(QRect(560, 370, 161, 31))
        self.SavePrintBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.SavePrintBtn.setAutoFillBackground(False)
        self.SavePrintBtn.setStyleSheet(u"")
        self.SavePrintBtn.setCheckable(False)
        self.LmpChoise = QComboBox(self.centralwidget)
        self.LmpChoise.addItem("")
        self.LmpChoise.setObjectName(u"LmpChoise")
        self.LmpChoise.setGeometry(QRect(50, 110, 261, 31))
        self.LmpChoise.setStyleSheet(u"background:#fcfcf7;\n"
"")
        self.LmpChoise.setEditable(True)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 110, 41, 31))
        self.label_8.setStyleSheet(u"font: 700 12pt \"Calibri\";")
        self.LmpChoise_2 = QComboBox(self.centralwidget)
        self.LmpChoise_2.addItem("")
        self.LmpChoise_2.setObjectName(u"LmpChoise_2")
        self.LmpChoise_2.setGeometry(QRect(230, 30, 271, 71))
        self.LmpChoise_2.setStyleSheet(u"background:#fcfcf7;\n"
"    transition: .2s linear;")
        self.LmpChoise_2.setEditable(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.checkBox.raise_()
        self.shipperLine.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.driverLine.raise_()
        self.label_3.raise_()
        self.vehicleName.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.vehicleNumber.raise_()
        self.label_6.raise_()
        self.driverName.raise_()
        self.label_7.raise_()
        self.mppName.raise_()
        self.calendarWidget.raise_()
        self.ValueSpinBox.raise_()
        self.label_9.raise_()
        self.CLink.raise_()
        self.comboBox.raise_()
        self.SavePrintBtn.raise_()
        self.label_8.raise_()
        self.LmpChoise.raise_()
        self.LmpChoise_2.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u0410\u0422\u041d", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043d\u0430 \u043f\u0435\u0447\u0430\u0442\u044c", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u0437\u043e\u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044c -\u044d\u043a\u0441\u043f\u0435\u0434\u0438\u0442\u043e\u0440/\u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a?", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u0437\u043e\u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0437\u0447\u0438\u043a (\u044e\u0440.\u043b\u0438\u0446\u043e)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0434\u0438\u0442\u0435\u043b\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043d\u043e\u0435 \u0441\u0440\u0435\u0434\u0441\u0442\u0432\u043e", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442\u043d\u043e\u0433\u043e \u0441\u0440\u0435\u0434\u0441\u0442\u0432\u0430", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0412\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u041c\u041f\u041f", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \n"
"\u043a\u043e\u0440\u043e\u0431\u043e\u0432", None))
        self.CLink.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://1s-ut.lamoda.tech/app/ru_RU/\"><span style=\" text-decoration: underline; color:#004275;\">\u041e\u0442\u043a\u0440\u044b\u0442\u044c 1C \u0432 \u0431\u0440\u0430\u0443\u0437\u0435\u0440\u0435</span></a></p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1 - \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0441\u0442\u044c", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2 \u2013 \u0441\u043e\u0432\u043c\u0435\u0441\u0442\u043d\u0430\u044f \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0441\u0442\u044c \u0441\u0443\u043f\u0440\u0443\u0433\u043e\u0432", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"3 \u2013 \u0430\u0440\u0435\u043d\u0434\u0430", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"4 \u2013 \u043b\u0438\u0437\u0438\u043d\u0433", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"5 \u2013 \u0431\u0435\u0437\u0432\u043e\u0437\u043c\u0435\u0437\u0434\u043d\u043e\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435", None))

        self.SavePrintBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435/\u043f\u0435\u0447\u0430\u0442\u044c", None))
        self.LmpChoise.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0412\u0417:", None))
        self.LmpChoise_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))

    # retranslateUi

