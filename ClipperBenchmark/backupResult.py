#!/usr/bin/env python3
import shutil, os
import time
from os.path import sys
def backUpFile(backupIndex, backupDir):
    timeNow = time.strftime("%d_%m_%Y_%H"+"h")
    newFolder = os.path.join(backupDir, "at"+timeNow);
    os.makedirs(newFolder)
    with open(backupIndex, encoding='utf-8') as manyLines:
        for line in manyLines:
            stripLine = str(line.strip())
            if not stripLine.startswith("#"):
                shutil.copy(stripLine, newFolder)
    
if __name__ == "__main__":
    if len(sys.argv) == 3:
        backUpFile(sys.argv[1], sys.argv[2])
    else:
        print("Provide index file and destination directory")
    
