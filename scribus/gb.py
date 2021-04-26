#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import sys
# from os import system

# import scribus
import os



def processInterfaceFile():
    print ("Hallo")

def openDocument():
    print("Hallo")

def createNewDocument():
   print("Erstelle ein neues Dokument und gebe es zurück")
   return ""

def frontPage(LogoPath, ChurchPath, ChurchImage, Citation, CitationLocation, Month, Year):
    print ("Erstelle eine neue Seite mit folgenden Werte: ")
    print ("Pfad der Logos: " + LogoPath)
    print ("Pfad der Kirchenbilder: " + ChurchPath)
    print ("Bild der Kirche: " + ChurchImage)
    print ("Zitattext: " + Citation)
    print ("Herkunft des Zitats: " + CitationLocation)

    #Line upper left corner
    print ("Erstelle blaue Linie")

    #Headline
    print ("Erstelle die Überschrift")
    # Digital - Text
    print ("Erstelle den digital Text")
    # Congregation - Text
    print ("Erstelle den Gemeindenamen")

    # Month Year
    print ("Erstelle den Monat " + Month + " und das Jahr " + Year)

    # Logo charitable
    print ("Erstelle das Logo mit den Daten: " + LogoPath + "Logo_NAK_karitativ_HQ.tiff")

    # Church image
    print ("Erstelle das Bild der Kirche mit den Daten: " + ChurchPath + ChurchImage)

    # Citation
    print ("Erstelle das Zitat: " + Citation)
    print ("Prüfe auf einen Überlauf")
    # Citation Location
    print ("Erstelle den Ort des Zitats: " + CitationLocation)

    # NAC
    print ("Erstelle den Text 'Neuapostolische Kirche'")
    # North and east germany
    print ("Erstelle den Text 'Nord- und Ostdeutschland'")

    # NAC Logo
    print ("Erstelle das NAK-Logo mit den Daten: " + LogoPath + "Logo_NAK_HQ.tif")

    # Save doc
    print ("Speichere das Dokument mit den Datan: FEHLT")

def colors():
    print ("Erstelle die Farbe NAK-blau 100%")
    print ("Erstelle die Farbe Tabelle-Hintergrund")
    print ("Lösche die Farbe: Blue")
    print ("Lösche die Farbe: Cool Black")
    print ("Lösche die Farbe: Cyan")
    print ("Lösche die Farbe: Green")
    print ("Lösche die Farbe: Magenta")
    print ("Lösche die Farbe: Red")
    print ("Lösche die Farbe: Registration")
    print ("Lösche die Farbe: Rich Black")
    print ("Lösche die Farbe: Warm Black")
    print ("Lösche die Farbe: Yellow")

def createCharStyle(Name, Font, FontSize, Features="", BaseLineOffset = 0, Tracking = 0):
    print ("Erstelle einen neuen Zeichenstil mit den folgenden Werten: ")
    print("Name: " + Name)
    print("Font: " + Font)
    print("FontSize: " + FontSize)
    print("Features: " + Features)
    print("BaseLineOffset: " + BaseLineOffset)
    print("Tracking: " + Tracking)

def createParagraphStyle(Name, LineSpacingMode, Alignment, LeftMargin, RightMargin, GapBefore, GapAfter, FirstIndent, CharStyle, LineSpacing = 0, HasDropCap = 0, DropCapLines = 0 ):
    print("Name: " + Name)
    print("LineSpacingMode: " + LineSpacingMode)
    print("Alignment: " + Alignment)
    print("LeftMargin: " + LeftMargin)
    print("RightMargin: " + RightMargin)
    print("GapBefore: " + GapBefore)
    print("GapAfter: " + GapAfter)
    print("FirstIndent: " + FirstIndent)
    print("CharStyle: " + CharStyle)
    print("LineSpacing: " + LineSpacing)
    print("HasDropCap: " + HasDropCap)
    print("DropCapLines: " + DropCapLines)

    if (LineSpacingMode != 0 and HasDropCap != 0 ):
        print ("Keine Zeilenhöhe und DropCapLine")
    if (LineSpacingMode == 0 and HasDropCap != 0):
        print ("Hat Zeilenhöhe und DropCapLine")
    if (LineSpacingMode != 0 and HasDropCap == 0):
        print ("Hat KEINE Zeilenhöhe und keine DropCapLines")
    if (LineSpacingMode == 0 and HasDropCap == 0):
        print ("Hat Zeilenhöhe und KEINE DropCapLines")

def createNewDocument(NewFile):
    print("Neues Dokument: ", NewFile)

def createFrontPage(Document, Paths, Congregation, MY, Citation, Image ):
    print("Erste Seite erstellen: ", Document, Paths, Congregation, MY, Citation, Image)
def createLastPage(Document, Impress, RecurringEvents, Pastors):
    print("Letzte Seite erstellen: ", Document, Impress, RecurringEvents, Pastors)
def pageNumbering(Files):
    print("Seiten nummerieren: ", Files)
def pageCategories(Document, Pages):
    print("Seiten kategoriesieren: ", Document, Pages)
def newPage(Document, PageAction, PageNumber, Category):
    print("Neue Seite: ", Document, PageAction, PageNumber, Category)
def textwords(Document, Page, Text, Textwords):
    print("Textwörter: ", Document, Page, Text, Textwords)
def newArticle(Document, Headline, Text, Page, Images):
    print("Neuer Artikel: ", Document, Headline, Text, Page, Images)
def schedules(Document, Data, Page):
    print("Terminplan: ", Document, Data, Page)

def openDocument(Document):
    print ("Öffne Dokument")


def processInterfaceFile(InterfaceFile):
    print ("Öffne die Datei: " + InterfaceFile)
    with open(InterfaceFile) as lfiInterfaceFile:
        larrData = json.load(lfiInterfaceFile)

    # Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
    print(larrData)

    for larrAction in larrData:
        print ("Aktionsdaten: ", larrAction)
        print ("Aktion: ",larrAction['action'])
        if larrAction['action'] == "createNewDocument": createNewDocument(
            NewFile=larrAction['file']
        )
        if larrAction['action'] == "createFrontPage": createFrontPage(
            Document=larrAction['document'],
            Paths=larrAction['paths'],
            Congregation=larrAction['congregation'],
            MY=larrAction['my'],
            Citation=larrAction['citation'],
            Image=larrAction['image']
        )
        if larrAction['action'] == "createLastPage": createLastPage(
            Document=larrAction['document'],
            Impress=larrAction['impress'],
            RecurringEvents=larrAction['recurringEvents'],
            Pastors=larrAction['pastors']
        )
        if larrAction['action'] == "pageNumbering": pageNumbering(
            Files=larrAction['destinationFile']
        )
        if larrAction['action'] == "pageCategories": pageCategories(
            Document=larrAction['document'],
            Pages=larrAction['pages']
        )
        if larrAction['action'] == "newPage": newPage(
            Document=larrAction['document'],
            PageAction=larrAction['pageAction'],
            PageNumber=larrAction['pageNumber'],
            Category=larrAction['category']
        )
        if larrAction['action'] == "textwords": textwords(
            Document=larrAction['document'],
            Page=larrAction['page'],
            Text=larrAction['text'],
            Textwords=larrAction['textwords']
        )
        if larrAction['action'] == "newArticle": newArticle(
            Document=larrAction['document'],
            Headline=larrAction['headline'],
            Text=larrAction['text'],
            Page=larrAction['page'],
            Images=larrAction['images']
        )
        if larrAction['action'] == "schedules": schedules(
            Document=larrAction['document'],
            Data=larrAction['data'],
            Page=larrAction['page']
        )

def main(argv):
    processInterfaceFile(argv[1])

if __name__ == '__main__':
    main(os.sys.argv)




