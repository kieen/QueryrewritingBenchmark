from getListOfQueries import getListOfQueries
from runCommandWithTimeout import runCommandWithTimeout
from readClipperResult import readClipperResult
import os
def runClipper(folder, ontology, timeout_in_second):
    """ ontology: ontology to be tested
        folder: parent folder of the ontology. This folder contain queries *.dl files
        timeout_in_second: timeout time
        return: file name of the result file.  
    """
    clipperPath = "/Users/kien/query-rewriting-benchmark/software/clipper/clipper.sh"
    # strip space 
    folder = str(folder).strip()
    ontology = str(ontology).strip()
    
    # create clipper-result folder
    clipperDir = folder + "clipper_result/"
    if not os.path.exists(clipperDir):
        os.makedirs(clipperDir)

    # get full paths
    ontologyFullPath = os.path.join(folder, ontology)        
    resultFile = os.path.join(clipperDir, ontology + ".clipper.result")  
    
    # get all *.cq queries in this foler
    queries = getListOfQueries(folder)
    queries.sort()
    # print("List of queries:")
    # for query in queries:
    #    print(query)
    print("Running queries with Clipper")
    print("Creating the resulting file in:%s" % resultFile)
    try:
        with open(resultFile, mode='w', encoding='utf-8') as a_file: 
            a_file.write("#Run " + ontology + " with Clipper; Time in ms" + '\n')
    except OSError as e:
        print(e)
        
    for query in queries:
        # print("Query: %s"%query)
        queryFullPath = os.path.join(folder, query)
        queryResultFullPath = os.path.join(clipperDir, query + ".result")
        commandString = clipperPath + "  rewrite -tq " + ontologyFullPath + " -cq " + queryFullPath + " -d " + queryResultFullPath                                                               
        
        print("Command to run clipper:" + commandString)
        output = runCommandWithTimeout(commandString, timeout_in_second)
        if not output == "timeout" and not output == "error":
            rules = readClipperResult(queryResultFullPath)
            print(query + ", time: %.2f , rules: %d" % (output, rules))
            with open(resultFile, mode='a', encoding='utf-8') as a_file: 
                a_file.write(query + ", time: %.2f, rules: %s" % (output, rules) + '\n')
        elif output=="timeout": 
            with open(resultFile, mode='a', encoding='utf-8') as a_file: 
                a_file.write(query + ", time: timeout in %s s, rules: %s" % (timeout_in_second, output) + '\n')
            print(output)
        elif output=="error": 
            with open(resultFile, mode='a', encoding='utf-8') as a_file: 
                a_file.write(query + ", time: error, rules: error \n")
            print(output)    
    # return resultFile
    return resultFile       
# Test
# runClipper("/Users/kien/query-rewriting-benchmark/rewriting/lubm/" , "   hornshiq-univ-12March.owl")
