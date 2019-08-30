#!/bin/sh
FILE="SET YOUR PATH HERE"
if [ -f "$FILE/shortID.txt" ]; then
    echo "$FILE/shortID.txt exist"
	  mv $FILE/shortID.txt $FILE/shortIDOld.txt
    python idExport.py > longID.txt
    sleep 10
    python read.py
    sleep 10
    DIFF=$(diff shortID.txt shortIDOld.txt)
    if [ "$DIFF" != "" ]
    then
      echo "The TeamViewer ID has changed!"
      python mail.py
    fi
    else
      echo "$FILE/shortID.txt does not exist"
      python idExport.py > longID.txt
      sleep 10
      python read.py
    fi
rm longID.txt
