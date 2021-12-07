import argparse
import sys


def Reformat(inputFp, outputFp, mode):


    for line in inputFp:
        newLine  = line.rstrip()
        listOfWords = newLine.split("\t")
        lemma = listOfWords[0]
        conjugated = listOfWords[1]
        features = listOfWords[2]
        
        if (mode):
            reformatted = features+lemma+features + "\t" + conjugated + "\n"
        else:
            reformatted = features+lemma+features + "\n"
        outputFp.write(reformatted)

def buckets(fp, op, mode, len_tags, len_lemma):
    for line in fp:
        newLine  = line.rstrip()
        listOfWords = newLine.split("\t")
        lemma = listOfWords[0]
        conjugated = listOfWords[1]
        tags = listOfWords[2]

        tags = tags.replace(";", "")
        while len(tags) < len_tags:
            tags = tags + tags
        tags = tags[:len_tags]

        while len(lemma) < len_lemma:
            lemma = lemma + lemma
        lemma = lemma[:len_lemma]

        
        if (mode):
            reformatted = tags+lemma+tags + "\t" + conjugated + "\n"
        else:
            reformatted = tags+lemma+tags + "\n"
        op.write(reformatted)


def mapUnicode(fp, op, mode):
    D = {}
    i = 300
    for line in fp:
        newLine = line.rstrip()
        listOfWords = newLine.split("\t")

        x = listOfWords[2]
        features = x.split(";")
        for feature in features[1:]:
            if feature not in D:
                D[feature] = chr(i)
                i+=1


        # print(y)
        
    fp.seek(0)


    for line in fp:
        newLine  = line.rstrip()
        listOfWords = newLine.split("\t")
        lemma = listOfWords[0]
        conjugated = listOfWords[1]
        features = listOfWords[2]


        listOfFeatures = features.split(";")
        morphString = listOfFeatures[0]
        for feature in listOfFeatures[1:]:
            if feature in D:
                morphString += D[feature]
            else:
                morphString += D[feature]
                i+=1

        
        if (mode):
            reformatted = morphString+lemma+morphString + "\t" + conjugated + "\n"
        else:
            reformatted = morphString+lemma+morphString + "\n"
        op.write(reformatted)

def main(args):

    if (args.nocompression):    
        Reformat(args.input_file, args.output_file, args.train)
    elif (args.unicodeMap):
        mapUnicode(args.input_file, args.output_file, args.train)
    elif (args.buckets):
        buckets(args.input_file, args.output_file, args.train, args.len_tags, args.len_lemma)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", "-i", type=argparse.FileType('r'), help="input instances (train or test)", metavar="FILE")
    parser.add_argument("--output_file", "-o", type=argparse.FileType('w'), help="output formatted data", metavar="FILE", default=sys.stdout)

    train_or_test = parser.add_mutually_exclusive_group(required=True)
    train_or_test.add_argument("--train", action="store_true")
    train_or_test.add_argument("--test", action="store_true")


    compression_type = parser.add_mutually_exclusive_group(required=True)
    compression_type.add_argument("--nocompression", action="store_true")
    compression_type.add_argument("--unicodeMap", action="store_true")
    compression_type.add_argument("--buckets", action="store_true")

    parser.add_argument("--len_lemma", type=int, help="length of the lemma bucket for bucket compression")
    parser.add_argument("--len_tags", type=int, help="length of the tags bucket for bucket compression")



    args=parser.parse_args()
    main(args)

    for fp in (args.output_file, args.input_file): fp.close()
