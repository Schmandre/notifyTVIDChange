#!/bin/sh
FILE=/root
if [ -f "$FILE/shortID.txt" ]; then
    echo "$FILE/shortID.txt exist"
	  mv $FILE/shortID.txt /root/shortIDOld.txt
    python idExport.py > longID.txt
    sleep 10
    python read.py
    sleep 10
    DIFF=$(diff shortID.txt shortIDOld.txt)
    if [ "$DIFF" != "" ]
    then
      echo "Die TeamViewer ID's haben sich geaendert"
      python mail.py
    fi
    else
      echo "$FILE does not exist"
      python idExport.py > longID.txt
      sleep 10
      python read.py
    fi
rm longID.txt
