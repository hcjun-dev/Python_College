##
# Hyungchol Jun
# 2014-03-01
# p6.4 hij


def hfunc(mainlist):  # checking if the list is in order
    if (mainlist == sorted(mainlist)) or (mainlist == sorted(mainlist, reverse=True)):  # in order or in reverse order
        return True
    return False  # if not in order, return False


def ifunc(mainlist):  # Duplicate adjacent
    for i in range(len(mainlist)-2):
        if mainlist[i] == mainlist[i+1]:
            return True
    return False


def jfunc(mainlist):  # Just adjacent
    for i in range(len(mainlist)-1):
        for j in range(i+1, len(mainlist)-1):
            if mainlist[i] == mainlist[j]:
                return True
    return False

def func0306():
    # start of main function
    mainlist = []
    inputv = input("Please input numbers: ")  # Getting input
    while inputv != "":
        mainlist.append(inputv)
        inputv = input("Please input numbers: ")

    # Printing area.
    if hfunc(mainlist):
        print("h function was True")
    else:
        print("h was FALSE")
    if ifunc(mainlist):
        print("i function was True")
    else:
        print("i was FALSE")
    if jfunc(mainlist):
        print("j function was True")
    else:
        print("j was FALSE")
