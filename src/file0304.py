##
# Hyungchol Jun
# 2014-03-02
# P6.1
# Write a program that initializes a list with ten random integers and then prints four lines of output, containing
## Every element at an even index
## Every even element
## All elements in reverse order
## Only the first and last element

def subfunc0304(mainlist):
    firstfunc(mainlist)
    secondfunc(mainlist)
    thirdfunc(mainlist)
    fourthfunc(mainlist)

def firstfunc(mainlist):
    print("\n====First Problem====")
    for j in range(1, 11):
        if j % 2 == 1:  # First problem, every element at an even index/////////////////////////ERROR
            print("Even index ", mainlist[j - 1])

def secondfunc(mainlist):
    print("\n====Second Problem====")
    for k in range(0, 10):
        if (mainlist[k] > 0):
            if (mainlist[k] % 2 == 0):  # Second problem, every even element/////////////////////////ERROR
                print("Even element", mainlist[k])

def thirdfunc(mainlist):
    print("\n====Third Problem====")
    for l in range(9, -1, -1):  # Third problem, all elements in reverse order
        if l == 0:
            print("1 st value is ", mainlist[l])
        elif l == 1:
            print("2 nd value is", mainlist[l])
        elif l == 2:
            print("3 rd value is", mainlist[l])
        else:
            print(l, "th value is ", mainlist[l])

def fourthfunc(mainlist):
    print("\n====Fourth Problem====")
    print("The first element is", mainlist[0], "\nAnd the last is", mainlist[len(mainlist) - 1])

from random import randint

def func0304():
    mainlist = []
    for i in range(10):
        r = randint(-2147483647, 2147483647)
        mainlist.append(r)
    subfunc0304(mainlist)
