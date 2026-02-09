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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QWidget)
from data import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 380)
        MainWindow.setMinimumSize(QSize(750, 380))
        MainWindow.setMaximumSize(QSize(750, 380))
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        icon = QIcon()
        if QIcon.hasThemeIcon(QIcon.ThemeIcon.UserOffline):
            icon = QIcon.fromTheme(QIcon.ThemeIcon.UserOffline)
        else:
            icon.addFile(u":/icons/icons8-\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442\u0441\u044f-48.png", QSize(), QIcon.Mode.Selected, QIcon.State.On)

        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget{\n"
"font: 12pt \"Calibri\";\n"
"}\n"
"QLineEdit{\n"
"background: #fcfcf7;\n"
"color:black;\n"
"}\n"
"QPlainTextEdit{\n"
"font-size:10pt;\n"
"background: #fcfcf7;\n"
"color:black;\n"
"}\n"
"QListView{\n"
"background: #fcfcf7;\n"
"}\n"
"QPushButton{\n"
"background:#fcfcf7;\n"
"}\n"
"\n"
"QPushButton{\n"
"color:black;\n"
"}\n"
"\n"
"QDateEdit{\n"
"background: #fcfcf7;\n"
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
        self.checkBox.setGeometry(QRect(20, 170, 351, 20))
        self.checkBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.checkBox.setChecked(True)
        self.shipperLine = QPlainTextEdit(self.centralwidget)
        self.shipperLine.setObjectName(u"shipperLine")
        self.shipperLine.setGeometry(QRect(10, 30, 221, 101))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.shipperLine.setFont(font)
        self.shipperLine.setStyleSheet(u"color:black;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 10, 121, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 10, 161, 16))
        self.driverLine = QPlainTextEdit(self.centralwidget)
        self.driverLine.setObjectName(u"driverLine")
        self.driverLine.setGeometry(QRect(510, 30, 231, 101))
        self.driverLine.setFont(font)
        self.driverLine.setStyleSheet(u"color:black;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(590, 10, 71, 16))
        self.vehicleName = QLineEdit(self.centralwidget)
        self.vehicleName.setObjectName(u"vehicleName")
        self.vehicleName.setGeometry(QRect(510, 160, 231, 22))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(550, 140, 161, 20))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(520, 190, 221, 20))
        self.vehicleNumber = QLineEdit(self.centralwidget)
        self.vehicleNumber.setObjectName(u"vehicleNumber")
        self.vehicleNumber.setGeometry(QRect(510, 220, 231, 22))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(570, 250, 111, 20))
        self.driverName = QLineEdit(self.centralwidget)
        self.driverName.setObjectName(u"driverName")
        self.driverName.setGeometry(QRect(510, 270, 231, 21))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(250, 240, 81, 20))
        self.mppName = QLineEdit(self.centralwidget)
        self.mppName.setObjectName(u"mppName")
        self.mppName.setGeometry(QRect(200, 260, 201, 21))
        self.ValueSpinBox = QSpinBox(self.centralwidget)
        self.ValueSpinBox.setObjectName(u"ValueSpinBox")
        self.ValueSpinBox.setGeometry(QRect(120, 310, 111, 31))
        self.ValueSpinBox.setStyleSheet(u"background:#fcfcf7;\n"
"color:black;")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 300, 91, 41))
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
        self.CLink.setGeometry(QRect(10, 350, 161, 21))
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
        self.comboBox.setGeometry(QRect(510, 310, 231, 22))
        self.comboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.comboBox.setStyleSheet(u"background:#fcfcf7;\n"
"color:black;")
        self.PrintBtn = QPushButton(self.centralwidget)
        self.PrintBtn.setObjectName(u"PrintBtn")
        self.PrintBtn.setGeometry(QRect(310, 330, 121, 31))
        self.PrintBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.PrintBtn.setAutoFillBackground(False)
        self.PrintBtn.setStyleSheet(u"")
        self.PrintBtn.setCheckable(False)
        self.LmpChoise = QComboBox(self.centralwidget)
        self.LmpChoise.addItem("")
        self.LmpChoise.setObjectName(u"LmpChoise")
        self.LmpChoise.setGeometry(QRect(60, 200, 381, 31))
        self.LmpChoise.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.LmpChoise.setStyleSheet(u"background:#fcfcf7;\n"
"color:black;\n"
"")
        self.LmpChoise.setEditable(True)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 200, 41, 31))
        self.label_8.setStyleSheet(u"font: 700 12pt \"Calibri\";")
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(70, 260, 121, 21))
        self.dateEdit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.dateEdit.setStyleSheet(u"color:black;")
        self.dateEdit.setMinimumDateTime(QDateTime(QDate(2025, 1, 1), QTime(6, 0, 0)))
        self.dateEdit.setMaximumDate(QDate(2100, 12, 31))
        self.dateEdit.setMinimumDate(QDate(2025, 1, 1))
        self.dateEdit.setCalendarPopup(True)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 260, 41, 21))
        self.transferBtn = QPushButton(self.centralwidget)
        self.transferBtn.setObjectName(u"transferBtn")
        self.transferBtn.setGeometry(QRect(300, 140, 151, 21))
        self.transferBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.transferBtn.setAutoFillBackground(False)
        self.transferBtn.setStyleSheet(u"")
        self.transferBtn.setCheckable(False)
        self.transLine = QPlainTextEdit(self.centralwidget)
        self.transLine.setObjectName(u"transLine")
        self.transLine.setGeometry(QRect(250, 30, 241, 101))
        self.transLine.setFont(font)
        self.transLine.setStyleSheet(u"color:black;")
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
        self.ValueSpinBox.raise_()
        self.label_9.raise_()
        self.CLink.raise_()
        self.comboBox.raise_()
        self.PrintBtn.raise_()
        self.label_8.raise_()
        self.LmpChoise.raise_()
        self.dateEdit.raise_()
        self.label_10.raise_()
        self.transferBtn.raise_()
        self.transLine.raise_()

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

        self.PrintBtn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0435\u0447\u0430\u0442\u0430\u0442\u044c", None))
        self.LmpChoise.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0412\u0417:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430:", None))
        self.transferBtn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
    # retranslateUi

