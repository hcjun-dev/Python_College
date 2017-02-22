##
# Hyungchol Jun
# 2014-03-19
# 0324 - P_7.9.py
import sys

def func0324():
    inputFile = open("%s" % sys.argv[1], "r")
    outputFile = open("%s" % sys.argv[2], "w")

    inputLines = inputFile.readlines()

    for i in range(len(inputLines), 0, -1):
        inputLines[i-1] = inputLines[i-1].rstrip()
        outputFile.write(inputLines[i-1])
        if i != 1:
            outputFile.write("\n")
    inputFile.close()
    outputFile.close()
