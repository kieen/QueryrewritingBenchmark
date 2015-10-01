#!/usr/bin/env python3
from runClipper import runClipper
from runRapid import runRapid
from runRequiem import runRequiem
import shutil,os
import time
from os.path import sys
from printLatexHeader import printLatexHeader
from printLatexFooter import printLatexFooter
from printResultOfEachOntologyInLatex import printResultOfEachOntologyInLatex
# run the benchmark and return all result file of Clipper and Rapid in tuple
def runBenchmark(ontologyList, timeout_in_second, finalResultFile, backupFolder):
    resultFilesClipper = []
    resultFilesRapid = []
    resultFilesRequiem = []
    #reasonerList = ["Clipper", "Rapid", "Requiem"]
    reasonerList = ["Clipper", "Rapid"]
    numberOfReasoner = len(reasonerList)
    
    # Print header of the latex file
    printLatexHeader(numberOfReasoner, finalResultFile)
    # Print name of reasoners
    with open(finalResultFile, mode='a', encoding='utf-8') as aFile:
        # Print names of reasoner in the table
        aFile.write(r' &')
        for reasoner in reasonerList:
            aFile.write("&%8s" % reasoner)
        for reasoner in reasonerList:
            aFile.write("&%8s" % reasoner)
        aFile.write(r' \\' + "\n")
        aFile.write(r'\hline' + "\n")
    # For each ontology, run reasoner and print out the result
    with open(ontologyList, encoding='utf-8') as ontListFile:
        for aline in ontListFile:
            aline = str(aline.strip())
            if not aline == "" and not aline.startswith("%") and not aline.startswith("#"):
                splitLine = aline.split(',')
                ontology = splitLine[0].strip()
                folder = splitLine[1].strip()
                print('ontology:' + ontology)
                print('folder:' + folder)
                fullPathOntology = os.path.join(folder, ontology)
                print('full path:' + fullPathOntology)
                
                #Run Clipper
                resultFileOfClipper = runClipper(folder, ontology, timeout_in_second)
                resultFilesClipper.append(resultFileOfClipper)
                
                #Run Rapid
                resultFileOfRapid = runRapid(folder, ontology, timeout_in_second)
                resultFilesRapid.append(resultFileOfRapid)
                
                #Run Requiem
                #resultFileOfRequiem = runRequiem(folder, ontology, timeout_in_second)
                #resultFilesRequiem.append(resultFileOfRequiem)
                
                #Collect the result and output to the latex file
                resultFileOfReasonerDict = {}
                resultFileOfReasonerDict["Clipper"] = resultFileOfClipper
                resultFileOfReasonerDict["Rapid"] = resultFileOfRapid
                #resultFileOfReasonerDict["Requiem"] = resultFileOfRequiem
                
                printResultOfEachOntologyInLatex(ontology, reasonerList, resultFileOfReasonerDict, finalResultFile)
                
    printLatexFooter(finalResultFile)            
    return (resultFilesClipper, resultFilesRapid, resultFilesRequiem)
if __name__ == '__main__':
    if len(sys.argv) == 5:
        (resultFilesClipper, resultFilesRapid, resultFilesRequiem) = runBenchmark(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        timeNow = time.strftime("%d_%m_%Y_%H_%M")
        backupDir=sys.argv[4] 
        newFolder = os.path.join(backupDir, "at"+timeNow);
        os.makedirs(newFolder)
        
        print("#Result files of Clipper:")
        for file in resultFilesClipper:
            print(file)
            shutil.copy(file, newFolder)
            
        print("#Result files of Rapid:")
        for file in resultFilesRapid:
            print(file)
            shutil.copy(file, newFolder)
            
        #print("#Result files of Requiem:")
        #for file in resultFilesRequiem:
        #    print(file)    
        #    shutil.copy(file, newFolder)
            
        print("#The collected result in latex:"+sys.argv[3])
        shutil.copy(sys.argv[3], newFolder)
        print("All results have a backup version in the folder:"+ newFolder)
    else:
        print("Please use only 3 arguments: ontologylist,  timeout in second, final_result_file, backup-folder")
