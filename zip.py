import os.path
from posixpath import split
from reformatdata import Reformat  
from reformatdata import mapUnicode
from reformatdata import buckets




for root, _, files in os.walk("trainHigh", topdown=False):
    for name in files:
        if not name.startswith("."):
            full_input_path = os.path.join(root, name)
            language = "reformatted-buckets/" + name[:-11]
            # print(language)
            full_outputPath = os.path.join(language, name)
            # print(splitList)
            

            os.mkdir(language)

            print(name)
            inputFp = open(full_input_path, "r")
            outputFp = open(full_outputPath, "w")
            buckets(inputFp, outputFp, True, 6, 12)


        
for root, _, files in os.walk("testData", topdown=False):
    for name in files:
        if not name.startswith("."):
            full_input_path = os.path.join(root, name)
            language = "reformatted-buckets/" + name[:-5]
            # print(language)
            full_outputPath = os.path.join(language, name)
            # print(splitList)

            print(name)
            inputFp = open(full_input_path, "r")
            outputFp = open(full_outputPath, "w")
            buckets(inputFp, outputFp, False, 6, 12)
