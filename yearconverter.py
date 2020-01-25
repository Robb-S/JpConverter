import datetime
from html.parser import HTMLParser
class YearConverters(object):
    ''' container for era objects, zodiac objects // prop: yDict (eraCode: OneEra), eraCodeAllList (alpha sorted), 
        eraCodeModernList (reverse date sorted), nowEraCode (based on ending year of 0), modernEraStart (1868), 
        jYearTuples (list of tuples) for loading and sorting, 
        zFromYearDict (yearMod: ZodiacYear), zToYearsDict (zodCode: list of years), nowYear  '''
    def __init__(self):
        self.nowYear = datetime.datetime.now().year
        # self.maxYear = self.nowYear + 99                # arbitrary maximim for years to check 
        self.minYear = 100000                               # set this later
        self.modernEraStart = 1868      # beginning of Meiji era
        self.htmlparse = HTMLParser()
        self.loadJYears()               # load data and prepare indexes
        self.zToYearsDict = {}          # this will be set up only after it's requested
        self.loadZYears()

    def unparse(self, parsed): return self.htmlparse.unescape(parsed)

    def loadJYears(self):
        self.yDict = {}
        self.jYearTuples = [         # utf-8 and html encoding
            ("reiwa", "Reiwa", "令和", 2019, 0),
            ("heisei", "Heisei", "平成", 1989, 2019),	
            ("showa", "Sh&#333;wa", "昭和", 1926, 1989),
            ("taisho", "Taish&#333;", "大正", 1912, 1926),
            ("meiji", "Meiji", "明治", 1868, 1912),
            ("keio", "Kei&#333;", "慶応", 1865, 1868),
            ("genji", "Genji", "元治", 1864, 1865),
            ("bunkyu", "Bunky&#363;", "文久", 1861, 1864),
            ("manen", "Man'en", "万延", 1860, 1861),
            ("ansei", "Ansei", "安政", 1854, 1860),
            ("kaei", "Kaei", "嘉永", 1848, 1854),
            ("koka", "K&#333;ka", "弘化", 1844, 1848),
            ("tenpo", "Tenp&#333;", "天保", 1830, 1844),
            ("bunsei", "Bunsei", "文政", 1818, 1830),
            ("bunka", "Bunka", "文化", 1804, 1818),
            ("kyowa", "Ky&#333;wa", "享和", 1801, 1804),
            ("kansei", "Kansei", "寛政", 1789, 1801),
            ("tenmei", "Tenmei", "天明", 1781, 1789),
            ("anei", "An'ei", "安永", 1772, 1781),
            ("meiwa", "Meiwa", "明和", 1764, 1772),
            ("horeki", "H&#333;reki", "宝暦", 1751, 1764),
            ("kanen", "Kan'en", "寛延", 1748, 1751),
            ("enkyo2", "Enky&#333;", "延享", 1744, 1748),
            ("kanpo", "Kanp&#333;", "寛保", 1741, 1744),
            ("genbun", "Genbun", "元文", 1736, 1741),
            ("kyoho", "Ky&#333;h&#333;", "享保", 1716, 1736),
            ("shotoku", "Sh&#333;toku", "正徳", 1711, 1716),
            ("hoei", "H&#333;ei", "宝永", 1704, 1711),
            ("genroku", "Genroku", "延享", 1688, 1704),
        ]                   # (source: http://www.meijigakuin.ac.jp/~watson/ref/nengo-utf8.html and Nelson)
        self.nowEraCode = ""
        self.minYear = min([onetuple[3] for onetuple in self.jYearTuples])
        tempEraCodeAllList = []
        tempEraCodeModernList = []
        for jYearTuple in self.jYearTuples:
            thisEraObject = OneEra(*jYearTuple)         # tuple items are parameters to instantiate OneEra object
            thisEraCode = thisEraObject.getEraCode()    
            self.yDict[thisEraCode] = thisEraObject     # use eraCode as index, overwrite if it already exists
            if thisEraObject.getEndYear()==0: self.nowEraCode = thisEraCode   # set the current era
            tempEraCodeAllList.append(thisEraCode)
            if thisEraObject.getStartYear() >= self.modernEraStart: 
                tempEraCodeModernList.append((thisEraCode, thisEraObject.getStartYear()))
        self.eraCodeAllListSorted = sorted(tempEraCodeAllList)        # alpha sort for this list of all eras
        # next, modern list is sorted in reverse order of date
        self.eraCodeModernListSorted = [a[0] for a in sorted(tempEraCodeModernList, key=lambda x: x[1], reverse=True)]
        self.maxYear = self.yDict[self.nowEraCode].getStartYear() + 98        # year 99 fo current era is maxYear

    def makeColorSpan(self, thecolor):
        js1c = js2c = ""
        if thecolor:
            js1c = '<span style="color:{}">'.format(thecolor)
            js2c = '</span>'
        return js1c, js2c

    def getEraNamesPlusCodes(self, eraType, thecolor=""):
        ''' returns list of tuples for display in radio buttons or dropdown list.  eraType = "modern" or "all" '''
        theEras = []
        if eraType=="modern": listToUse = self.eraCodeModernListSorted
        else: listToUse = self.eraCodeAllListSorted
        for eraCode in listToUse:
            oneTuple = (self.getENameUnparsed(eraCode)+ " " + self.getJName(eraCode, thecolor), eraCode)
            theEras.append(oneTuple)
        return theEras

    def iYearToJYear(self, iYear, thecolor=""):      # returns list with 0, 1, or 2 tuples of (eName, jName, eraYear)
        js1c, js2c = self.makeColorSpan(thecolor)    # if thecolor is specified, japanese characters will appear in that color
        jYears1 = []            # fill with one or two tuples of (startYear, eraCode) for matching era(s), then sort it
        jYears2 = []            # fill with one or two tuples of (eName, jName, eraYear)
        if not iYear in range(self.minYear, self.maxYear+1): 
            raise ValueError("Please enter a year between {} and {}".format(self.minYear, self.maxYear))   
            #return jYears2   # return blank if out of range
        for oneEra in self.yDict.values():
            if (oneEra.isIYearInEra(iYear)): 
                jYears1.append( (oneEra.getStartYear(), oneEra.getEraCode() ) )   # startYear is sort key if there are two
        jYears1.sort(key=lambda x: x[0])
        for startYear, eraCode in jYears1:
            jYears2.append( ( self.yDict[eraCode].getENameUnparsed(), js1c + self.yDict[eraCode].getJName() + js2c, 
                self.yDict[eraCode].iYearToEraYear(iYear)) )
        return jYears2          

    def jYearToIYear(self, eraCode, jYear):     # return international year, or 0 if out of range
        try:                                                                # raise exception if era not found
            if eraCode == self.nowEraCode: maxJYear = 99
            else: maxJYear = self.yDict[eraCode].getNumYears()
        except: raise ValueError("Era {} not found".format(eraCode))            
        if jYear in range(1, maxJYear+1): return self.yDict[eraCode].getStartYear() + jYear - 1  # test for out of range
        else: raise ValueError("Please enter a value between 1 and "+str(maxJYear))

    def getNowYear(self): return self.nowYear
    def getNowEra(self): return self.nowEraCode             # based on endYear == 0
    def getMinYear(self): return self.minYear
    def getMaxYear(self): return self.maxYear
    def getEName(self, eraCode): return self.yDict[eraCode].getEName()
    def getENameUnparsed(self, eraCode): return self.yDict[eraCode].getENameUnparsed()
    def getJName(self, eraCode, thecolor=""): 
        js1c, js2c = self.makeColorSpan(thecolor)     
        return js1c + self.yDict[eraCode].getJName() + js2c
    def getStartYear(self, eraCode): return self.yDict[eraCode].getStartYear()
    def getEndYear(self, eraCode): return self.yDict[eraCode].getEndYear()
    def getNumYears(self, eraCode): return self.yDict[eraCode].getNumYears()

    def loadZYears(self):
        self.zFromYearDict = {}
        zodTuples = [
            (0, "monkey", "猿", "申"),      # yearmod (mod 12), eName, jName (animal), jName (kanji for zodiac sign)
            (1, "rooster", "鳥", "酉"),
            (2, "dog", "犬", "戌"),
            (3, "boar", "猪", "亥"),
            (4, "rat", "鼠", "子"),
            (5, "ox", "牛", "丑"),
            (6, "tiger", "虎", "寅"),
            (7, "rabbit", "兎", "卯"),
            (8, "dragon", "龍", "辰"),
            (9, "snake", "蛇", "巳"),
            (10, "horse", "馬", "午"),
            (11, "sheep", "羊", "未"),
        ]
        for zodTuple in zodTuples:
            self.zFromYearDict[zodTuple[0]] = ZodiacYear(*zodTuple)   # use yearMod as index, overwrite if it already exists

    def getZodEName(self, theyear): return self.zFromYearDict[theyear%12].getEName()
    def getZodJName(self, theyear, thecolor=""): # returns span with Japanese characters in color, if specified by parameter
        js1c, js2c = self.makeColorSpan(thecolor)        
        return js1c + self.zFromYearDict[theyear%12].getJName() + js2c
    def getZodJZName(self, theyear, thecolor=""): # Japanese characters in color, if specified
        js1c, js2c = self.makeColorSpan(thecolor)        
        return js1c + self.zFromYearDict[theyear%12].getJZName() + js2c
    def getZodEJZNames(self, theyear, thecolor=""): # Japanese characters in color if it's specified
        js1c, js2c = self.makeColorSpan(thecolor)
        ans = "Year of the "+ self.zFromYearDict[theyear%12].getEName() + " " + \
            js1c + self.zFromYearDict[theyear%12].getJName() + js2c + \
            " (" + js1c + self.zFromYearDict[theyear%12].getJZName() + js2c + ")"
        return ans

    def makeZToYearDict(self, backYears, forwardYears):
        self.zToYearsDict = {}
        for oneYear in range(self.nowYear-backYears, self.nowYear+forwardYears+1):
            zodCode = self.zFromYearDict[oneYear%12].getEName()
            try: self.zToYearsDict[zodCode].append(oneYear)
            except: self.zToYearsDict[zodCode] = [oneYear]

    def getYearsFromZodiac(self, zodCode):                          # zodCode = eName
        if len(self.zToYearsDict)==0: self.makeZToYearDict(100, 3)  # from 100 year in the past, to 3 years in the future
        return self.zToYearsDict[zodCode]

class OneEra(object):
    ''' era object - eraCode (simple name), eName (name with macrons), jName (kanji), startYear, endYear, numYears '''
    def __init__(self, eraCode, eName, jName, startYear, endYear):
        self.eraCode = eraCode
        self.eName = eName
        self.jName = jName
        self.startYear = startYear
        self.endYear = endYear
        if (self.endYear == 0): self.numYears = 0
        else: self.numYears = self.endYear - self.startYear + 1
        
    def isIYearInEra(self, iYear):
        if (self.endYear ==0): return iYear>=self.startYear
        else: return (iYear>=self.startYear) and (iYear<=self.endYear)
    def iYearToEraYear(self, iYear):
        if self.isIYearInEra(iYear): return iYear-self.startYear+1
        else: return 0

    def getEraCode(self): return self.eraCode
    def getEName(self): return self.eName
    def getENameUnparsed(self):
        htmlparse = HTMLParser()
        return htmlparse.unescape(self.eName)
    def getJName(self): return self.jName
    def getStartYear(self): return self.startYear
    def getEndYear(self): return self.endYear
    def getNumYears(self): return self.numYears

class ZodiacYear(object):
    def __init__(self, yearMod, eName, jName, jZName):
        self.yearMod = yearMod
        self.eName = eName
        self.jName = jName
        self.jZName = jZName
    def getYearMod(self): return self.yearMod
    def getEName(self): return self.eName
    def getJName(self): return self.jName
    def getJZName(self): return self.jZName
