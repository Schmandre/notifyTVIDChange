import string
import config

#Read the data from longID and return the TV ID
fileIN = file(config.pathToScripts+'longID.txt', 'r')
lines = fileIN.readlines()
outputLong = lines[3]
fileIN.close()

#Remove all characters that are not numbers
all=string.maketrans('','')
nodigs=all.translate(all, string.digits)
outputShort = outputLong.translate(all, nodigs)

#Export in a new text file
fileOUT = open(config.pathToScripts+'shortID.txt','w')
fileOUT.write(outputShort[2:])
fileOUT.close()
