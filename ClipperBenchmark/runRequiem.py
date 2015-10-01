from getListOfQueries import getListOfQueries
from runCommandWithTimeout import runCommandWithTimeout
from readRequiemResult import readRequiemResult
import os

def runRequiem(folder, ontology, timeout_in_second):
    requiemJar = "/Users/kien/query-rewriting-benchmark/software/requiem.jar"
    # strip space 
    folder = str(folder).strip()
    ontology = str(ontology).strip()
    
    # create requiem-result folder
    requiemDir = folder + "requiem_result/"
    if not os.path.exists(requiemDir):
        os.makedirs(requiemDir)

    # get full paths
    ontologyFullPath = os.path.join(folder, ontology)        
    resultFile = os.path.join(requiemDir, ontology + ".requiem.result")  
    
    # get all *.cq queries in this foler
    queries = getListOfQueries(folder)
    queries.sort()
    # print("List of queries:")
    # for query in queries:
    #    print(query)
    print("Running queries with requiem")
    print("Creating the resulting file in:%s" % resultFile)
    try:
        with open(resultFile, mode='w', encoding='utf-8') as a_file: 
            a_file.write("#Run " + ontology + " with requiem; Time in ms" + '\n')
    except OSError as e:
        print(e)
        
    for query in queries:
        # print("Query: %s"%query)
        queryFullPath = os.path.join(folder, query)
        queryResultFullPath = os.path.join(requiemDir, query + ".result")
        commandString = "java -jar " + requiemJar + " " +queryFullPath + " file:" + ontologyFullPath + " " + queryResultFullPath + " G"                                                               
        
        print("Command to run requiem:%s \n " % commandString)
        output = runCommandWithTimeout(commandString, timeout_in_second)
        if not output == "timeout" and not output == "error":
            rewrittenQueries = readRequiemResult(queryResultFullPath)
            # print(query + ", time %.2f, program size: %s , queries: %s" % (output, programSize, rewrittenQueries))
            print(query + ", time %.2f, rules: %s \n" % (output, rewrittenQueries))
            with open(resultFile, mode='a', encoding='utf-8') as a_file: 
            #   a_file.write(query + ", time: %.2f, program size: %s , queries: %s" % (output, programSize, rewrittenQueries) + '\n')
                a_file.write(query + ", time: %.2f, rules: %s" % (output, rewrittenQueries) + '\n')
        elif output=="timeout": 
            with open(resultFile, mode='a', encoding='utf-8') as a_file: 
                a_file.write(query + ", time: timeout in %s s, rules: %s" % (timeout_in_second, output) + '\n')
            print(output)
        elif output=="error": 
            with open(resultFile, mode='a', encoding='utf-8') as a_file: 
                a_file.write(query + ", time: error, rules: error \n")
            print(output)    
            #   a_file.write(query +  "time: %s, program size: %s , queries: %s" % (output, output,output) + '\n')
            # print(output)
    # return resultFile
    return resultFile
# Test
#runRequiem("/Users/kien/query-rewriting-benchmark/rewriting/lubm/" , "   hornshiq-univ-12March.owl",100)
