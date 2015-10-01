def printLatexHeader(numberOfReasoners, fileName):
    numberOfReasoners = int(numberOfReasoners)
    with open(fileName, mode='w', encoding='utf-8') as aFile:
        aFile.write(r'\documentclass{llncs}' + "\n")
        aFile.write(r'\begin{document}' + "\n")
        aFile.write(r'\begin{center}'+"\n")
        aFile.write(r'\begin{table}'+"\n")
        aFile.write(r'\begin{tabular}{|l|l|')
        for i in range(numberOfReasoners):
            aFile.write(r'c')
        aFile.write(r'|')
        for i in range(numberOfReasoners):
            aFile.write(r'c')
        aFile.write(r'@{~}|}' + "\n") 
        aFile.write(r'\hline ' + "\n")
        from _ast import Str
        nextLine = r'& & \multicolumn{' + str(numberOfReasoners) + r'}{c|}{\# Rules/CQs} & \multicolumn{' + str(numberOfReasoners) \
        + r'}{c|}{Time (s)}\\ '
        aFile.write(nextLine+"\n")
        aFile.write(r'\hline ' + "\n")
        
        
#prinLatexHeader(3,"test.tex")
