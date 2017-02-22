##
# Hyungchol Jun
# 2014-03-02
# P6.16
# Write a program that generates a sequence of 20 random values between 0 and 99 in a list, prints the sequence,
# sorts it, and prints the sorted sequence. Use the list sort method

from random import randrange
def func0317():
    mainlist = []
    print("Printing the sequence")
    for i in range(20):
        r = randrange(0, 99)
        mainlist.append(r)
        print(mainlist[i])

    # sorting the values
    mainlist.sort()
    print("\nPrinting the sorted sequence")
    for j in range(20):
        print(mainlist[j])

