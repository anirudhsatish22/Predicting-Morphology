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


def mapUnicode(fp, op, mode):
    D = {}
    i = 300
    for line in fp:
        newLine = line.rstrip()
        listOfWords = newLine.split("\t")

        x = listOfWords[2]
        features = x.split(";")
        print(features)
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


        print(features)
        if features in D:
            x = D[features]
        else:
            x = chr(i)
            i+=1
        
        if (mode):
            reformatted = x+lemma+x + "\t" + conjugated
        else:
            reformatted = x+lemma+x
        op.writeline(reformatted)

def main(args):

    if (args.nocompression):    
        Reformat(args.input_file, args.output_file, args.train)
    elif (args.unicodeMap):
        mapUnicode(args.input_file, args.output_file, args.train)
    # Ref2(args.input_file, args.output_file, args.train)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", "-i", type=argparse.FileType('r'), help="input instances (train or test)", metavar="FILE")
    parser.add_argument("--output_file", "-o", type=argparse.FileType('w'), help="output formatted data", metavar="FILE", default=sys.stdout)

    eval_group = parser.add_mutually_exclusive_group(required=True)
    eval_group.add_argument("--train", action="store_true")
    eval_group.add_argument("--test", action="store_true")


    eval_group = parser.add_mutually_exclusive_group(required=True)
    eval_group.add_argument("--nocompression", action="store_true")
    eval_group.add_argument("--unicodeMap", action="store_true")



    args=parser.parse_args()
    main(args)

    for fp in (args.output_file, args.input_file): fp.close()
