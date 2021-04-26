#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from os import system
import scribus
import os



def processInterfaceFile():
    print ("Hallo")

def openDocument():
    print("Hallo")

def createNewDocument():
    return scribus.newDoc((148, 210), (10, 10, 10, 10), PORTRAIT,
                         1, UNIT_MILLIMETERS, NOFACINGPAGES, FIRSTPAGELEFT)
    
def processFile():
   

def frontPage(LogoPath, ChurchPath, ChurchImage, Citation, CitationLocation):
    #scribus.setText('Gemeindebrief   DIGITAL Buxtehude',"Oben")

    #Line upper left corner
    l_line = scribus.createLine(10,10,10,33,"l_Line")
    scribus.setLineWidth(0.75, l_line)
    scribus.setLineColor("NAK-blau 100%", l_line)
    scribus.setLineShade("NAK-blau 100%", l_line)

    #Headline
    t_headline = scribus.createText(10,22,128,20,"t_Headline")
    scribus.setText("Gemeindebrief", t_headline)
    scribus.selectText(1, 100, t_headline)
    scribus.setCharacterStyle(
        "Erste Seite - Gemeindebrief - gross", t_headline)
    scribus.deselectAll()
    # Digital - Text
    t_digitalText = scribus.createText(107,27,30,7, "t_Digital")
    scribus.selectText(1, 100, t_digitalText)
    scribus.setCharacterStyle(
        "Erste Seite - Gemeindebrief - gross", t_digitalText)
    scribus.deselectAll()
    # Congregation - Text
    t_congregationText = scribus.createText(10,35.250, 70, 6, "t_Congregation")
    scribus.selectText(1, 100, t_congregationText)
    scribus.setCharacterStyle(
        "Erste Seite - Gemeindebrief - klein", t_congregationText)
    scribus.deselectAll()

    # Month Year
    t_monthYear = scribus.createText(56, 46.500, 82, 10, "t_MonthYear")
    scribus.selectText(1, 100, t_monthYear)
    scribus.setCharacterStyle(
        "Erste Seite - Gemeindebrief - Monat", t_monthYear)
    scribus.deselectAll()

    # Logo charitable
    i_charitable = scribus.createImage(10, 46, 35.5, 9, "i_NAC_charitable")
    scribus.loadImage(LogoPath + "Logo_NAK_karitativ_HQ.tiff", i_charitable)
    scribus.setImageScale(0.0613, 0.0613, i_charitable)
    
    # Church image
    i_churchImage = scribus.createImage(10,57,128,100,"i_Church")
    scribus.loadImage(ChurchPath + ChurchImage, i_churchImage)
    scribus.setImageScale(1, 1, i_churchImage)
    scribus.setImageOffset(-18.244, -0.342, i_churchImage)
    
    # Citation
    t_citation = scribus.createText(42.500, 162.500,95.500,4.500, "t_Citation")
    # OverflowCheck
    scribus.setText(Citation, t_citation)
    scribus.selectText(1, 100, t_citation)
    scribus.setCharacterStyle("Erste Seite - Bibelzitat - Text", t_citation)
    scribus.deselectAll()
    # Citation Location
    t_citationLocation = scribus.createText(42.500, 170, 95.500, 3, "t_CitationLocation")
    scribus.setText(CitationLocation, t_citationLocation)
    scribus.selectText(1, 100, t_citationLocation)
    scribus.setCharacterStyle(
        "Erste Seite - Bibelzitat - Ort", t_citationLocation)
    scribus.deselectAll()

    # NAC
    t_nac = scribus.createText(52.500,195,66,5,"t_NAC")
    scribus.setText("Neuapostolische Kirche", t_nac)
    scribus.selectText(1, 100, t_nac)
    scribus.setCharacterStyle("Erste Seite - NAK", t_nac)
    scribus.deselectAll()
    # North and east germany
    t_northEastGermany = scribus.createText(52.500, 195, 66, 5, "t_NorthEastGermany")
    scribus.setText("Nord- und Ostdeutschland", t_northEastGermany)
    scribus.selectText(1, 100, t_northEastGermany)
    scribus.setCharacterStyle(
        "Erste Seite - Nord- und Ostdeutschland", t_northEastGermany)
    scribus.deselectAll()

    # NAC Logo
    i_nacLogo = scribus.createImage(122, 184, 16, 16,"i_Logo")
    scribus.loadImage("L:\\GB\\Bilder\\Logos\\Logo_NAK_HQ.tif", i_nacLogo)
    scribus.setImageScale(0.0384, 0.0384, i_nacLogo)

    scribus.saveDocAs()

def colors():
    scribus.defineColorCMYKFloat("NAK-blau 100%", 68.0, 34.0, 0.0, 0.0)
    scribus.defineColorRGB("Tabelle-Hintergrund", 215, 225, 243)
    scribus.deleteColor("Blue")
    scribus.deleteColor("Cool Black")
    scribus.deleteColor("Cyan")
    scribus.deleteColor("Green")
    scribus.deleteColor("Magenta")
    scribus.deleteColor("Red")
    scribus.deleteColor("Registration")
    scribus.deleteColor("Rich Black")
    scribus.deleteColor("Warm Black")
    scribus.deleteColor("Yellow")

def createCharStyle(Name, Font, FontSize, Features="", BaseLineOffset = 0, Tracking = 0):
    scribus.createCharStyle(
        Name,
        font=Font,
        fontsize=FontSize,
        features=Features,
        fillcolor="",
        fillshade=1.0,
        strokecolor="Black",
        strokeshade=1.0,
        baselineoffset=BaseLineOffset,
        shadowxoffset=0,
        shadowyoffset=0,
        outlinewidth=0,
        underlineoffset=0,
        underlinewidth=0,
        strikethruoffset=0,
        strikethruwidth=0,
        scaleh=1,
        scalev=1,
        tracking=Tracking
    )


def createParagraphStyle(Name, LineSpacingMode, Alignment, LeftMargin, RightMargin, GapBefore, GapAfter, FirstIndent, CharStyle, LineSpacing = 0, HasDropCap = 0, DropCapLines = 0 ):
    
    if (LineSpacingMode != 0 and HasDropCap != 0 ):
        scribus.createParagraphStyle(
            Name,
            linespacingmode=LineSpacingMode,
            alignment=Alignment,
            leftmargin=LeftMargin,
            rightmargin=RightMargin,
            gapbefore=GapBefore,
            gapafter=GapAfter,
            firstindent=FirstIndent,
            hasdropcap=HasDropCap,
            dropcaplines=DropCapLines,
            charstyle=CharStyle)
    if (LineSpacingMode == 0 and HasDropCap != 0):
        scribus.createParagraphStyle(
            Name,
            linespacingmode=LineSpacingMode,
            linespacing=LineSpacing,
            alignment=Alignment,
            leftmargin=LeftMargin,
            rightmargin=RightMargin,
            gapbefore=GapBefore,
            gapafter=GapAfter,
            firstindent=FirstIndent,
            hasdropcap=HasDropCap,
            dropcaplines=DropCapLines,
            charstyle=CharStyle)
    if (LineSpacingMode != 0 and HasDropCap == 0):
        scribus.createParagraphStyle(
            Name,
            linespacingmode=LineSpacingMode,
            alignment=Alignment,
            leftmargin=LeftMargin,
            rightmargin=RightMargin,
            gapbefore=GapBefore,
            gapafter=GapAfter,
            firstindent=FirstIndent,
            hasdropcap=HasDropCap,
            charstyle=CharStyle)
    if (LineSpacingMode == 0 and HasDropCap == 0):
        scribus.createParagraphStyle(
            Name,
            linespacingmode=LineSpacingMode,
            linespacing=LineSpacing,
            alignment=Alignment,
            leftmargin=LeftMargin,
            rightmargin=RightMargin,
            gapbefore=GapBefore,
            gapafter=GapAfter,
            firstindent=FirstIndent,
            hasdropcap=HasDropCap,
            charstyle=CharStyle)


def processInterfaceFile(InterfaceFile):
     with open(InterfaceFile) as lfiInterfaceFile:
        larrData = json.load(lfiInterfaceFile)

    # Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
    print(larrData)

    for larrAction in larrData:
        print(lstrFile)
        scribus.openDoc(lstrFile)
        lstrFilename = os.path.splitext(scribus.getDocName())[0]
        pdf = scribus.PDFfile()
        pdf.compress = True
        pdf.compressmtd = 1
        pdf.quality = 2
        pdf.file = lstrFilename+".pdf"
        pdf.save()
        scribus.closeDoc()

def main(argv):
    processInterfaceFile(argv[1])

if __name__ == '__main__':
    main(system.argv)




