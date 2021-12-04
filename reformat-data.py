# fp = open('all/spanish-train-high', 'r')

# writer = open('spanish-formatted-data', 'w')


# for line in fp:
#     # print(line)
#     newLine  = line.rstrip()
    
#     listOfWords = newLine.split("\t")
#     lemma = listOfWords[0]
#     features = listOfWords[2]
    
#     newList = [features+lemma+features, listOfWords[1]]
#     writer.write("\t".join(newList))
#     writer.write("\n")



fp = open('all/spanish-test', 'r')

writer = open('spanish-test-data', 'w')


for line in fp:
    # print(line)
    newLine  = line.rstrip()
    
    listOfWords = newLine.split("\t")
    lemma = listOfWords[0]
    features = listOfWords[2]
    
    newList = [features+lemma+features]
    writer.write("\t".join(newList))
    writer.write("\n")


