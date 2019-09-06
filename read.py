import string
import config

#Read the data from longID and return the TV ID
with open(config.pathToScripts+'longID.txt') as fileIN:
    for countLine, line in enumerate(fileIN, 1):
        if "TeamViewer ID:" in line:
            countLine = str(countLine)
            outputLong = line

#Remove all characters that are not numbers
all=string.maketrans('','')
nodigs=all.translate(all, string.digits)
outputShort = outputLong.translate(all, nodigs)

#Export in a new text file
fileOUT = open(config.pathToScripts+'shortID.txt','w')
fileOUT.write(outputShort[2:])
fileOUT.close()
