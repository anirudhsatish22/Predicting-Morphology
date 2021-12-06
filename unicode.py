fp = open("trainHigh/hindi-train-high", "r")
featureSet = set()
wholeSet = set()
for line in fp:
    newLine = line.rstrip()
    listOfWords = newLine.split("\t")

    x = listOfWords[2]
    features = x.split(";")
    y = ''.join(features)
    print(y)
    wholeSet.add(y)
    for f in features:
        featureSet.add(f)


print("featureSet", len(featureSet))
print("whole set", len(wholeSet))
