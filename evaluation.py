import numpy as np
import argparse
import sys 
import os.path

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
    i = 0
    for line in fp:
        i+=1
        newLine  = line.rstrip()
        listOfWords = newLine.split("\t")
        
        D.add(listOfWords[1])

    return D,i




def accuracy(predictedFp, expectedFp):
    i = 0
    j = 0
    setOfCorrectInflections,total = readCorrectTest(expectedFp)
    expectedFp.seek(0)
    for line in predictedFp:
        newLine  = line.rstrip()
        listOfWords = newLine.split("\t")
        # print(listOfWords[1])
        j+=1
        if listOfWords[1] in setOfCorrectInflections:
            i+=1
        
    predictedFp.seek(0)
    if j == 0:
        j = 1
    return (i/total, j/total)




def levenshtein(predictedfp, correctfp):
    correctfp.seek(0)

    # for line in correctfp:
    #     newLine = line.rstrip()
    #     listOfWords = newLine.split("\t")
    #     correctInflection = listOfWords[1]
        
    #     predictedLine = predictedfp.readline()
    #     newPredictedLine = predictedLine.rstrip()
    #     predictedInflection = newPredictedLine.split("\t")[1]
    dist = 0
    total = 0
    for line in predictedfp:
        # print(line)
        newLine = line.rstrip()
        listOfWords = newLine.split("\t")
        predictedInflection = listOfWords[1]

        correctLine = correctfp.readline()
        newCorrectLine = correctLine.rstrip()
        correctListOfWords = newCorrectLine.split("\t")
        lemma = correctListOfWords[0]
        while (lemma not in listOfWords[0]):
            correctLine = correctfp.readline()
            newCorrectLine = correctLine.rstrip()
            correctListOfWords = newCorrectLine.split("\t")
            lemma = correctListOfWords[0]


        if len(correctListOfWords) == 2:
            correctInflection = correctListOfWords[1]
        else:
            correctInflection = "aaaa"
        # correctInflection = correctListOfWords[1]

        # print(correctInflection, predictedInflection)
        dist += distance(predictedInflection, correctInflection)
        total += 1

    if total == 0:
        total = 0.1 # to avoid divide by 0 errors,  


    # print(round(dist/total, 2))
    # print(total)
    return round(dist/total, 2)
        
            

# print(round(distance("नहाना", "तुम नहाते"), 2))


# round(dist/total, 2)
# fp = open("testData/hindi-test", "r")



# fp = open("hindi.txt", "r")
# output = open("testData/hindi-test", "r")
# levenshtein(fp, output)
# accuracy(fp)
# readCorrectTest(fp)


def evaluateOutput(predictedFp, expectedFp):
    acc = accuracy(predictedFp, expectedFp)
    levDist = levenshtein(predictedFp, expectedFp)

    return ((round(acc[0]*100,2), acc[1]), levDist)


def evalAll(outputFp,directory):
    for root, _, files in os.walk(directory, topdown=False):
        for name in files:
            if not name.startswith("."):
                full_path = os.path.join(root, name)

                expectedFilePath = "testData/" + name + "-test"

                print(expectedFilePath)

                predicted = open(full_path, "r")
                expected = open(expectedFilePath, "r")

                acc, levDist = evaluateOutput(predicted, expected)
                # (name,  acc[0], levDist)
                outputStr = name + "\n\tpercentage guessed: " + str(round(acc[1]*100,2)) + "\n"
                outputFp.write(outputStr)
                




def main(args):
    # if args:
    #     x = evaluateOutput(args.predictedOutput, args.expectedOutput)    
    #     # for line in args.expectedOutput:
    #     #     print(line)
    #     print(x)
    # else:
    #     evalAll()

    if (args.run_all):    
        evalAll(args.writeOutput, args.directory)
    else:
        x = evaluateOutput(args.predictedOutput, args.expectedOutput)    
    #     # for line in args.expectedOutput:
    #     #     print(line)
        print(x)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--predictedOutput", "-p", type=argparse.FileType('r'), help="txt file with the predicted inflections from the model", metavar="FILE")
    parser.add_argument("--expectedOutput", "-e", type=argparse.FileType('r'), help="test file with lemma, features and expected correct inflection", metavar="FILE", default=sys.stdout)

    parser.add_argument("--run_all", action="store_true")
    parser.add_argument("--writeOutput", "-w", type=argparse.FileType('w'), help="File to write output for all the data", metavar="FILE")
    parser.add_argument("--directory", help="Directory name")
    args=parser.parse_args()
    main(args)

    for fp in (args.predictedOutput, args.expectedOutput): fp.close()
