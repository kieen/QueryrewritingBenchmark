def putResultToDictionary(fileName):
    """ Read final result file of reasoners
        Input: fileName which contains lines of the form: 
        q1.cq, time: 134, rules: 123
        q1.cq, time: timeout , rules: timeout
        Output:  
    """
    print("Reading result from file:"+fileName)
    resultMap={}
    with open(fileName, encoding='utf-8') as lines:
        for aline in lines:
            aline = str(aline.strip())
            if not aline.startswith("#"):
                splitLine = aline.split(",")
                queryName=splitLine[0].strip()
                
                timeSection=splitLine[1].strip()
                splitTimeSection=timeSection.split(":")
                if splitTimeSection[0]=="timeout":
                    runTime="timeout" 
                else:
                    runTime=splitTimeSection[1].strip()
                
                ruleSection=splitLine[2].strip()
                splitRuleSection=ruleSection.split(":")
                numberOfRules=splitRuleSection[1].strip()
                
                resultMap[queryName]=(numberOfRules,runTime)
    return resultMap
#test
#resultMap= putResultToDictionary("/Users/kien/query-rewriting-benchmark/rewriting/result-backup/at21_09_2015_13h/galen-doctored_elhi.owl.requiem.result")
#print(resultMap)
#print(len(resultMap))
#print(resultMap["q1.cq"])