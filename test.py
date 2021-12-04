fp = open('all/adyghe-train-high', 'r')


for line in fp:
    listOfWords = line.split()
    print(listOfWords)