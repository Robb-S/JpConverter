from jpconvhelper import makeColorSpan
class Converter(object):
    ''' one converter object contains conversion rate, labels, etc. to perform one type of conversion and report results
        methods: conversion result as float, string (to sig digits), string with units, full equation '''

    def __init__(self, convCode, convDisplay, unit1, unit1single, unit2, convFactor, sigDigits, convType, unitKanji=""):
        self.convCode = convCode                # e.g. "mi2km"
        self.convDisplay = convDisplay          # e.g. "miles to kilometers"
        self.unit1 = unit1                      # e.g. "miles"
        if len(unit1single)>0: self.unit1single = unit1single    # e.g. "mile" (if blank then same as unit1)
        else: self.unit1single = self.unit1    
        self.unit2 = unit2                      # e.g. "kilometers"
        self.convFactor = convFactor            # e.g. 1.60934
        self.sigDigits = sigDigits              # e.g. 2
        self.convType = convType                # e.g. "tometric" / "frommetric" / "tojpmeasure" / "fromjpmeasure"
        if self.convCode in ["f2c", "c2f"]: self.unitSpacer = ""        # space before unit name, none if degree sign        
        else: self.unitSpacer = " "
        self.unitKanji = unitKanji

    def getAmt2Float(self, amt1):               # return conversion result as floating point
        if self.convCode=="f2c": return (((amt1-32.0)*5.0)/9.0)
        elif self.convCode=="c2f": return (((amt1*9.0)/5.0)+32.0)
        else: return (amt1 * self.convFactor)

    def getAmt2String(self, amt1):              # return conversion result as string, displayed using significant digits
        amt2 = self.getAmt2Float(amt1)
        formatstr = "{" + ":.{}f".format(self.sigDigits) + "}"      # e.g. "{:.2f}" for two significant digits
        return formatstr.format(amt2)                               # e.g. "{:.2f}".format(1.77777) -> "1.78"

    def getAmt2StringUnits(self, amt1, thecolor=""):                             # conversion result + units
        jsc1, jsc2 = makeColorSpan(thecolor)
        if self.unitKanji and self.convType=="tojpmeasure":           # add in kanji after the unit name in English
            kpart = " (" + jsc1 + self.unitKanji + jsc2 + ")"
        else: kpart = ""
        amt2str = self.getAmt2String(amt1)
        return amt2str + self.unitSpacer + self.unit2 + kpart               # unitSpacer is either "" (for degree sign) or " "

    def getAmt1StringUnits(self, amt1, thecolor=""):         # amt1 plus units
        jsc1, jsc2 = makeColorSpan(thecolor)
        if self.unitKanji and self.convType=="fromjpmeasure":           # add in kanji after the unit name in English
            kpart = " (" + jsc1 + self.unitKanji + jsc2 + ")"
        else: kpart = ""
        if amt1==1: return str(amt1) + self.unitSpacer + self.unit1single + kpart  # not needed for amt2 since it's a float
        else: return str(amt1) + self.unitSpacer + self.unit1 + kpart

    def getEquation(self, amt1, eqstring=" = ", thecolor=""):  # full equation, with optional equal sign characters, color for Jp
        #print ("get equation")
        return self.getAmt1StringUnits(amt1, thecolor) + eqstring + self.getAmt2StringUnits(amt1, thecolor)

    ''' get properties next '''
    def getConvCode(self): return self.convCode
    def getConvDisplay(self): return self.convDisplay
    def getUnit1(self): return self.unit1
    def getUnit1Single(self): return self.unit1single
    def getUnit2(self): return self.unit2
    def getConvFactor(self): return self.convFactor
    def getSigDigits(self): return self.sigDigits
    def getConvType(self): return self.convType
    def getUnitKanji(self): return self.unitKanji


