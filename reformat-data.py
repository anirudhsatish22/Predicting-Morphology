import argparse
import sys


def main(args):

    inputFp = args.input_file

    outputFp = args.output_file

    for line in inputFp:
        newLine  = line.rstrip()
        
        listOfWords = newLine.split("\t")
        lemma = listOfWords[0]
        conjugated = listOfWords[1]
        features = listOfWords[2]
        
        if (args.train):
            reformatted = features+lemma+features + "\t" + conjugated + "\n"
        else:
            reformatted = features+lemma+features + "\n"
        outputFp.write(reformatted)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", "-i", type=argparse.FileType('r'), help="input instances (train or test)", metavar="FILE")
    parser.add_argument("--output_file", "-o", type=argparse.FileType('w'), help="output formatted data", metavar="FILE", default=sys.stdout)

    eval_group = parser.add_mutually_exclusive_group(required=True)
    eval_group.add_argument("--train", action="store_true")
    eval_group.add_argument("--test", action="store_true")


    args=parser.parse_args()
    main(args)

    for fp in (args.output_file, args.input_file): fp.close()
