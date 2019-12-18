# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui',
# licensing of 'main2.ui' applies.
#
# Created: Tue Dec 17 22:54:53 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(851, 411)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 521))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("256jpconverter.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background-color:#B0BEC5;")
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setMinimumSize(QtCore.QSize(800, 380))
        self.central_widget.setMaximumSize(QtCore.QSize(16777215, 600))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.central_widget.setFont(font)
        self.central_widget.setObjectName("central_widget")
        self.button_convert = QtWidgets.QPushButton(self.central_widget)
        self.button_convert.setGeometry(QtCore.QRect(730, 190, 110, 51))
        self.button_convert.setStyleSheet("color:#ffffff;background-color:#42a5f5;font:arial;font-size:16px;font-weight:bold;")
        self.button_convert.setObjectName("button_convert")
        self.input1 = QtWidgets.QLineEdit(self.central_widget)
        self.input1.setGeometry(QtCore.QRect(385, 190, 291, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input1.sizePolicy().hasHeightForWidth())
        self.input1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.input1.setFont(font)
        self.input1.setStyleSheet("background-color:#eeeeee;font-size:20px;")
        self.input1.setInputMask("")
        self.input1.setMaxLength(20)
        self.input1.setObjectName("input1")
        self.button_from_metric = QtWidgets.QPushButton(self.central_widget)
        self.button_from_metric.setGeometry(QtCore.QRect(385, 0, 110, 60))
        self.button_from_metric.setMinimumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.button_from_metric.setFont(font)
        self.button_from_metric.setStyleSheet("color:white;background-color:#1565c0;font:arial;font-size:17px;font-weight:bold;")
        self.button_from_metric.setCheckable(False)
        self.button_from_metric.setAutoDefault(False)
        self.button_from_metric.setFlat(False)
        self.button_from_metric.setObjectName("button_from_metric")
        self.button_from_jpmeasure = QtWidgets.QPushButton(self.central_widget)
        self.button_from_jpmeasure.setGeometry(QtCore.QRect(500, 0, 110, 60))
        self.button_from_jpmeasure.setMinimumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.button_from_jpmeasure.setFont(font)
        self.button_from_jpmeasure.setStyleSheet("color:white;background-color:#1565c0;font:arial;font-size:17px;font-weight:bold;")
        self.button_from_jpmeasure.setFlat(False)
        self.button_from_jpmeasure.setObjectName("button_from_jpmeasure")
        self.button_to_jpyear = QtWidgets.QPushButton(self.central_widget)
        self.button_to_jpyear.setGeometry(QtCore.QRect(615, 65, 110, 60))
        self.button_to_jpyear.setMinimumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.button_to_jpyear.setFont(font)
        self.button_to_jpyear.setStyleSheet("color:white;background-color:#0288d1;font:arial;font-size:17px;font-weight:bold;")
        self.button_to_jpyear.setFlat(False)
        self.button_to_jpyear.setObjectName("button_to_jpyear")
        self.button_exit = QtWidgets.QPushButton(self.central_widget)
        self.button_exit.setGeometry(QtCore.QRect(730, 290, 110, 50))
        self.button_exit.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.button_exit.setFont(font)
        self.button_exit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_exit.setStyleSheet("color:#ffffff;background-color:#777777;font:arial;font-size:17px;font-weight:bold;")
        self.button_exit.setFlat(False)
        self.button_exit.setObjectName("button_exit")
        self.button_to_jpmeasure = QtWidgets.QPushButton(self.central_widget)
        self.button_to_jpmeasure.setGeometry(QtCore.QRect(500, 65, 110, 60))
        self.button_to_jpmeasure.setMinimumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.button_to_jpmeasure.setFont(font)
        self.button_to_jpmeasure.setStyleSheet("color:white;background-color:#0288d1;font:arial;font-size:17px;font-weight:bold;")
        self.button_to_jpmeasure.setFlat(False)
        self.button_to_jpmeasure.setObjectName("button_to_jpmeasure")
        self.button_zodiac = QtWidgets.QPushButton(self.central_widget)
        self.button_zodiac.setGeometry(QtCore.QRect(730, 0, 110, 60))
        self.button_zodiac.setMinimumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.button_zodiac.setFont(font)
        self.button_zodiac.setStyleSheet("color:white;background-color:#1565c0;font:arial;font-size:17px;font-weight:bold;")
        self.button_zodiac.setFlat(False)
        self.button_zodiac.setObjectName("button_zodiac")
        self.button_from_jpyear = QtWidgets.QPushButton(self.central_widget)
        self.button_from_jpyear.setGeometry(QtCore.QRect(615, 0, 110, 60))
        self.button_from_jpyear.setMinimumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.button_from_jpyear.setFont(font)
        self.button_from_jpyear.setStyleSheet("color:white;background-color:#1565c0;font:arial;font-size:17px;font-weight:bold;")
        self.button_from_jpyear.setObjectName("button_from_jpyear")
        self.label_instructions1 = QtWidgets.QLabel(self.central_widget)
        self.label_instructions1.setGeometry(QtCore.QRect(385, 140, 391, 46))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_instructions1.setFont(font)
        self.label_instructions1.setStyleSheet("font-size:20px;color:#222222;padding:11px 0px 11px 0px;")
        self.label_instructions1.setObjectName("label_instructions1")
        self.label_output2 = QtWidgets.QTextEdit(self.central_widget)
        self.label_output2.setGeometry(QtCore.QRect(385, 260, 341, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setWeight(50)
        font.setBold(False)
        self.label_output2.setFont(font)
        self.label_output2.setStyleSheet("")
        self.label_output2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_output2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_output2.setLineWidth(0)
        self.label_output2.setReadOnly(True)
        self.label_output2.setObjectName("label_output2")
        self.conv_layout = QtWidgets.QScrollArea(self.central_widget)
        self.conv_layout.setGeometry(QtCore.QRect(10, 70, 261, 310))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.conv_layout.setFont(font)
        self.conv_layout.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.conv_layout.setFrameShadow(QtWidgets.QFrame.Plain)
        self.conv_layout.setLineWidth(0)
        self.conv_layout.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.conv_layout.setWidgetResizable(True)
        self.conv_layout.setObjectName("conv_layout")
        self.conv_layout_contents = QtWidgets.QWidget()
        self.conv_layout_contents.setGeometry(QtCore.QRect(0, 0, 261, 310))
        self.conv_layout_contents.setObjectName("conv_layout_contents")
        self.conv_layout.setWidget(self.conv_layout_contents)
        self.button_to_metric = QtWidgets.QPushButton(self.central_widget)
        self.button_to_metric.setGeometry(QtCore.QRect(385, 65, 110, 60))
        self.button_to_metric.setMinimumSize(QtCore.QSize(100, 60))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.button_to_metric.setFont(font)
        self.button_to_metric.setAutoFillBackground(False)
        self.button_to_metric.setStyleSheet("color:white;background-color:#0288d1;font:arial;font-size:17px;font-weight:bold;")
        self.button_to_metric.setFlat(False)
        self.button_to_metric.setObjectName("button_to_metric")
        self.label_header1 = QtWidgets.QLabel(self.central_widget)
        self.label_header1.setGeometry(QtCore.QRect(10, 0, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        self.label_header1.setFont(font)
        self.label_header1.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_header1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_header1.setLineWidth(2)
        self.label_header1.setObjectName("label_header1")
        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 851, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Measures = QtWidgets.QMenu(self.menubar)
        self.menu_Measures.setObjectName("menu_Measures")
        self.menu_Years = QtWidgets.QMenu(self.menubar)
        self.menu_Years.setObjectName("menu_Years")
        MainWindow.setMenuBar(self.menubar)
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_from_jpyear = QtWidgets.QAction(MainWindow)
        self.action_from_jpyear.setObjectName("action_from_jpyear")
        self.action_to_jpyear = QtWidgets.QAction(MainWindow)
        self.action_to_jpyear.setObjectName("action_to_jpyear")
        self.action_zodiac = QtWidgets.QAction(MainWindow)
        self.action_zodiac.setObjectName("action_zodiac")
        self.action_from_metric = QtWidgets.QAction(MainWindow)
        self.action_from_metric.setObjectName("action_from_metric")
        self.action_to_metric = QtWidgets.QAction(MainWindow)
        self.action_to_metric.setObjectName("action_to_metric")
        self.action_from_jpmeasure = QtWidgets.QAction(MainWindow)
        self.action_from_jpmeasure.setObjectName("action_from_jpmeasure")
        self.action_to_jpmeasure = QtWidgets.QAction(MainWindow)
        self.action_to_jpmeasure.setObjectName("action_to_jpmeasure")
        self.action_from_jpyear_historic = QtWidgets.QAction(MainWindow)
        self.action_from_jpyear_historic.setObjectName("action_from_jpyear_historic")
        self.menu_File.addAction(self.action_exit)
        self.menu_Measures.addAction(self.action_from_metric)
        self.menu_Measures.addAction(self.action_to_metric)
        self.menu_Measures.addSeparator()
        self.menu_Measures.addAction(self.action_from_jpmeasure)
        self.menu_Measures.addAction(self.action_to_jpmeasure)
        self.menu_Years.addAction(self.action_from_jpyear)
        self.menu_Years.addAction(self.action_from_jpyear_historic)
        self.menu_Years.addAction(self.action_to_jpyear)
        self.menu_Years.addSeparator()
        self.menu_Years.addAction(self.action_zodiac)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Measures.menuAction())
        self.menubar.addAction(self.menu_Years.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.button_from_metric, self.button_from_jpmeasure)
        MainWindow.setTabOrder(self.button_from_jpmeasure, self.button_from_jpyear)
        MainWindow.setTabOrder(self.button_from_jpyear, self.button_zodiac)
        MainWindow.setTabOrder(self.button_zodiac, self.button_to_metric)
        MainWindow.setTabOrder(self.button_to_metric, self.button_to_jpmeasure)
        MainWindow.setTabOrder(self.button_to_jpmeasure, self.button_to_jpyear)
        MainWindow.setTabOrder(self.button_to_jpyear, self.input1)
        MainWindow.setTabOrder(self.input1, self.button_convert)
        MainWindow.setTabOrder(self.button_convert, self.button_exit)
        MainWindow.setTabOrder(self.button_exit, self.label_output2)
        MainWindow.setTabOrder(self.label_output2, self.conv_layout)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "JP Converter", None, -1))
        self.button_convert.setText(QtWidgets.QApplication.translate("MainWindow", "Convert", None, -1))
        self.button_from_metric.setText(QtWidgets.QApplication.translate("MainWindow", "From \n"
"Metric", None, -1))
        self.button_from_jpmeasure.setText(QtWidgets.QApplication.translate("MainWindow", "From JP \n"
"Measures", None, -1))
        self.button_to_jpyear.setText(QtWidgets.QApplication.translate("MainWindow", "To JP \n"
"Years", None, -1))
        self.button_exit.setText(QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))
        self.button_to_jpmeasure.setText(QtWidgets.QApplication.translate("MainWindow", "To JP \n"
"Measures", None, -1))
        self.button_zodiac.setText(QtWidgets.QApplication.translate("MainWindow", "Zodiac\n"
"Years", None, -1))
        self.button_from_jpyear.setText(QtWidgets.QApplication.translate("MainWindow", "From JP \n"
"Years", None, -1))
        self.label_instructions1.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.label_output2.setHtml(QtWidgets.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, -1))
        self.button_to_metric.setText(QtWidgets.QApplication.translate("MainWindow", "To \n"
"Metric", None, -1))
        self.label_header1.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.menu_File.setTitle(QtWidgets.QApplication.translate("MainWindow", "&File", None, -1))
        self.menu_Measures.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Measurements", None, -1))
        self.menu_Years.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Calendar", None, -1))
        self.action_exit.setText(QtWidgets.QApplication.translate("MainWindow", "E&xit", None, -1))
        self.action_from_jpyear.setText(QtWidgets.QApplication.translate("MainWindow", "From &Japanese years (modern)", None, -1))
        self.action_to_jpyear.setText(QtWidgets.QApplication.translate("MainWindow", "To Japanese &years", None, -1))
        self.action_zodiac.setText(QtWidgets.QApplication.translate("MainWindow", "&Zodiac years", None, -1))
        self.action_from_metric.setText(QtWidgets.QApplication.translate("MainWindow", "From &Metric", None, -1))
        self.action_to_metric.setText(QtWidgets.QApplication.translate("MainWindow", "To M&etric", None, -1))
        self.action_from_jpmeasure.setText(QtWidgets.QApplication.translate("MainWindow", "&From Japanese measurements", None, -1))
        self.action_to_jpmeasure.setText(QtWidgets.QApplication.translate("MainWindow", "&To Japanese measurements", None, -1))
        self.action_from_jpyear_historic.setText(QtWidgets.QApplication.translate("MainWindow", "From Japanese years (&historic)", None, -1))

