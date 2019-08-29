import string

#Einlesen der Datei und Ausgabe der Zeile mit der TV ID
fileIN = file('longID.txt', 'r')
lines = fileIN.readlines()
outputLong = lines[3]
fileIN.close()

#Entfernen aller Zeichen die keine number sind
all=string.maketrans('','')
nodigs=all.translate(all, string.digits)
outputShort = outputLong.translate(all, nodigs)

#Export in die neue Textdatei
fileOUT = open('shortID.txt','w') 
fileOUT.write(outputShort) 
fileOUT.close() 