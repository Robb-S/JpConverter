class Mess(object):
    ''' container for label text and other messages in local language  '''
    def __init__(self):
        paraTemp =  '<p style="line-height:1.3;">{}</p>'       # template for text paragraphs with adequate line height
        self.language = "E"
        self.kanjiColor = "#ffea00"
        self.enterAmt = "Enter amount to convert"
        self.enterYearZodiac = "Enter year (1-9999)"
        self.fromJpYearTemp = "Enter year from {} era"      # era name will be inserted later
        self.toJpYearTemp = "Enter int'l year ({}-present)"
        self.couldNotParseTemp = "Could not parse date: {}"
        self.pstart = '<p style="line-height:1.2; margin:0; padding:0;">'
        self.pstopstart = '</p><p style="line-height:1.2; margin:0; padding:0;">'
        self.pstop = '</p>'
        self.blankConvertMsg = "Please enter a value"
        startMsg2Text = "Press one of the buttons on the right to see the available conversion units."
        self.startMsg2 = paraTemp.format(startMsg2Text)
        self.theWordIs = "is"

    def getLanguage(self): return self.language
    def getEnterAmt(self): return self.enterAmt
    def getEnterYearZodiac(self): return self.enterYearZodiac
    def getFromJpYear(self, param1): return self.fromJpYearTemp.format(param1)
    def getToJpYear(self, param1): return self.toJpYearTemp.format(param1)
    def getCouldNotParse(self, param1): return self.countNotParseTemp.format(param1)
    def getBlankConvertMsg(self): return self.blankConvertMsg
    def getPstop(self): return self.pstop
    def getPstopstart(self): return self.pstopstart
    def getPstart(self): return self.pstart
    def getStartMsg2(self): return self.startMsg2
    def getIs(self): return self.theWordIs

    def makeJYearDisplay(self, listOfJYearTuples, iYear):   # this may be have multiple Japanese era years
        if len(listOfJYearTuples) == 0: return self.mess.getCouldNotParse(str(iYear))  # does this ever happen?  
        ansDisp = str(iYear) + " is: "
        lineNum = 1
        for eName, jName, eraYear in listOfJYearTuples:
            if lineNum>1: ansDisp += self.pstopstart + "and "           # for two-line answers, insert a paragraph break
            ansDisp += eName + " (" + jName + ") " + str(eraYear)       # e.g. 1989 is Showa 64 and Heisei 1 
            lineNum +=1 
        return self.pstart + ansDisp + self.pstop               # need to use paragraphs for proper line height control    

