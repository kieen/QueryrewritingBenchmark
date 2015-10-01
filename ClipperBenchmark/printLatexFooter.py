def printLatexFooter(fileName):
    with open(fileName, mode='a', encoding='utf-8') as aFile:
        aFile.write(r'\end{tabular}'+"\n")
        aFile.write(r'\end{table}'+"\n")
        aFile.write(r'\end{center}'+"\n")
        aFile.write(r'\end{document}' + "\n")
        
