def makeHeader1(themode, theui="main2.ui"):
    ''' return text and stylesheet for header based on mode '''
    titles = {"frommetric": "Convert from metric", "fromjpyear": "Convert from Japanese year", 
        "fromjpyearhistoric": "Convert from Japanese year", 
        "fromjpmeasure": "Convert from Japanese measure", "zodiac": "Show Zodiac year", 
        "tometric": "Convert to Metric", "tojpyear": "Convert to Japanese year", 
        "tojpmeasure": "Convert to Japanese measure", "start": "Choose conversion type"}
    #print (theui)
    if theui in ["main2.ui", "main1.ui"]:
        if themode in ["frommetric", "fromjpyear", "fromjpyearhistoric", "fromjpmeasure", "zodiac"]: backgroundColor = "#1565c0"
        elif themode in ["start"]: backgroundColor = "#5e5e5e"
        else: backgroundColor = "#0288d1"
        thestyle = "padding: 0 4px 0 10px;color:#eeeeee;font-weight:bold;font-size:22px;"+\
            "background-color:{};".format(backgroundColor)
    else:
        if themode=="start": backgroundColor = "#222222"
        elif themode=="frommetric": backgroundColor = "#00600f"
        elif themode=="tometric": backgroundColor = "#087f23"
        elif themode=="fromjpmeasure": backgroundColor = "#00600f"
        elif themode=="tojpmeasure": backgroundColor = "#087f23"
        elif themode=="fromjpyear": backgroundColor = "#00600f"
        elif themode=="fromjpyearhistoric": backgroundColor = "#00600f"
        elif themode=="tojpyear": backgroundColor = "#087f23"
        elif themode=="zodiac": backgroundColor = "#00600f"
        # elif themode=="fromjpmeasure": backgroundColor = "#001970"
        # elif themode=="tojpmeasure": backgroundColor = "#26418f"
        # elif themode=="fromjpyear": backgroundColor = "#c43e00"
        # elif themode=="fromjpyearhistoric": backgroundColor = "#c43e00"
        # elif themode=="tojpyear": backgroundColor = "#c56000"
        # elif themode=="zodiac": backgroundColor = "#a00037"
        else: backgroundColor = "#3e3e3e"
        thestyle = "padding: 0 4px 0 10px;color:#eeeeee;font-weight:bold;font-size:21px;"+\
            "border-style: solid; border-color: #bbbbbb; border-width: 1px;"+\
            "background-color:{};".format(backgroundColor)
    thetext = titles[themode]
    return thetext, thestyle
    
def makeStyleSheet(thestylemode, theui="main2.ui"):
    thestyle = ""
    if thestylemode == "radiobutton": 
        if theui in ["main1.ui","main2.ui"]: thestyle = "font-size: 17px;padding: 0 0 6px 0;color: #000000;"
        else: thestyle = "font-size: 17px;padding: 0 0 6px 0;color:#ffffff;"
    return thestyle

def strToNum(numstr):
    try: amt = int(numstr)
    except: 
        try: amt = float(numstr)
        except: amt = 0
    return amt

def getMenuStyle(theui="main2.ui"):
    if theui=="main3.ui":
        a= """
                QMenuBar {
                    background-color: #ffffff;
                    color: #000000;
                }

                QMenuBar::item {
                    background-color: #ffffff;
                    color: #000000;
                }

                QMenuBar::item::selected {
                    background-color: #dddddd;
                }

                QMenu {
                    background-color: #ffffff;
                    color: #000000; 
                }

                QMenu::item::selected {
                    background-color: #dddddd;
                }
            """
        return a
    else: return ""

