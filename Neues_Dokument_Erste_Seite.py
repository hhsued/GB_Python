#doc = scribus.newDoc((148,210), (10,10,10,10), PORTRAIT, 1, UNIT_MILLIMETERS, NOFACINGPAGES, FIRSTPAGELEFT)
#scribus.createLine(10,10,10,33,"Strich_oben")
#scribus.setLineWidth(0.75,"Strich_oben")
#scribus.createText(10,22,128,20,"Oben")
#scribus.setText('Gemeindebrief   DIGITAL Buxtehude',"Oben")
#scribus.selectText(1,14,"Oben")
#scribus.setCharacterStyle('Erste Seite - Gemeindebrief - gro�',"Oben")
#scribus.deselectAll()
list = scribus.getCharStyles()