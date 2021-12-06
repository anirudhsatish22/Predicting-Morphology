import numpy as np

def distance(str1, str2):
    """Simple Levenshtein implementation for evalm."""
    m = np.zeros([len(str2)+1, len(str1)+1])
    for x in range(1, len(str2) + 1):
        m[x][0] = m[x-1][0] + 1
    for y in range(1, len(str1) + 1):
        m[0][y] = m[0][y-1] + 1
    for x in range(1, len(str2) + 1):
        for y in range(1, len(str1) + 1):
            if str1[y-1] == str2[x-1]:
                dg = 0
            else:
                dg = 1
            m[x][y] = min(m[x-1][y] + 1, m[x][y-1] + 1, m[x-1][y-1] + dg)
    return int(m[len(str2)][len(str1)])


def readCorrectTest(fp):
    D = set()
    for line in fp:
        newLine  = line.rstrip()
        listOfWords = newLine.split("\t")
        D.add(listOfWords[1])

    return D




def accuracy(fp):
    i = 0
    for line in fp:
        newLine  = line.rstrip()
        listOfWords = newLine.split("\t")

        correctfp = open("testData/hindi-test", "r")
    

        setOfCorrectInflections = readCorrectTest(correctfp)
        if listOfWords[1] in setOfCorrectInflections:
            i+=1
        
    print(i/1000)


# def levenshtein(predictedfp, correctfp):

print(distance("नहाना", "तुम नहाते"))
# fp = open("testData/hindi-test", "r")



fp = open("hindi.txt", "r")
accuracy(fp)
# readCorrectTest(fp)

