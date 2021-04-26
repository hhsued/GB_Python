from PyPDF2 import PdfFileWriter, PdfFileReader,PdfFileMerger
import sys
import pathlib
import os

#Argumente:
# 1: Quelldatei -> lstrSourceFile
# 2: Zieldatei -> lstrDestFile
# 3: Zielseite in Zieldokument -> lintDestPage

# Nur wenn Zielposition gleich links muss eine neue, leere Seite erstellt werden

lmodPDFW = PdfFileWriter()
lmodPDFR = PdfFileReader

lstrSourceFile = sys.argv[1]
lstrDestFile = sys.argv[2]
lintDestPage = int(sys.argv[3])

lstrTempFileName = pathlib.Path(lstrDestFile).name.replace(pathlib.Path(lstrDestFile).suffix, "") + "_temp" + pathlib.Path(lstrDestFile).suffix
lstrTempPath = lstrDestFile.replace(pathlib.Path(lstrDestFile).name, lstrTempFileName)

# Datei, welche die einzelnen PDFSeiten hat
file1 = PdfFileReader(lstrSourceFile, "rb")

#if lintDestPage == 1:
#    lmodNewFile = PdfFileWriter()
#    lmodNewFile.addBlankPage(file1.getPage(0).mediaBox[3], file1.getPage(0).mediaBox[2] * 2)
#    lpaNewPage = lmodNewFile.getPage(lintDestPage - 1)
#    lpaNewPage.rotateClockwise(-90)
#    lfilWriteFile = open(lstrDestFile, "wb")
#    lmodNewFile.write(lfilWriteFile)
#    lfilWriteFile.close()

# Datei, welche die entgültigen PDFSeiten hat
#file2 = PdfFileReader(lstrDestFile, "rb")

lintLeftPage = file1.numPages - (lintDestPage - 1)
lintRightPage = 1 + (lintDestPage - 1)

if (lintDestPage % 2) == 0:
    #Even
    lintTemp = lintLeftPage
    lintLeftPage = lintRightPage
    lintRightPage = lintTemp

lmodPDFW.addBlankPage(file1.getPage(0).mediaBox[3], file1.getPage(0).mediaBox[2] * 2)
lpaNewPage = lmodPDFW.getPage(0)
lpaNewPage.rotateClockwise(-90)
print ("Neue Seite 1 erstellt")
lpaPageLeft = file1.getPage(lintLeftPage-1)
lpaPageRight = file1.getPage(lintRightPage-1)
print ("Kopiere die Seite ", lintLeftPage, " auf die LINKE Seite der 1. Seite der neuen Datei")
lpaNewPage.mergeRotatedTranslatedPage(lpaPageLeft, tx=file1.getPage(0).mediaBox[2], ty=file1.getPage(0).mediaBox[2], rotation=-90)
print("Kopiere die Seite ", lintRightPage, " auf die RECHTE Seite der 1. Seite der neuen Datei")
lpaNewPage.mergeRotatedTranslatedPage(lpaPageRight, tx=file1.getPage(0).mediaBox[2] / 2,ty=file1.getPage(0).mediaBox[2] / 2, rotation=-90)
lfilWriteFile = open(lstrTempPath, "wb")
lmodPDFW.write(lfilWriteFile)
lfilWriteFile.close()

if os.path.exists(lstrDestFile):
    merger = PdfFileMerger()
    merger.append(PdfFileReader(lstrDestFile, 'rb'))
    merger.append(PdfFileReader(lstrTempPath, 'rb'))
    os.remove(lstrDestFile)
    merger.write(lstrDestFile)
    os.remove(lstrTempPath)
else:
    os.rename(lstrTempPath, lstrDestFile)



