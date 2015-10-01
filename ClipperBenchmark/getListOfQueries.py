import os
#get in folder all files with .cq extension
def getListOfQueries(folder):
    queries=[]
    for fileName in os.listdir(folder):
        if fileName.endswith(".cq"):
            queries.append(fileName)
    return queries
    
#for cqFile in getListOfQueries("/Users/kien/query-rewriting-benchmark/rewriting/lubm/clipper/"):
#    print(cqFile)