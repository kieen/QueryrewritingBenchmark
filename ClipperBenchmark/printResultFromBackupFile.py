from outputResultInLatex import outPutResultInLatex
from printLatexHeader import printLatexHeader
from printLatexFooter import printLatexFooter
def printResultFromBackupFiles(ontologyList, folderOfResultFile, latexFileName):
    fullPathLatexFile=folderOfResultFile+r'/'+latexFileName
    fullPathOntologyList=folderOfResultFile+r'/'+ontologyList
    printLatexHeader(3,fullPathLatexFile)
    reasonerList=["clipper","rapid","requiem"]
    with open(fullPathLatexFile, mode='a', encoding='utf-8') as aFile:
        #Print names of reasoner in the table
        aFile.write(r' &')
        for reasoner in reasonerList:
            aFile.write("&%8s"%reasoner)
        for reasoner in reasonerList:
            aFile.write("&%8s"%reasoner)
        aFile.write(r' \\'+"\n")
        aFile.write(r'\hline'+"\n")
    
    with open(fullPathOntologyList, encoding='utf-8') as manyLines:
        for aLine in manyLines:
            anOntologyName=aLine.strip()
            
            resultFileOfReasonerDict={}
            resultFileOfReasonerDict["clipper"]=folderOfResultFile+r'/'+anOntologyName+".clipper.result"
            resultFileOfReasonerDict["rapid"]=folderOfResultFile+r'/'+anOntologyName+".rapid.result"
            resultFileOfReasonerDict["requiem"]=folderOfResultFile+r'/'+anOntologyName+".requiem.result"
            
            outPutResultInLatex(anOntologyName, reasonerList, resultFileOfReasonerDict, fullPathLatexFile)
            
    printLatexFooter(fullPathLatexFile)
printResultFromBackupFiles("ontologylist.txt", "/Users/kien/query-rewriting-benchmark/rewriting/result-backup/at21_09_2015_13h", "finalResult.tex")