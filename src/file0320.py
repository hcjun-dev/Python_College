##
# Hyungchol Jun
# 2014-03-19
# 0320 - P_7.2.py

def func0320():
    inFileName = input("Please enter the file name: ")
    outFileName = input("Please enter the output file name: ")

    inputFile = open("%s.txt" % inFileName, "r")
    outFile = open("%s.txt" % outFileName, "w")
    lineNum = inputFile.tell()
    for line in inputFile:
        lineNum += 1
        outFile.write("/* %d */ " % lineNum)
        outFile.write("%s" % line)
    inputFile.close()
    outFile.close()