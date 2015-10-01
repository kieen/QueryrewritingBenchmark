# return a tuple (logic_program_size, number_of_rewritten_queries)
def readRapidResult(fileName):
    logicProgramSize = 0;
    numberOfRewritingQueries = 0;
    with open(fileName, encoding='utf-8') as manyLines:
        for line in manyLines:
            stripLine = str(line.strip())
            if "Logic program size" in stripLine:
                splitedLine = stripLine.split(": ")                
                logicProgramSize = splitedLine[1]
                print("Logic program size: %s" % logicProgramSize)
            if "Rewritings" in stripLine:
                splitedLine = stripLine.split(":")
                sizeString = splitedLine[1]
                numberOfRewritingQueries = sizeString.split("-")[0]
                print("Number of rewritten queries: %s" % numberOfRewritingQueries)
            
    return (logicProgramSize, numberOfRewritingQueries)
#print(readRapidResult("/Users/kien/query-rewriting-benchmark/rewriting/lubm/rapid_result/q1.cq.result")) 
# should return 250
