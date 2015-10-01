#!/usr/bin/env python3
import os,sys

def splitQueryFile(fileName, destinationFolder):
    count=0
    with open(fileName, encoding='utf-8') as manyLines:
        for aline in manyLines:
            stripLine=str(aline.strip())
            print(stripLine)
            if not stripLine=="" and not stripLine.startswith("%"):
                count+=1
                newQueryName="q"+str(count)+".cq"
                newQueryNamePath=os.path.join(destinationFolder,newQueryName)
                with open(newQueryNamePath,mode='w', encoding='utf-8 ') as aFile:
                        aFile.write(stripLine+'\n')
if __name__=='__main__':
    print("Example run: splitQueryFile     filename    destinationFolder ")
    if len(sys.argv)==3:
        splitQueryFile(sys.argv[1],sys.argv[2])
        print("The resulting queries are placed in %s"%sys.argv[2])
    else:
        print("Not correct arguments, see Example run")

                
            
            