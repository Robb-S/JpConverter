import sys
from PySide2 import QtXml
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QWidget, QRadioButton, QVBoxLayout
from PySide2.QtWidgets import QTextEdit, QScrollArea, QAction, QMainWindow, QMenuBar
from PySide2.QtCore import QFile, QObject, Qt, QPoint, QCoreApplication
from PySide2.QtGui import QIntValidator, QDoubleValidator
from jpconvhelper import makeHeader1, makeStyleSheet, strToNum, getMenuStyle
from converters import *
from yearconverter import *
from messages import *
from ui_mainwindow3 import Ui_MainWindow3               # used for deployment version

#import os
#print ("** current directory: ", os.getcwd())          # use this to figure out where to put UI files during development
theUIFileName = 'main3.ui'
devMode = "development"     # quick development, using UI file made directly from QT Designer
#devMode = "deployment"     # deployment version, using a .py version of the UI file 

class MainWindow(QMainWindow):
    def __init__(self, ui_file, devMode, parent=None):       
        super(MainWindow, self).__init__()    
        self.uiFileName = ui_file                           # use this if there are multiple UI files
        if devMode == "development":                        # use ui file directly made by QDesigner
            uiFile = QFile(ui_file)
            uiFile.open(QFile.ReadOnly)                     # read in UI for the form
            loader = QUiLoader()
            self.window = loader.load(uiFile)
            uiFile.close() 
        else: #deployment - use .py version of ui file, with slightly different setup
            self.ui = Ui_MainWindow3()
            self.ui.setupUi(self)
        self.getParts()                                     # identify form objects
        self.convs = Converters()                       # load converters for main conversion categories
        self.yc = YearConverters()                      # load converters for japanese years, zodiac years
        self.mess = Mess()                              # instructions and messages in local language
        self.connectParts()                             # connect buttons to operations
        self.validFloat = QDoubleValidator()
        self.validYear = QIntValidator()
        self.validYear.setRange(1,9999)                 # used for years       
        self.btnConvert.hide()
        self.widgetSetup("start")                       # initial conditions for form
        if devMode == "development": self.window.show()
        else: self.show()

    def widgetSetup(self, themode):     # based on which main button is pressed
        self.themode = themode          # this is set when a main button is pressed, or on initial load
        self.emptyConvLayout()          # get rid of old radio buttons if they exist, hide input/output, etc.
        thetext, thestyle = makeHeader1(themode, self.uiFileName)       # make heading for convType = themode
        self.header1.setStyleSheet(thestyle)                            # can have different background colors
        self.header1.setText(thetext)
        self.header1.show()
        self.hideBigInstructions()
        if themode in self.convs.getValidConvTypes():                       # set up radio buttons for conversions
            oneConvTypeInfo = self.convs.convTypeToConvInfo(themode)        # get convCodes, displays for this convType
            for ix, (convCode, convDisplay) in enumerate(oneConvTypeInfo):  # iterate through enumerated list of tuples
                self.oneRadio = QRadioButton("{}".format(convDisplay))      # text for button 
                self.oneRadio.setObjectName("object_{}".format(convCode))   # to be used later by sender()
                self.oneRadio.setStyleSheet(makeStyleSheet("radiobutton", self.uiFileName))  
                self.layoutConv.addWidget(self.oneRadio)
                self.oneRadio.clicked.connect(self.convSetup)               # convSetup will call sender() to find convCode
                if ix==0: self.oneRadio.setFocus()                          # set focus on first button in list
        if themode=="fromjpyear":                                           # set up radio buttons for modern eras
            self.fromjpyearmode = "modern"                                  # start with modern eras only
            self.showJpEras()
        if themode=="fromjpyearhistoric":                                   # set up radio buttons for all eras
            self.fromjpyearmode = "all"                                     # start with modern eras only
            self.showJpEras()
        if themode=="tojpyear":                                             # no choices, go straight to input box
            self.showInstructions(self.mess.getToJpYear(self.yc.getMinYear()), "")
            self.input1.setText(str(self.yc.getNowYear()))                  # start with current year
            self.setUpValidator()            
            self.convertUnits()
        if themode=="zodiac":                                               # no choices, go straight to input box
            self.showInstructions(self.mess.getEnterYearZodiac(), "")
            self.input1.setText(str(self.yc.getNowYear()))                  # start with current year            
            self.setUpValidator()            
            self.convertUnits()
        if themode=="start": 
            self.btnFromMetric.setFocus()  
            self.showBigInstructions(self.mess.getStartMsg2())

    def showBigInstructions(self, themsg):
        self.instructions2.setText(themsg)
        self.scrollArea.hide()
        self.instructions2.show()

    def hideBigInstructions(self):
        self.scrollArea.show()
        self.instructions2.hide()

    def showJpEras(self):                                                   # display radio buttons for Japanese eras
        jpEraList = self.yc.getEraNamesPlusCodes(self.fromjpyearmode)       # modern or all
        for ix, (eraText, eraCode) in enumerate(jpEraList):
            self.oneRadio = QRadioButton("{}".format(eraText))              # text for button
            self.oneRadio.setObjectName("object_{}".format(eraCode))        # to be used later by sender()
            self.oneRadio.setStyleSheet(makeStyleSheet("radiobutton",self.uiFileName))  
            self.layoutConv.addWidget(self.oneRadio)
            self.oneRadio.clicked.connect(self.eraSetup)                    # eraSetup will call sender() to find eraCode
            if ix==0: self.oneRadio.setFocus()                              # set focus on first button
        if self.fromjpyearmode == "modern":
            self.oneRadio = QRadioButton("{}".format("Show more eras"))     # now add option for more eras
            self.oneRadio.setObjectName("object_{}".format("all"))          # to be used later by sender()
        else:
            self.oneRadio = QRadioButton("{}".format("Show fewer eras"))    # now add option to return to modern eras
            self.oneRadio.setObjectName("object_{}".format("modern"))       # to be used later by sender()
        self.oneRadio.setStyleSheet(makeStyleSheet("radiobutton",self.uiFileName))  
        self.layoutConv.addWidget(self.oneRadio)
        self.oneRadio.clicked.connect(self.eraSetup)                        # eraSetup will call sender() to find eraCode

    def eraSetup(self):                             # this is called when radio button is chosen
        theEra = self.getCodeFromSenderName()       # era or mode is determined by object name of sending radio button
        if theEra in ["all", "modern"]:             # switch between modern and all
            self.fromjpyearmode = theEra            # set the mode here
            self.emptyConvLayout()                  # clear former list
            if theEra=="all": self.widgetSetup("fromjpyearhistoric")
            else: self.widgetSetup("fromjpyear")
        else:                                       # theEra will be eraCode for chosen era
            self.chosenEra = theEra                 # set this property
            if self.yc.getNowEra() == theEra: theHint = "(1- )"                 # no final year if it's the current era
            else: theHint = "(1-{})".format(self.yc.getNumYears(theEra))        # final year in that era
            self.showInstructions(self.mess.getFromJpYear(self.yc.getENameUnparsed(theEra)), theHint)
            self.output2.hide()
            self.setUpValidator()

    def setUpValidator(self):
        if self.themode in self.convs.getValidConvTypes():              # measures
            if self.convs.isTempConv(self.theConvCode): self.validFloat.setBottom(-999999)    # temperatures can be negative
            else: self.validFloat.setBottom(0.0)                        # other measures can't be negative
            self.input1.setValidator(self.validFloat)  
        if self.themode in ["fromjpyear","fromjpyearhistoric", "tojpyear", "zodiac"]:
            self.input1.setValidator(self.validYear)        # range already set to 1-9999

    def convSetup(self):                                    # set up based on which radio button was set
        self.theConvCode = self.getCodeFromSenderName()     # get the code based on the sending button, and set it
        self.showInstructions(self.mess.getEnterAmt())
        self.setUpValidator()
        self.input1.setText("1")                            # show units=1 to start
        self.convertUnits()

    def getCodeFromSenderName(self):                        # based on objectName of sender button
        sending_button = self.sender()
        return str(sending_button.objectName()).replace("object_", "")

    def convertUnits(self):                                 # main conversion routine
        pstart = self.mess.getPstart()                      # get paragraph HTML from Message object
        pstopstart = self.mess.getPstopstart()
        pstop = self.mess.getPstop()
        jcol = self.mess.getJColor()                        # special color for Japanese text
        if len(self.input1.text())<1:                       # test for blank input
            self.output2.setText(self.mess.getBlankConvertMsg())      # show error message
            self.output2.show()
            return
        if self.themode in self.convs.getValidConvTypes():  # standard conversions: fromjpmeasure, tometric, etc   
            amt1Text = self.input1.text()
            amt1 = strToNum(amt1Text)         
            if self.convs.isTooCold(self.theConvCode, amt1): eqString = self.mess.getTooCold() #check for temp below abs zero
            else: eqString = self.convs.getEquation(self.theConvCode, amt1, " =" + pstopstart, jcol) 
            self.output2.setText(pstart + eqString + pstop)   # use paragraphs for better control of appearance
        elif self.themode=="tojpyear":                                  # int'l year to Japanese year
            try:
                iYear = int(self.input1.text())
                yearDisplay = self.mess.makeJYearDisplay(self.yc.iYearToJYear(iYear, jcol), iYear)
            except ValueError as errorMsg:
                yearDisplay = pstart + str(errorMsg) + pstop  # display the error message
            self.output2.setText(yearDisplay)
            #print (yearDisplay)
        elif self.themode in ["fromjpyear", "fromjpyearhistoric"]:      # Japanese year to int'l year
            jYear = int(self.input1.text())                             # validator at work, so this should be an integer
            try:                                                        # raise exception if not in range
                iYear = self.yc.jYearToIYear(self.chosenEra, jYear)
                yearDisplay = pstart +  "{} ({}) {}".format(self.yc.getENameUnparsed(self.chosenEra), \
                    self.yc.getJName(self.chosenEra, jcol), jYear) + \
                    pstopstart + self.mess.getIs() + " " + str(iYear) + pstop
            except ValueError as errorMsg:
                yearDisplay = pstart + str(errorMsg) + pstop  # display the error message
            self.output2.setText(yearDisplay)
        elif self.themode=="zodiac":                                    # international year to zodiac sign
            iYear = int(self.input1.text())
            # display is HTML with paragraph, line height, and Japanese characters in color (specified in Mess class)
            yearDisplay = pstart + str(iYear) + " " + self.mess.getIs() + ":" + pstopstart + \
                self.mess.getYearOfThe().capitalize() + " " + self.yc.getZodEName(iYear) + pstop
            self.output2.setText(yearDisplay)
            zBig = self.mess.makeZodiacBigDisplay(self.yc.getZodEName(iYear), 
                self.yc.getZodJName(iYear, jcol), self.yc.getZodJZName(iYear, jcol))
            self.showBigInstructions(zBig)
        self.output2.show()                                             # common to all conversion types

    def emptyConvLayout(self):                                  # clear the radio buttons in the converter/jpYear layout
        for i in reversed(range(self.layoutConv.count())):      # delete them in reverse order
            self.layoutConv.itemAt(i).widget().deleteLater()
        self.instructions1.hide()
        self.input1.setPlaceholderText("")                      # clear previous hints
        self.input1.hide()                                      # conversion not chosen yet, so hide this
        self.btnConvert.hide()                                  # conversion not chosen yet, so hide this
        self.output2.hide()                                     # conversion not chosen yet, so hide this

    def showInstructions(self, instructionsText, inputHint=""):     # position UI elements, set label, show input box
        self.instructions1.setText(instructionsText)
        self.instructions1.show()    
        self.input1.setText("")  
        self.input1.setPlaceholderText(inputHint)      
        self.input1.show()
        self.btnConvert.show()
        self.input1.setFocus()

    def convertQuickly(self):                           # testing
        if not self.input1.text(): amt = 0
        else: amt = float(self.input1.text()) * 2.0
        amtString = '{} kilograms'.format(amt)
        self.output2.setText(amtString)

    def getParts(self):                                                     # map form elements to object properties
        self.centralw = self.findWidget(QWidget, 'central_widget')
        self.input1 = self.findWidget(QLineEdit, 'input1')
        self.output2 = self.findWidget(QTextEdit, 'label_output2')
        self.header1 = self.findWidget(QLabel, 'label_header1')
        self.btnConvert = self.findWidget(QPushButton, 'button_convert')
        self.btnExit = self.findWidget(QPushButton, 'button_exit')
        self.btnFromMetric = self.findWidget(QPushButton, 'button_from_metric')
        self.btnToMetric = self.findWidget(QPushButton, 'button_to_metric')
        self.btnFromJpMeasure = self.findWidget(QPushButton, 'button_from_jpmeasure')
        self.btnToJpMeasure = self.findWidget(QPushButton, 'button_to_jpmeasure')
        self.btnFromJpYear = self.findWidget(QPushButton, 'button_from_jpyear')
        self.btnToJpYear = self.findWidget(QPushButton, 'button_to_jpyear')
        self.btnZodiac = self.findWidget(QPushButton, 'button_zodiac')
        self.scrollArea = self.findWidget(QScrollArea, 'conv_layout')     
        content_widget = QWidget()                          # now add the QVBoxLayout widget programmatically, for scrolling
        self.scrollArea.setWidget(content_widget)
        self.scrollArea.setWidgetResizable(True)
        self.layoutConv = QVBoxLayout(content_widget)           
        self.layoutConv.setAlignment(Qt.AlignTop)           # don't evenly space the radio buttons, but start at the top
        self.instructions1 = self.findWidget(QLabel, 'label_instructions1')
        self.instructions2 = self.findWidget(QLabel, 'label_instructions2')        
        self.menuExit = self.findWidget(QAction, 'action_exit')
        self.menuFromMetric = self.findWidget(QAction, 'action_from_metric')
        self.menuToMetric = self.findWidget(QAction, 'action_to_metric')
        self.menuFromJpMeasure = self.findWidget(QAction, 'action_from_jpmeasure')
        self.menuToJpMeasure = self.findWidget(QAction, 'action_to_jpmeasure')
        self.menuFromJpYear = self.findWidget(QAction, 'action_from_jpyear')
        self.menuFromJpYearHistoric = self.findWidget(QAction, 'action_from_jpyear_historic')
        self.menuToJpYear = self.findWidget(QAction, 'action_to_jpyear')
        self.menuZodiac = self.findWidget(QAction, 'action_zodiac')
        self.menubar = self.findWidget(QMenuBar, 'menubar')
        if self.uiFileName=="main3.ui": self.menubar.setStyleSheet(getMenuStyle("main3.ui"))    # in jpconvhelper.py

    def findWidget(self, widgetType, widgetName):
        if devMode == "development":  return self.window.findChild(widgetType, widgetName)
        else: return self.findChild(widgetType, widgetName)

    def connectParts(self):             # connect buttons and menu actions to operations
        self.input1.returnPressed.connect(self.convertUnits)
        self.btnConvert.clicked.connect(self.convertUnits)
        self.btnExit.clicked.connect(self.exitHandler)
        self.menuExit.triggered.connect(self.exitHandler)
        self.btnFromMetric.clicked.connect(lambda: self.widgetSetup("frommetric"))
        self.menuFromMetric.triggered.connect(lambda: self.widgetSetup("frommetric"))
        self.btnToMetric.clicked.connect(lambda: self.widgetSetup("tometric"))
        self.menuToMetric.triggered.connect(lambda: self.widgetSetup("tometric"))
        self.btnFromJpMeasure.clicked.connect(lambda: self.widgetSetup("fromjpmeasure"))
        self.menuFromJpMeasure.triggered.connect(lambda: self.widgetSetup("fromjpmeasure"))
        self.btnToJpMeasure.clicked.connect(lambda: self.widgetSetup("tojpmeasure"))
        self.menuToJpMeasure.triggered.connect(lambda: self.widgetSetup("tojpmeasure"))
        self.btnFromJpYear.clicked.connect(lambda: self.widgetSetup("fromjpyear"))
        self.menuFromJpYear.triggered.connect(lambda: self.widgetSetup("fromjpyear"))
        self.menuFromJpYearHistoric.triggered.connect(lambda: self.widgetSetup("fromjpyearhistoric"))
        self.btnToJpYear.clicked.connect(lambda: self.widgetSetup("tojpyear"))
        self.menuToJpYear.triggered.connect(lambda: self.widgetSetup("tojpyear"))
        self.btnZodiac.clicked.connect(lambda: self.widgetSetup("zodiac"))
        self.menuZodiac.triggered.connect(lambda: self.widgetSetup("zodiac"))

    def exitHandler(self):
        app.exit()
 
if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)        # suppresses error message on laptop python console
    app = QApplication(sys.argv)
    #form = Form(theUIFileName)
    window = MainWindow(theUIFileName, devMode)
    sys.exit(app.exec_())
