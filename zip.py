import os.path
from posixpath import split
from reformatdata import Reformat  




# for root, _, files in os.walk("trainHigh", topdown=False):
#     for name in files:
#         if not name.startswith("."):
#             full_input_path = os.path.join(root, name)
#             language = "reformattedData/" + name[:-11]
#             # print(language)
#             full_outputPath = os.path.join(language, name)
#             # print(splitList)
            

#             os.mkdir(language)

#             print(name)
#             inputFp = open(full_input_path, "r")
#             outputFp = open(full_outputPath, "w")
#             Reformat(inputFp, outputFp, True)


        
for root, _, files in os.walk("testData", topdown=False):
    for name in files:
        if not name.startswith("."):
            full_input_path = os.path.join(root, name)
            language = "reformattedData/" + name[:-5]
            # print(language)
            full_outputPath = os.path.join(language, name)
            # print(splitList)

            print(name)
            inputFp = open(full_input_path, "r")
            outputFp = open(full_outputPath, "w")
            Reformat(inputFp, outputFp, False)