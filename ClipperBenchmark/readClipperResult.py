def readClipperResult(fileName):
    count=0
    startCouting=False
    with open(fileName, encoding='utf-8') as lines:
        for line in lines:
            if startCouting==True:
                count+=1
            stripLine=str(line.strip())
            if "rewritten queries" in stripLine:
                startCouting=True
          
    return count
print(readClipperResult("/Users/kien/query-rewriting-benchmark/rewriting/lubm/clipper_result/q1.cq.result")) 
#should return 250