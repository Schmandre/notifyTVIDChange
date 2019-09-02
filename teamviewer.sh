#!/bin/sh
FILE="SET YOUR PATH HERE"
if [ -f "$FILE/shortID.txt" ]; then
    echo "$FILE/shortID.txt already exists"
	  mv $FILE/shortID.txt $FILE/shortIDOld.txt
    python $FILE/idExport.py > $FILE/longID.txt
    sleep 10
    python $FILE/read.py
    sleep 10
    DIFF=$(diff shortID.txt shortIDOld.txt)
    if [ "$DIFF" != "" ]
    then
      echo "TeamViewer ID has changed!"
      python $FILE/mail.py
    fi
    else
      echo "$FILE/shortID.txt does not exist, creating"
      python $FILE/idExport.py > $FILE/longID.txt
      sleep 10
      python $FILE/read.py
    fi
rm $FILE/longID.txt
