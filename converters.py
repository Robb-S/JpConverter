from converter import *
class Converters(object):
    ''' collection of converter objects, and methods for retrieval, indexing and conversion '''
    def __init__(self):
        self.convDict = {}                  # key = convCode, value = converter object
        self.clearConvTypeDicts()           # set these to empty dicts
        self.setValidConvTypes(["frommetric", "tometric", "fromjpmeasure", "tojpmeasure"])  
        self.loadBaseConverters()           

    def clearConvTypeDicts(self):
        self.convTypeToConvCodesDict = {}    # key = convType, value = list of convCodes
        self.convTypeToConvInfoDict = {}    # key = convType, value = list of (convCode, convDisplay) tuples

    def setValidConvTypes(self, theList):   # to check against when loading converter tuples (to avoid typos)
        self.validConvTypes = theList       # separate method so the list can be updated if necessary

    def getValidConvTypes(self):   
        return self.validConvTypes

    def loadBaseConverters(self):           # this can alternatively be done from external file
        self.tempConvCodes = ["c2f", "f2c"] # these can use negative numbers
        convTuples = [
			("c2f", "°C to °F", "°C", "", "°F", 0.0, 1, "frommetric"),
			("km2mi", "kilometers to miles", "kilometers", "kilometer", "miles", 0.621371, 2, "frommetric"),
			("m2ft", "meters to feet", "meters", "meter", "feet", 3.28084, 3, "frommetric"),
			("cm2in","centimeters to inches", "centimeters", "centimeter", "inches", 0.393701, 3, "frommetric"),
			("sqm2sqft","square meters to square feet","square meters","square meter", "square feet", 10.7640, 3, "frommetric"),
			("kg2lb","kilograms to pounds", "kilograms","kilogram", "pounds", 2.2046, 3, "frommetric"),
			("ml2oz","milliliters to fluid ounces", "milliliters", "milliliter", "fluid oz", 0.033814, 3, "frommetric"),
			("f2c","°F to °C", "°F", "","°C", 0.0, 1, "tometric"),
			("mi2km","miles to kilometers","miles", "mile", "km", 1.60934, 2, "tometric"),
			("ft2m","feet to meters","feet","foot", "meters", 0.3048, 3, "tometric"),
			("in2cm","inches to centimeters", "inches", "inch", "cm", 2.54, 3, "tometric"),
			("sqft2sqm","square feet to square meters","square feet", "square foot", "sq meters", 0.0929, 3, "tometric"),
			("lb2kg","pounds to kilograms", "pounds","pound", "kilograms", 0.45359, 3, "tometric"),
			("oz2ml","fluid ounces to milliliters","fluid oz","","milliliters", 29.5735, 3, "tometric"),
			("acre2tsubo", "acres to tsubo", "acres", "acre","tsubo", 1224.18, 2, "tojpmeasure", "坪"),
			("sqm2tsubo", "square meters to tsubo", "square meters", "square meter","tsubo", 0.3025, 2, "tojpmeasure", "坪"),
			("sqft2tsubo", "square feet to tsubo", "square feet", "square foot", "tsubo",  0.0281, 3, "tojpmeasure", "坪"),
			("sqm2jo", "square meters to jo", "square meters", "square meter", "jo", 0.605, 2, "tojpmeasure", "畳"),
			("sqft2jo", "square feet to jo", "square feet", "square foot", "jo",  0.0562, 3, "tojpmeasure", "畳"),
			("tsubo2acre", "tsubo to acres", "tsubo", "", "acres", 0.0008169, 5, "fromjpmeasure", "坪"),
			("tsubo2sqm", "tsubo to square meters", "tsubo", "", "square meters", 3.3058, 2, "fromjpmeasure", "坪"),
			("tsubo2sqft", "tsubo to square feet", "tsubo", "", "square feet",  35.584, 2, "fromjpmeasure", "坪"),
			("jo2sqm", "jo to square meters", "jo", "", "square meters", 1.653, 2, "fromjpmeasure", "畳"),
			("jo2sqft", "jo to square feet", "jo", "", "square feet.", 17.79, 2, "fromjpmeasure", "畳"),	
			("go2ml", "go to ml (sake)", "go", "", "ml", 180.4, 2, "fromjpmeasure", "合"),
			("ml2go", "ml to go (sake)", "milliliters", "milliliter", "go", 0.005544, 4, "tojpmeasure", "合"),
			("go2floz", "go to fluid oz (sake)", "go", "", "fluid oz.", 6.1, 2, "fromjpmeasure", "合"),	
			("floz2go", "fluid oz to go (sake)", "fluid oz", "", "go", 0.1639, 3, "tojpmeasure", "合"),	
            ("sh2ml", "shaku to ml (sake)", "shaku", "", "ml", 18.04, 1, "fromjpmeasure", "勺"),
			("ml2sh", "ml to shaku (sake)", "milliliters", "milliliter", "shaku", 0.05544, 3, "tojpmeasure", "勺"),
            ("sh2floz", "shaku to fluid oz (sake)", "shaku", "", "fluid oz", 0.61, 3, "fromjpmeasure", "勺"),
			("floz2sh", "fluid oz to shaku (sake)", "fluid oz", "fluid oz", "shaku", 1.639, 3, "tojpmeasure", "勺"),
        ]
        for convTuple in convTuples:
            self.loadOneConverter(convTuple)                        # separate method so it can be used independently 

    def loadOneConverter(self, convTuple):  
        if convTuple[7] in self.validConvTypes:                     # make sure convType is valid and not misspelled
            self.convDict[convTuple[0]] = Converter(*convTuple)     # use convCode as index, overwrite if it already exists
            self.clearConvTypeDicts()                               # will recalculate these when necessary
        else: raise ValueError("invalid converter type: " + convTuple[7])
            
    def isTempConv(self, convCode):
        return convCode in self.tempConvCodes

    def makeConvTypeToConvDicts(self):                              # make both dictionaries at the same time
        self.clearConvTypeDicts()                                   # clear them first just to be safe
        for oneConverter in self.convDict.values():
            theCode = oneConverter.getConvCode()
            theType = oneConverter.getConvType()
            theDisplay = oneConverter.getConvDisplay()           
            theTuple = (theCode, theDisplay)
            try: self.convTypeToConvCodesDict[theType].append(theCode)       # add to dictionary entry if it exists already
            except: self.convTypeToConvCodesDict[theType] = [theCode]        # otherwise create new dictionary entry (list)
            try: self.convTypeToConvInfoDict[theType].append(theTuple)
            except: self.convTypeToConvInfoDict[theType] = [theTuple]
    
    def convTypeToConvCodes(self, convType):     # returns list of convCodes for a particular convType (e.g. "tometric")
        if len(self.convTypeToConvCodesDict)==0: self.makeConvTypeToConvDicts()
        try: convCodeList = self.convTypeToConvCodesDict[convType]
        except: convCodeList = []
        return convCodeList

    def convTypeToConvInfo(self, convType):     # returns list of (convCode, convDisplay) tuples for a convType
        if len(self.convTypeToConvInfoDict)==0: self.makeConvTypeToConvDicts()  # makes both dictionaries
        try: convInfoList = self.convTypeToConvInfoDict[convType]
        except: convInfoList = []
        return convInfoList
    
    def numberOfConverters(self):
        return len(self.convDict)

    def maxConvertersPerType(self):             # largest number of converters for any type
        ''' fetches lists of converters for each convType, returns size of biggest list '''
        return max([len(self.convTypeToConvCodes(convType)) for convType in self.validConvTypes])

    ''' straightforward conversions from Converter objects next '''
    def getAmt2StringUnits(self, convCode, amt1):
        try: return self.convDict[convCode].getAmt2StringUnits(amt1)
        except: return ""
    def getAmt2String(self, convCode, amt1):
        try: return self.convDict[convCode].getAmt2String(amt1)
        except: return ""
    def getAmt2Float(self, convCode, amt1):
        try: return self.convDict[convCode].getAmt2Float(amt1)
        except: return ""   # instead of number
    def getAmt1StringUnits(self, convCode, amt1):
        try: return self.convDict[convCode].getAmt1StringUnits(amt1)
        except: return ""
    def getEquation(self, convCode, amt1, eqstring=" = ", thecolor = ""):
        try: return self.convDict[convCode].getEquation(amt1, eqstring, thecolor)
        except: return ""
    def getUnitKanji(self, convCode):
        try: return self.convDict[convCode].getUnitKanji()
        except: return ""
