# return a tuple (logic_program_size, number_of_rewritten_queries)
def readRequiemResult(fileName):
    
    numberOfRewritingQueries = 0;
    with open(fileName, encoding='utf-8') as manyLines:
        for line in manyLines:
            stripLine = str(line.strip())
            if "Size of the rewriting (queries)" in stripLine:
                splitedLine = stripLine.split(": ")                
                numberOfRewritingQueries = splitedLine[1]
                print("Number of rewritten queries: %s" % numberOfRewritingQueries)
            
    return (numberOfRewritingQueries)

#n=readRequiemResult("/Users/kien/query-rewriting-benchmark/download/requiem/q2.result")
#print(n)
