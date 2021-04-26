from PyPDF2 import PdfFileWriter, PdfFileReader
from pathlib import Path
import sys

lmodPDFW = PdfFileWriter()
lmodPDFR = PdfFileReader

lstrSourceFile = sys.argv[1]
lstrDestFile = sys.argv[2]

print ("Beginne die Bearbeitung der Datei: ", lstrSourceFile)

lpdfInputFile = lmodPDFR(lstrSourceFile)

lintPageCount = lpdfInputFile.getNumPages()

larrPageOrder = []
larrPages = []

for lintPage in range(lintPageCount):
    larrPages.append(lintPage+1)

lboolIsEven = True

for _ in range(int(lintPageCount / 2)):
    if lboolIsEven:
        larrPageOrder.append(larrPages[-1])
        larrPageOrder.append(larrPages[0])
        lboolIsEven = False
    else:
        larrPageOrder.append(larrPages[0])
        larrPageOrder.append(larrPages[-1])
        lboolIsEven = True
    del larrPages[-1]
    del larrPages[0]

lintNewPageCount = int(lintPageCount / 2)

for i in range(lintNewPageCount):
    lmodPDFW.addBlankPage(lpdfInputFile.getPage(0).mediaBox[3], lpdfInputFile.getPage(0).mediaBox[2] * 2)
    lpaNewPage = lmodPDFW.getPage(i)
    lpaNewPage.rotateClockwise(-90)
    print ("Neue Seite ", i+1, " erstellt")
    lpaPageLeft = lpdfInputFile.getPage(larrPageOrder[0]-1)
    lpaPageRight = lpdfInputFile.getPage(larrPageOrder[1]-1)
    print ("Kopiere die Seite ", larrPageOrder[0], " auf die LINKE Seite der ", i+1, ". Seite der neuen Datei")
    lpaNewPage.mergeRotatedTranslatedPage(lpaPageLeft, tx=lpdfInputFile.getPage(0).mediaBox[2], ty=lpdfInputFile.getPage(0).mediaBox[2], rotation=-90)
    print("Kopiere die Seite ", larrPageOrder[1], " auf die RECHTE Seite der ", i + 1, ". Seite der neuen Datei")
    lpaNewPage.mergeRotatedTranslatedPage(lpaPageRight, tx=lpdfInputFile.getPage(0).mediaBox[2] / 2,ty=lpdfInputFile.getPage(0).mediaBox[2] / 2, rotation=-90)
    lfilWriteFile = open(lstrDestFile, "wb")
    lmodPDFW.write(lfilWriteFile)
    lfilWriteFile.close()
    del larrPageOrder[0]
    del larrPageOrder[0]

lfilWriteFile = open(lstrDestFile, "wb")
lmodPDFW.write(lfilWriteFile)
lfilWriteFile.close()

print ("Bearbeitung abgeschlossen! Neue Datei: ", lstrDestFile)