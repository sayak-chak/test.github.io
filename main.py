from wordAnalyzer import *

def printOut(strArr):
    for line in strArr: print(line[0])

if __name__ == "__main__":
    filepath = 'sample.txt'
    file = open(filepath, 'r')
    paragraph = file.read().lower()

    freqOfWords = findFreq(paragraph)
    #print(freqOfWords)
    
    orderedImportanceOfLines = summaryOfParagraph(paragraph, freqOfWords)

    printOut(orderedImportanceOfLines)