from putResultToDictionary import putResultToDictionary

def printResultOfEachOntologyInLatex(ontologyName, reasonerList, resultFileOfAllReasonersDict, finalResultFile):
    """ write result for ontologyName by queries and reasoner, in latex format
        Exampple: 
                ontologyName  clipper rapid requiem (rules)   cliper rapid requiem (runtime) 
                q1            1        2        3             1        2    3
        Input:
            ontologyName: the name of ontology
            listOfReasoners: list of string consisted of reasoner names ordered as it will apprea in the final table 
                            for example ["clipper","requiem","rapid"]
            resultOfEachReasoner: a dictionary where key is the name of the reasoner, value is the result file name of that reasoner
                            for example "clipper": "ontology.clipper.result"
        Output:  
            finalResultFile: file contain result of all reasoner organized by ontology, query, runtime,...
    """
    queries=[]
    resultOfAllReasonersDict = {}
    
    with open(finalResultFile, mode='a', encoding='utf-8') as aFile:
        #Print ontology name    
        aFile.write(ontologyName.replace("_","-"))
    
        #Get result and keep in a dict
        for reasoner in reasonerList:
            # get the result file
            resultFile = resultFileOfAllReasonersDict[reasoner]
            # parse it and store the result in a dict
            resultDict = putResultToDictionary(resultFile)
            queries=list(resultDict.keys())
            queries.sort()
            # put that dict to another dict
            resultOfAllReasonersDict[reasoner] = resultDict
            #Print result for each query    
            #for j in range(numberOfQueries):
            
        #Print result for each query
        for query in queries:
            #print number of rules
            aFile.write("%5s %10s" % ("&",query))
            for reasoner in reasonerList:
                rules=resultOfAllReasonersDict[reasoner][query][0]
                aFile.write("%2s %10s" %("&",rules))
            
            #print time
            for reasoner in reasonerList:
                runtime=resultOfAllReasonersDict[reasoner][query][1]
              #  print("%2s %10s" % ("&",runtime))
                aFile.write("%2s %10s" % ("&",runtime))
            aFile.write(r'\\'+"\n")
        aFile.write(r'\hline'+"\n")
    # with open(finalResultFile, mode='w', encoding='utf-8') as a_file: 
    #    a_file.write("")
   
    #printLatexFooter(finalResultFile)
        
# test
"""
reasonersList=["clipper","rapid","requiem"]
resultFileOfReasonerDic={"clipper":"/Users/kien/query-rewriting-benchmark/rewriting/result-backup/at21_09_2015_13h/hornshiq-univ-12March.owl.clipper.result"}
resultFileOfReasonerDic["requiem"]="/Users/kien/query-rewriting-benchmark/rewriting/result-backup/at21_09_2015_13h/hornshiq-univ-12March.owl.requiem.result"
resultFileOfReasonerDic["rapid"]="/Users/kien/query-rewriting-benchmark/rewriting/result-backup/at21_09_2015_13h/hornshiq-univ-12March.owl.rapid.result"
outPutResultInLatex("uobm", reasonersList, resultFileOfReasonerDic, "/Users/kien/query-rewriting-benchmark/rewriting/result-backup/at21_09_2015_13h/result.tex")
"""